# Scrape Product Prices & Convert Currency
# Scrape product prices from a local e-commerce website and convert them into another currency (e.g., USD to KES).

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# STEP 1: Scrape books
url = "https://books.toscrape.com/"

response = requests.get(url)
# response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

books = soup.select("article.product_pod")

book_data = []

# Collect first 10 books
for book in books[:10]:
    title = book.h3.a["title"].strip()

    # Example price format: £51.77
    price_text = book.select_one(".price_color").text.strip()

    # Remove currency symbol and convert to float
    price_gbp = float(price_text.replace("£", ""))

    book_data.append({
        "title": title,
        "price_gbp": price_gbp
    })

# STEP 2: Get exchange rate
# Free API
api_url = "https://open.er-api.com/v6/latest/GBP"

rate_response = requests.get(api_url)

rate_data = rate_response.json()
print(rate_data)

gbp_to_usd = rate_data["rates"]["USD"]

print(f"Current GBP → USD rate: {gbp_to_usd}")


# STEP 3: Convert prices
for item in book_data:
    item["price_usd"] = round(
        item["price_gbp"] * gbp_to_usd,
        2
    )
print(book_data)

# STEP 4: Save to JSON
json_file = "books_prices.json"

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(book_data, f, indent=4)

print(f"JSON saved: {json_file}")


# STEP 5: Save to CSV
df = pd.DataFrame(book_data)
csv_file = "books_prices.csv"
df.to_csv(csv_file, index=False)
print(f"CSV saved: {csv_file}")

# Preview data
print(df.head())



