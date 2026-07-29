import requests

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_papers(query, max_results=20):
    # Search PubMed
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    resp = requests.get(ESEARCH_URL, params=search_params)
    resp.raise_for_status()
    id_list = resp.json().get("esearchresult", {}).get("idlist", [])

    if not id_list:
        return ""

    # Fetch PubMed XML Details
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    fetch_resp = requests.get(EFETCH_URL, params=fetch_params)
    fetch_resp.raise_for_status()
    return fetch_resp.text