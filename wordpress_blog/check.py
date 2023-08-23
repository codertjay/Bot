import requests
import time

# API endpoint
endpoint = "https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStatsBySeason/2022REG/3/20?key=234a48e86a4f4a728edcf200e4bef21f"

# Number of requests and time tracking
num_requests = 0
start_time = time.time()

try:
    while True:
        response = requests.get(endpoint)
        num_requests += 1
        # Print response status code for verification
        print(f"Request {num_requests}: Status Code - {response.json()}")
        # Sleep for a short interval before making the next call
        time.sleep(1)  # Adjust this interval as needed

except KeyboardInterrupt:
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal Requests Made: {num_requests}")
    print(f"Total Time Taken: {total_time:.2f} seconds")
