# File 4: api_example4_query_params.py
# Description: Demonstrating how to use query parameters in API requests using the requests library

import requests

# This is the URL for the mock API endpoint (Your music instruments data).
url = "https://anmarjarjees.github.io/json-examples/music-inst.json"

# Query Parameter Example: 
# We want to filter the data based on a specific instrument name (example: "Piano")
# Construct the query parameter to filter based on the instrument name
params = {"name": "Piano"}

# Send a GET request with the query parameters
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    
    # Display the fetched data
    print("Filtered Data for 'Piano':")
    print(data)

    # Example of filtering within the response (if it is a list of items)
    for instrument in data:
        if instrument["name"] == "Piano":
            print(f"Instrument Name: {instrument['name']}")
            print(f"History: {instrument['history']}")
            print(f"Specs: {instrument['specs']}")
            print("------------")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Additional Info:
# When using query parameters:
# 1. We pass a dictionary to the `params` argument in `requests.get()`.
# 2. The parameters are automatically encoded into the URL.
# Link: https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
