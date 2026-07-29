import csv
import io
from flask import Flask, render_template, request, Response
from pubmed_extractor.api import fetch_pubmed_papers
from pubmed_extractor.parser import parse_pubmed_xml

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    papers = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            xml_data = fetch_pubmed_papers(query)
            if xml_data:
                papers_obj = parse_pubmed_xml(xml_data)
                papers = [p.to_dict() for p in papers_obj]
    
    return render_template("index.html", papers=papers, query=query)

@app.route("/export", methods=["POST"])
def export():
    query = request.form.get("query", "").strip()
    xml_data = fetch_pubmed_papers(query)
    papers_obj = parse_pubmed_xml(xml_data)
    
    output = io.StringIO()
    fieldnames = ["pubmed_id", "title", "pub_date", "non_academic_authors", "company_affiliations", "paper_url"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for p in papers_obj:
        writer.writerow(p.to_dict())
    
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=pubmed_pharma_results.csv"}
    )

if __name__ == "__main__":
    app.run(debug=True)