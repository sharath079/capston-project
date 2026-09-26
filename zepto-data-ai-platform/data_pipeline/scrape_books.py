import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=5):
    books = []
    for page in range(1, pages+1):
        url = BASE_URL.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        for item in soup.select(".product_pod"):
            title = item.h3.a["title"]
            price = item.select_one(".price_color").text.strip("£")
            rating = item.p["class"][1]
            availability = item.select_one(".availability").text.strip()
            category = "All Products"
            books.append([title, price, rating, availability, category])
    return pd.DataFrame(books, columns=["title","price_gbp","star_rating","availability","category"])

if __name__ == "__main__":
    df = scrape_books()
    df.to_csv("raw_books.csv", index=False)
    print("Scraping complete. Saved raw_books.csv")
