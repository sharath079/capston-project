import pandas as pd
import sqlite3

def clean_books(df):
    rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    price_gbp = df["price_gbp"].astype("string").str.replace(r"[^\d.-]", "", regex=True)
    df["price_gbp"] = pd.to_numeric(price_gbp, errors="raise")
    df["rating"] = df["star_rating"].map(rating_map)
    df["in_stock"] = df["availability"].str.contains("In stock")
    df["price_inr"] = df["price_gbp"] * 105.50
    return df.drop(columns=["star_rating","availability"])

def store_sqlite(df):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    cur.execute("""CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price_gbp REAL,
        price_inr REAL,
        rating INTEGER,
        in_stock INTEGER,
        category_id INTEGER REFERENCES categories(id))""")
    for cat in df["category"].unique():
        cur.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)",(cat,))
    for _,row in df.iterrows():
        cat_id = cur.execute("SELECT id FROM categories WHERE name=?",(row["category"],)).fetchone()[0]
        cur.execute("INSERT INTO books(title,price_gbp,price_inr,rating,in_stock,category_id) VALUES (?,?,?,?,?,?)",
                    (row["title"],row["price_gbp"],row["price_inr"],row["rating"],int(row["in_stock"]),cat_id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv("raw_books.csv")
    df = clean_books(df)
    store_sqlite(df)
    print("Data cleaned and stored in books.db")
