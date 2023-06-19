import re
import PyPDF2


def hide_email_addresses(input_pdf, output_pdf):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    rectangle_color = (0, 0, 0)  # RGB color for the black rectangle

    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num, page in enumerate(pdf_reader.pages):
            text_layer = page.extract_text()

            email_matches = re.findall(email_regex, text_layer)
            for email in email_matches:
                page_width = page.mediabox[2]
                page_height = page.mediabox[3]
                x, y, width, height = 0, 0, page_width, page_height

                # Calculate the coordinates of the rectangle to cover the email address
                x_min, y_min, x_max, y_max = x, y, x + width, y + height

                # Add a black rectangle to cover the email address
                page.mergeRect(x_min, y_min, x_max, y_max, rectangle_color)

            pdf_writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f"Email addresses hidden and saved to {output_pdf}.")


# Usage example:
hide_email_addresses('input.pdf', 'output.pdf')
