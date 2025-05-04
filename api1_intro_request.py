# File: api1_intro_request.py
# Description: Introduction to APIs and how to use Python's requests library

# Import the 'requests' library for making HTTP calls.
# Links: https://docs.python-requests.org/en/latest/
import requests

# What is an API?
# ---------------
# API stands for Application Programming Interface.
# It allows two systems (like your Python script and a server) to communicate over the internet using HTTP.
# Most APIs return data in JSON format.


# What is a GET request?
# -----------------------
# A GET request is used to retrieve data from a server.
# Think of it like asking a website for information.

# Let's try a simple public API with NO API key.
# This example uses JSONPlaceholder – a free fake online REST API.
# Links: https://jsonplaceholder.typicode.com/

# Define the URL for the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"  # This returns a single blog post (ID: 1)

# Send a GET request to the URL
response = requests.get(url)
# Link: https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content

# Check if the request was successful (status code 200 means OK)
# Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    
    # Display the data (dictionary format)
    print("API response received:\n")
    print(data)

    """
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit    molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    """

    # Access individual fields from the JSON
    print("\nTitle of the post:", data["title"])
else:
    print("Failed to fetch data. Status code:", response.status_code)


# Tip: How to Explore JSON APIs
# -----------------------------
# 1. Use your browser to open the API URL and inspect the structure.
# 2. Use .json() in Python to convert the response to a dictionary.
# 3. Use print() or pprint to inspect the structure and access data.


# Bonus: What if the URL is wrong?
# --------------------------------
# It's a good habit to check status codes and handle exceptions.
# Learn more: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions