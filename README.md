# Pharma-Extraction
# 🧬 PubMed Pharma Paper Extractor

A Python CLI tool that fetches research papers from PubMed based on a user query, identifies papers with at least one non-academic author affiliated with a pharmaceutical or biotech company, and saves the filtered results into a CSV file.

✅ Built for **Aganitha's Python Take Home Exercise – 2025**

---

## 📌 Features

- 🔍 Uses the **NCBI E-utilities API (PubMed)** to fetch relevant research papers.
- 🧪 Filters papers to identify at least one non-academic author affiliated with a pharmaceutical or biotech company.
- 📥 Saves filtered results into a clean `.csv` file.
- 🧪 Includes basic test cases using **pytest**.
- 📦 Organized with **Poetry** for clean dependency and project management.

---

## 🗂️ Project Structure

```
get-papers-list/

├── src/
│   └── get_papers/
│       ├── main.py          # CLI entry point
│       └── pubmed.py        # Fetch + filter logic

├── tests/
│   └── test_main.py         # Test cases

├── requirements.txt

├── pyproject.toml

└── README.md
```

---

# 🚀 How to Set Up & Run the Project

## ⚠️ Prerequisites

Make sure you have:

- Python **3.9+**
- Poetry installed

---

## Clone the Repository

```bash
git clone https://github.com/okidkio/get-papers-list.git

cd get-papers-list
```

---

## Set Up Environment Using Poetry (Recommended)

Install dependencies:

```bash
poetry install
```

---

## Run the CLI Tool

```bash
poetry run get-papers-list --query "covid vaccine" --output results.csv --max_results 15
```

---

## Optional: Run with Virtual Environment

If you prefer not to use Poetry:

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/get_papers/main.py --query "covid vaccine" --output results.csv --max_results 15
```

---

# ⚙️ Command-Line Options

| Option | Description |
|--------|-------------|
| `--query` | Search query for PubMed (example: `"lung cancer"`) |
| `--output` | Path to save the filtered CSV output |
| `--max_results` | Optional limit on the number of papers retrieved |

---

# 🔧 Tools & Libraries Used

- 🐍 **Python 3.9+**
- 📦 **Poetry** – Dependency and project management
- 🌐 **Requests** – API integration
- 🐼 **Pandas** – CSV handling
- ⏳ **TQDM** – Progress display
- 🧪 **Pytest** – Unit testing
- 🤖 **OpenAI GPT** – Author affiliation classification (if integrated)

---

# 🧪 Run Tests

Using Poetry:

```bash
poetry run pytest
```

Or using pytest directly:

```bash
pytest
```

---

# 👤 Author

**Shiwani Wasnik**

GitHub:  
https://github.com/okidkio

Email:  
wasnikshiwani6@gmail.com
