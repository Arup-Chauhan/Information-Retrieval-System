import json
from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup

class DocumentParser:
    def __init__(self, output_path="C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/ParsedDocument/ParsedDocument.json"):
        self.parsed_data = []
        self.output_file_path = Path(output_path)

    def parse_html_files(self, html_dir):
        for file_path in Path(html_dir).iterdir():
            if file_path.suffix == ".html":
                with open(file_path, "r", encoding="utf-8") as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'html.parser')
                    title = soup.find("h1", id="firstHeading").get_text()
                    paragraphs = [p.get_text() for p in soup.select("div.mw-content-ltr p")]
                    content = " ".join(paragraphs).replace("\n", " ")
                    self.parsed_data.append({"Sneaker Title": title, "Sneaker Details":content})

    def write_data_to_json(self):
        pd.DataFrame(self.parsed_data).to_json(self.output_file_path, orient='records')

# Driver code
if __name__ == "__main__":
    print ("Started")
    html_folder_path = "C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Web Crawler/ScrappedDocuments"
    html_parser = DocumentParser()
    html_parser.parse_html_files(html_folder_path)
    html_parser.write_data_to_json()
