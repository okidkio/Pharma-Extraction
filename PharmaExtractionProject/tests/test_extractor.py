import pytest
from pubmed_extractor.parser import parse_pubmed_xml

SAMPLE_XML = """<?xml version="1.0"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <PMID>12345678</PMID>
      <Article>
        <ArticleTitle>Novel Cancer Therapy Study</ArticleTitle>
        <Journal><JournalIssue><PubDate><Year>2024</Year></PubDate></JournalIssue></Journal>
        <AuthorList>
          <Author>
            <LastName>Smith</LastName>
            <ForeName>John</ForeName>
            <AffiliationInfo>
              <Affiliation>Pfizer Pharmaceuticals Inc, New York, NY</Affiliation>
            </AffiliationInfo>
          </Author>
        </AuthorList>
      </Article>
    </MedlineCitation>
  </PubmedArticle>
</PubmedArticleSet>
"""

def test_parse_pubmed_xml():
    papers = parse_pubmed_xml(SAMPLE_XML)
    assert len(papers) == 1
    assert papers[0].pubmed_id == "12345678"
    assert "John Smith" in papers[0].non_academic_authors
    assert "Pfizer Pharmaceuticals Inc, New York, NY" in papers[0].company_affiliations