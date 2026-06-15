# Requests Soup

# Many servers (Amazon, Google, LinkedIn) see this and immediately block the connection (Status 403 or 503)
# because they assume you are a script that will overload their server.
# The Solution: Spoofing Headers

import requests

url = "https://zinduaschool.com/blog/"

# The "Costume" - This tells the server we are a Windows 10 PC using Chrome.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Sending the request with our costume on
response = requests.get(url, headers=headers)
'''
Content Types:
    response.text: The content decoded as a String (Unicode). Use this for HTML and JSON.
    response.content: The content as Bytes. Use this when scraping Images (.jpg), PDFs, or Videos, 
        or passing HTML to BeautifulSoup (to let BeautifulSoup handle encoding).
'''

from bs4 import BeautifulSoup

# Step 1: Feed the HTML content to the Soup
# We use response.content (bytes) instead of text to avoid encoding errors
soup = BeautifulSoup(response.content, "html.parser")

# Now 'soup' is a navigable tree!
# Navigation: Finding Elements

# Find - Scans the document and returns the very first match it sees.
title = soup.find("title")
print(title)

# Find_all - Scans the document and returns the very first match it sees.
headers = soup.find_all("h2")
print(headers)
for header in headers:
    print(header.text)

# Select
links = soup.find_all("a")
for link in links:
    print(link.text)

links2 = soup.select('a')
print(links2[0].text)

# .text: Returns the raw text.
# .get_text(strip=True): Pro Tip. This removes all the messy \n (newlines) and extra spaces around the text.