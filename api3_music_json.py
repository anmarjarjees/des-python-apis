# File: api_example3_music_json.py
# Description: Demonstrates how to fetch and parse musical instrument data from a custom JSON API.
# Link to API: https://anmarjarjees.github.io/json-examples/music-inst.json

# Import the 'requests' library to perform HTTP operations.
# Official Docs: https://requests.readthedocs.io/en/latest/
import requests


# Step 1: Define the API endpoint (public, no API key needed)
# -----------------------------------------------------------
url = "https://anmarjarjees.github.io/json-examples/music-inst.json"

# Step 2: Send a GET request to fetch the JSON data
response = requests.get(url)

# Step 3: Check if the request was successful (status code 200)
# HTTP Status Codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
if response.status_code == 200:
    instruments = response.json()  # Convert JSON to Python data (list of dicts)
    
    print("List of Musical Instruments:\n")

    # Step 4: Loop through each instrument in the JSON data
    for item in instruments:
        print(f"Instrument Name: {item['name']}")
        print(f"History: {item['history']}")
        
        # Access nested specs dictionary
        specs = item.get("specs", {})
        types = specs.get("type", [])
        categories = specs.get("category", [])

        print("  Types Available:")
        for t in types:
            print(f"    - {t}")

        print("  Categories:")
        for c in categories:
            print(f"    - {c}")

        print("-" * 40)  # Divider for readability

else:
    print("Failed to retrieve data. HTTP Status Code:", response.status_code)

# Tips:
# -----
# - Always check the API structure before coding (open it in the browser).
# - Use .get() when accessing dictionary keys to avoid errors if the key doesn't exist.
# - You can adapt this code for other JSON APIs with similar nested structure.

# JSON Explorer Tools (Optional):
# - https://jsonformatter.org/json-viewer
# - https://jsoneditoronline.org/