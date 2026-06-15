Week 2 Project

# Price Scraper + Currency Converter

## Scrape Product Prices & Convert Currency

### Goal:

Scrape product prices from a local e-commerce website and convert them into another currency (e.g., USD to KES).

### Instructions:

Use requests and BeautifulSoup to scrape prices of at least 10 products. Use this website - "https://books.toscrape.com/" or https://www.jumia.co.ke/
Store product name and price (in original currency).
Use a free currency conversion API (e.g., exchangerate-api.com).
Convert prices to another currency and save the data into a CSV or JSON file.

### Features to implement:

Collect and clean product name + price or book title + price.
Display the products with converted prices in a readable table format using pandas or tabulate.
Include error handling for connection issues.

### Optional extensions:

Allow user to select which currencies to convert between.
Add timestamp for when conversion was done.
Plot a simple bar chart of original vs. converted prices using matplotlib.