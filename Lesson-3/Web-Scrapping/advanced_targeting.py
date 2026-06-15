# Advanced Targeting

import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'

response = requests.get(url)
# Feed the HTML content to the Soup
soup = BeautifulSoup(response.content, "html.parser")

# The Dot . (Class Selector)
# 1. Basic Class Selection
# Find all elements with class="price"
prices = soup.select(".product_price")
price = soup.select(".product_color")

for p in price:
    print(p.get_text(strip=True)) # Output:

# 2. Chained Classes (Specific Targeting)
# Find a book that is BOTH a "book" AND a "special-offer"
special_book = soup.select_one(".book.star-rating Four")
# print(special_book.select_one("h2").text)
print(special_book) # Output: