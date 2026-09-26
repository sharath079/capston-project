# Data Pipeline Module

This module scrapes book data from [Books to Scrape](http://books.toscrape.com), cleans it, converts prices to INR, and stores it in a normalized SQLite database.

## Steps
1. Run `scrape_books.py` → saves raw_books.csv  
2. Run `clean_store.py` → cleans data and stores in books.db  
3. Execute queries in `queries.sql` → demonstrates SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, JOIN  
4. Use `pipeline_notebook.ipynb` → shows full pipeline, SQL queries, and pandas merge equivalence  

## Schema
- **categories**(id, name)  
- **books**(id, title, price_gbp, price_inr, rating, in_stock, category_id)  

## Fixed Conversion Rate
- 1 GBP = 105.50 INR (project-defined constant)

## Outputs
- `raw_books.csv`  
- `books.db` (SQLite database)  
- SQL query results and pandas merge demonstration
