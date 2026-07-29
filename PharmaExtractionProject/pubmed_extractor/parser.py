import re
import xml.etree.ElementTree as ET

# Pre-defined sets for O(1) lookups
PHARMA_KEYWORDS = {
    "pharma", "pharmaceuticals", "biotech", "biotechnology", "inc", "ltd", "corp", 
    "corporation", "gmbh", "therapeutics", "pfizer", "novartis", "roche", "merck", 
    "astrazeneca", "sanofi", "glaxosmithkline", "gsk", "bayer", "eli lilly"
}

ACADEMIC_KEYWORDS = {
    "university", "college", "school", "hospital", "clinic", "institute", "academy"
}

class Paper:
    # Hack 3: __slots__ for memory optimization
    __slots__ = ('pubmed_id', 'title', 'pub_date', 'non_academic_authors', 'company_affiliations', 'paper_url')
    
    def __init__(self, pubmed_id, title, pub_date, non_academic_authors, company_affiliations, paper_url):
        self.pubmed_id = pubmed_id
        self.title = title
        self.pub_date = pub_date
        self.non_academic_authors = non_academic_authors
        self.company_affiliations = company_affiliations
        self.paper_url = paper_url

    def to_dict(self):
        return {
            "pubmed_id": self.pubmed_id,
            "title": self.title,
            "pub_date": self.pub_date,
            "non_academic_authors": ", ".join(self.non_academic_authors),
            "company_affiliations": ", ".join(self.company_affiliations),
            "paper_url": self.paper_url
        }

def parse_pubmed_xml(xml_content):
    root = ET.fromstring(xml_content)
    papers = []

    pharma_set = PHARMA_KEYWORDS
    academic_set = ACADEMIC_KEYWORDS

    for article in root.findall(".//PubmedArticle"):
        pmid_elem = article.find(".//MedlineCitation/PMID")
        pubmed_id = pmid_elem.text if pmid_elem is not None else ""
        if not pubmed_id:
            continue

        title_elem = article.find(".//ArticleTitle")
        title = title_elem.text if title_elem is not None else "N/A"

        pub_date_elem = article.find(".//Journal/JournalIssue/PubDate/Year")
        pub_date = pub_date_elem.text if pub_date_elem is not None else "N/A"

        # Direct standardized PubMed paper URL
        paper_url = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"

        non_academic_authors = []
        company_affiliations = set()

        for author in article.findall(".//AuthorList/Author"):
            last_name = author.findtext("LastName", "")
            fore_name = author.findtext("ForeName", "")
            author_name = f"{fore_name} {last_name}".strip()

            affil_elems = author.findall(".//AffiliationInfo/Affiliation")
            for affil in affil_elems:
                affil_text = affil.text or ""
                affil_lower = affil_text.lower()
                
                # Precise word-level matching
                words = set(re.findall(r'\b\w+\b', affil_lower))
                
                # Hack 1: O(1) set operations
                if (words & pharma_set) and not (words & academic_set):
                    if author_name and author_name not in non_academic_authors:
                        non_academic_authors.append(author_name)
                    company_affiliations.add(affil_text)

        if non_academic_authors:
            papers.append(Paper(pubmed_id, title, pub_date, non_academic_authors, list(company_affiliations), paper_url))

    return papers