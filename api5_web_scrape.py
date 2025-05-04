# File: webscrape_example5_bs4.py
# Description: Introduction to basic web scraping using requests + BeautifulSoup (bs4)
# References:
# - BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# - requests documentation: https://requests.readthedocs.io/en/latest/
# For more details => Link: https://github.com/anmarjarjees/py-web-scraping

# Import required libraries
# -------------------------
import requests                     # To fetch HTML content from a URL
"""
NOTE:
In the local HTML example, we didn't use "requests" to fetch any data from an external source; 
instead, we just worked with a string containing the HTML content. 

To fix this warning and demonstrate the real-world application of requests, we could either:
1. Use a real website as mentioned, and include requests.get() to fetch the content.
2. Comment out or remove the import if you don't need it, as it won't be needed for local HTML data.
"""
from bs4 import BeautifulSoup       # To parse HTML (bs4 = BeautifulSoup v4)


# Example 1: Scraping a simple local HTML string
# ----------------------------------------------

# For demo purposes, we define a basic HTML page as a string.
# This helps us avoid relying on real websites and makes the demo fully offline.

html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>My Instruments Page</title>
</head>
<body>
    <h1>Welcome to the Instrument Store</h1>
    <ul>
        <li>Guitar</li>
        <li>Piano</li>
        <li>Ukulele</li>
    </ul>
    <p>Check out our <a href="https://www.long-mcquade.com/">Long & McQuade Musical Instruments</a>!</p>
</body>
</html>
"""

# Step 1: Parse the HTML using BeautifulSoup
# ------------------------------------------
# BeautifulSoup takes the HTML string and a parser name ("html.parser" is built-in)
soup = BeautifulSoup(html_doc, 'html.parser')

"""
NOTE:
With a real-website:
url = "https://example.com" # Fetch the webpage content
response = requests.get(url)  # Make the request
soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML
"""


# Step 2: Access and display parts of the page
# ---------------------------------------------

# Get the title of the page
title = soup.title.text
print("Page Title:", title)  # Output: My Instruments Page

# Get the main heading (h1)
heading = soup.h1.text
print("Main Heading:", heading)  # Output: Welcome to the Instrument Store

# Get all list items (<li>)
print("\nList of Instruments:")
for li in soup.find_all('li'):
    print("-", li.text)  # Output each instrument

# Get the link URL and link text
link = soup.find('a')  # Find the first <a> tag
print("\nLink Text:", link.text)
print("Link URL:", link['href'])

# Tip: You can also scrape from a real website like this:
# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# ---------------------------------------------

# ---------------------------------------------
# Final Notes:
# ---------------------------------------------
# - Web scraping is powerful when APIs are not available.
# - Avoid scraping large or dynamic websites (they may block your IP).
# - Learn to inspect HTML structure using browser "Inspect" tool (Right-click > Inspect).
