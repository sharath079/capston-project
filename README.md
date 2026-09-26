# Zepto Data & AI Platform

This capstone repository contains three modules:

- `zepto-data-ai-platform\data_pipeline` - scrape book listings, clean the data, and store it in SQLite.
- `zepto-data-ai-platform\analytics` - explore and model the Titanic dataset in Jupyter notebooks.
- `zepto-data-ai-platform\support_assistant` - run a FastAPI support assistant in mock mode.

## Run on Windows

The commands below are for PowerShell. Start in the repository root: the directory containing this `README.md` and the `zepto-data-ai-platform` folder. If needed, change to that directory first:

```powershell
cd "D:\path\to\your\cloned-repository"
```

### 1. Install Python dependencies

Check that the Python launcher is installed:

```powershell
py --version
```

Create a virtual environment, activate it, and install the project dependencies:

```powershell
$project = Join-Path (Get-Location) "zepto-data-ai-platform"
py -m venv "$project\.venv"
& "$project\.venv\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install -r "$project\requirements.txt"
```

If PowerShell blocks virtual environment activation, allow it for this terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
& "$project\.venv\Scripts\Activate.ps1"
```

Keep this PowerShell window open so the virtual environment remains active. If `py` is not recognized, install Python from [python.org](https://www.python.org/downloads/windows/), enable the option to add Python to PATH, then reopen PowerShell.

### 2. Run the data pipeline

Run both scripts from the data pipeline directory because they read and write files relative to the current directory:

```powershell
Set-Location "$project\data_pipeline"
python .\scrape_books.py
python .\clean_store.py
```

The scraper writes `raw_books.csv`; the cleaning step writes or updates `books.db`. The fixed conversion rate is 1 GBP = 105.50 INR. The cleaner inserts rows into the database, so rerunning it on an existing database can add duplicate book rows.

To inspect the SQL examples, open `queries.sql` in this directory or run `pipeline_notebook.ipynb` in VS Code. For more detail, see [the data pipeline guide](zepto-data-ai-platform/data_pipeline/README.md).

### 3. Run the analytics notebooks

The notebooks need Jupyter support. Install it into the active virtual environment:

```powershell
python -m pip install notebook ipykernel
Set-Location "$project\analytics"
python -m notebook
```

In the Jupyter page that opens, run `01_eda.ipynb` first, then `02_modeling.ipynb`. The first notebook downloads the Titanic dataset through Seaborn and saves `titanic.csv`; the second notebook reads that CSV and saves the trained model as `saved_pipeline.joblib`.

Alternatively, open the `analytics` folder in VS Code, choose the active `.venv` as the notebook kernel, and run the notebooks in the same order. The Titanic dataset download requires internet access. See [the analytics guide](zepto-data-ai-platform/analytics/README.md).

### 4. Start the support assistant

In the same PowerShell window, start the API from its module directory:

```powershell
Set-Location "$project\support_assistant"
python -m uvicorn app:app --reload
```

Keep this window open while using the API. Open the interactive API page at <http://127.0.0.1:8000/docs>, or try this request in a browser:

<http://127.0.0.1:8000/ask?query=What%20is%20Zepto%27s%20refund%20policy%3F>

Stop the server with `Ctrl+C`. The current API uses a deterministic mock response; it does not retrieve live policy content or call a real language model. `embed_store.py` is not required to start or use the current mock API. See [the support assistant guide](zepto-data-ai-platform/support_assistant/README.md).

### Start the API without activating the virtual environment

If the environment is not activated, use its Python executable explicitly. Run these commands from the repository root:

```powershell
$project = Join-Path (Get-Location) "zepto-data-ai-platform"
Set-Location "$project\support_assistant"
& "$project\.venv\Scripts\python.exe" -m uvicorn app:app --reload
```

This is also useful if another Python installation is selected by the `python` command.
