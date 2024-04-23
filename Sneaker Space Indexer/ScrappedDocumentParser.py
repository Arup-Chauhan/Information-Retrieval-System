import json
from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup

class DocumentParser:
    def __init__(self, output_path="C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/ParsedDocument/ParsedDocument.json"):
        self.parsed_data = []
        self.output_file_path = Path(output_path)

    def extract_content_from_html(self, directory_path):
        html_files = Path(directory_path).glob("*.html")
        for file in html_files:
            with file.open("r", encoding="utf-8") as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                title = soup.find("h1", id="firstHeading").text.strip()
                paragraphs = " ".join(p.text.strip().replace("\n", " ") for p in soup.find_all("p"))
                self.parsed_data.append({"Sneaker Title": title, "Sneaker Details": paragraphs})

    def write_data_to_json(self):
        pd.DataFrame(self.parsed_data).to_json(self.output_file_path, orient='records', lines=True)

# Driver code
if __name__ == "__main__":
    print ("Started")
    html_folder_path = "C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Web Crawler/ScrappedDocuments"
    html_parser = DocumentParser()
    html_parser.extract_content_from_html(html_folder_path)
    html_parser.write_data_to_json()
