# Zepto Data & AI Platform

This repository contains the **Zepto Data & AI Platform** capstone project, built as a single connected system with three modules:

- `/data_pipeline` — Scraping, cleaning, and storing catalog-style data in SQLite.
- `/analytics` — Titanic dataset profiling, EDA, and predictive modeling.
- `/support_assistant` — GenAI-powered support assistant with LangGraph + FastAPI.

---

## Setup Instructions

### Requirements
You may use either:
- One consolidated `requirements.txt` at the root, or
- Separate `requirements.txt` files per module.

Example consolidated requirements:

requests
beautifulsoup4
pandas
sqlite3-binary
seaborn
matplotlib
scikit-learn
imbalanced-learn
joblib
sentence-transformers
chromadb
fastapi
uvicorn
langgraph


Install dependencies:
```bash
pip install -r requirements.txt

## Running Each Module

1. Data Pipeline (/data_pipeline)
Run the scraping + cleaning script:

bash
python data_pipeline/scrape_books.py
This generates books.db with normalized schema.

Execute SQL queries from queries.sql using sqlite3 or inside the notebook.

Outputs include ≥60 books, cleaned fields, and INR conversion (fixed rate: 1 GBP = 105.50 INR).

2. Analytics Pipeline (/analytics)
Open 01_eda.ipynb and run all cells:

Loads Titanic dataset via sns.load_dataset("titanic")

Saves titanic.csv as offline fallback

Profiles, cleans, and performs EDA

Then run 02_modeling.ipynb:

Stratified train/test split

Preprocessing pipeline (ColumnTransformer + Pipeline)

Logistic Regression, Decision Tree, Random Forest

Evaluation metrics, imbalance handling, hyperparameter tuning

Regression side-task (predict fare)

Saves full pipeline with joblib.dump


3. Support Assistant (/support_assistant)
Ensure 8 policy documents exist in /support_assistant/docs/.

Run embedding script:

bash
python support_assistant/embed_store.py
Start FastAPI service:

bash
uvicorn support_assistant.app:app --reload
Query the assistant:

Code
http://127.0.0.1:8000/ask?query="What is Zepto's refund policy?"

Design Decisions
Data Pipeline: Chose SQLite for lightweight relational storage; schema normalized with PK/FK between categories and books.

Analytics: Two-notebook structure ensures single dataset load; strict threshold-based missing value handling; stratified split prevents class imbalance leakage.

Support Assistant: Deterministic mock mode (MOCK_LLM=1) ensures offline reproducibility; embeddings stored in ChromaDB for fast retrieval; LangGraph orchestrates intent classification, retrieval, and answer generation.

Acceptance Criteria Checklist
[1] ≥60 books scraped, cleaned, stored in SQLite

[2] INR conversion at fixed baseline rate

[3] ≥5 SQL queries with required clauses + JOIN

[4] Titanic dataset profiled, cleaned, EDA completed

[5] Stratified train/test split, preprocessing pipeline

[6] 3 classifiers trained + evaluated, imbalance handling

[7] Random Forest tuned with GridSearchCV + OOB score

[8] Regression side-task with metrics + residual plot

[9] Final comparison table + deployment recommendation

[10] Full pipeline saved with joblib.dump

[11] Support assistant runs offline with mock LLM

[12] FastAPI endpoint responds with grounded answers

[13] Commit history shows feature branch merged into main

Git Workflow
At least one feature branch created, committed to ≥2 times, and merged back into main.

Verified via git log --graph --all.

Submission
Submit exactly one public GitHub repository link containing:

Root README.md (this file)

/data_pipeline, /analytics, /support_assistant folders

Requirements file(s)

Commit history with branch/merge activity

Code
