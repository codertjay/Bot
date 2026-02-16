import argparse
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv

BASE_URL = "https://solodit.cyfrin.io/api/v1/solodit/findings"
DEFAULT_PAGE_SIZE = 100
RATE_LIMIT_STATUS = 429
ISSUE_PREFIX = "audit_"
ISSUE_PADDING = 5


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export all Move findings from the Solodit API into local markdown files."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("audit"),
        help="Directory to store generated issue files (default: ./audit).",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=DEFAULT_PAGE_SIZE,
        help="Number of findings to fetch per API page (max 100).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Optional hard limit on the number of pages to process.",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=None,
        help="Override automatic numbering and start from a specific issue index.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and log findings without writing files.",
    )
    return parser.parse_args()


def load_api_key() -> str:
    load_dotenv()
    api_key = os.getenv("SOLODIT_API_KEY")
    if not api_key:
        raise RuntimeError("SOLODIT_API_KEY is not set. Supply it via environment or .env file.")
    return api_key


def determine_start_index(output_dir: Path) -> int:
    max_index = 0
    for issue_file in output_dir.glob(f"{ISSUE_PREFIX}*.md"):
        # Continue numbering from the last sequential issue file.
        suffix = issue_file.stem.replace(ISSUE_PREFIX, "", 1)
        if suffix.isdigit():
            max_index = max(max_index, int(suffix))
    return max_index + 1


def wait_for_rate_limit(headers: Dict[str, str]) -> None:
    reset_header = headers.get("X-RateLimit-Reset")
    now = int(time.time())
    reset_ts = int(reset_header) if reset_header and reset_header.isdigit() else now + 5
    sleep_for = max(reset_ts - now, 5)
    print(f"Rate limit hit. Sleeping for {sleep_for} seconds...")
    time.sleep(sleep_for)


def fetch_page(
        session: requests.Session,
        api_key: str,
        page: int,
        page_size: int,
        retries: int = 3,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "page": page,
        "pageSize": page_size,
        "filters": {
            "languages": [{"value": "Move"}],
        },
    }
    headers = {
        "Content-Type": "application/json",
        "X-Cyfrin-API-Key": api_key,
    }

    for attempt in range(retries):
        response = session.post(BASE_URL, headers=headers, json=payload, timeout=30)
        if response.status_code == RATE_LIMIT_STATUS:
            wait_for_rate_limit(response.headers)
            continue
        try:
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"API request failed after {retries} attempts") from exc
            backoff = 2 ** attempt
            print(f"Request failed ({exc}). Retrying in {backoff} seconds...")
            time.sleep(backoff)
    raise RuntimeError("Unreachable: fetch_page exhausted retries")


def flatten_tags(finding: Dict[str, Any], key: str) -> List[str]:
    parent = finding.get(key) or []
    titles: List[str] = []
    for entry in parent:
        tag = entry.get("tags_tag") or {}
        title = tag.get("title")
        if title:
            titles.append(title)
    return titles


def flatten_finders(finding: Dict[str, Any]) -> List[str]:
    users: List[str] = []
    for finder in finding.get("issues_issue_finders", []) or []:
        warden = finder.get("wardens_warden") or {}
        handle = warden.get("handle")
        if handle:
            users.append(handle)
    return users


def protocol_categories(finding: Dict[str, Any]) -> List[str]:
    protocol = finding.get("protocols_protocol") or {}
    scores = protocol.get("protocols_protocolcategoryscore") or []
    categories: List[str] = []
    for score in scores:
        category = score.get("protocols_protocolcategory") or {}
        title = category.get("title")
        if title:
            categories.append(title)
    return categories


def render_issue_markdown(finding: Dict[str, Any]) -> str:
    tags = flatten_tags(finding, "issues_issuetagscore")
    finders = flatten_finders(finding)
    categories = protocol_categories(finding)
    header_lines = [
        # "---",
        # f"id: {finding.get('id')}",
        # f"impact: {finding.get('impact')}",
        # f"quality_score: {finding.get('quality_score')}",
        # f"rarity_score: {finding.get('general_score')}",
        # f"firm: {finding.get('firm_name')}",
        # f"protocol: {finding.get('protocol_name')}",
        # f"protocol_categories: {', '.join(categories) if categories else 'N/A'}",
        # f"report_date: {finding.get('report_date')}",
        # f"contest_link: {finding.get('contest_link')}",
        # f"source_link: {finding.get('source_link')}",
        # f"github_link: {finding.get('github_link')}",
        # f"pdf_link: {finding.get('pdf_link')}",
        # f"finders: {', '.join(finders) if finders else 'N/A'}",
        # f"tags: {', '.join(tags) if tags else 'N/A'}",
        # "---",
    ]
    summary = finding.get("summary") or "No summary provided."
    content = finding.get("content") or "No content provided."
    body_lines = [
        f"# {finding.get('title')}",
        "",
        "## Summary",
        summary.strip(),
        "",
        "## Details",
        content.strip(),
    ]
    return "\n".join(header_lines + body_lines).rstrip() + "\n"


def write_issue_file(output_dir: Path, index: int, finding: Dict[str, Any]) -> Path:
    filename = output_dir / f"{ISSUE_PREFIX}{index:0{ISSUE_PADDING}d}.md"
    filename.write_text(render_issue_markdown(finding), encoding="utf-8")
    return filename


def export_findings(args: argparse.Namespace) -> None:
    api_key = load_api_key()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    start_index = args.start_index or determine_start_index(args.output_dir)
    session = requests.Session()
    page = 1
    total_pages: Optional[int] = None
    issue_index = start_index

    while True:
        if args.max_pages and page > args.max_pages:
            print("Reached max page limit; stopping.")
            break
        payload = fetch_page(session, api_key, page=page, page_size=args.page_size)
        findings = payload.get("findings", [])
        metadata = payload.get("metadata", {})
        total_pages = metadata.get("totalPages") or total_pages
        if not findings:
            print("No more findings returned; stopping.")
            break
        for finding in findings:
            if args.dry_run:
                print(f"[{issue_index:05d}] {finding.get('title')}")
            else:
                written = write_issue_file(args.output_dir, issue_index, finding)
                rel_path = written.resolve().relative_to(Path.cwd())
                print(f"Saved {rel_path}")
            issue_index += 1
        page += 1
        if total_pages and page > total_pages:
            break

    print(
        f"Processed {issue_index - start_index} findings. Files are under {args.output_dir.resolve()}"
    )


def main() -> None:
    try:
        args = parse_args()
        export_findings(args)
    except Exception as exc:  # Surface actionable errors to the caller.
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
