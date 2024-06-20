# Web-based Information Retrieval System


### Overview
The system is designed using modern Python-based technologies to crawl, parse, index, and retrieve data. With customizable data topic, the project aims to provide a user-friendly interface for enthusiasts and researchers.

### Design
Our system integrates multiple components that work in conjunction to provide efficient data retrieval. These components include a web crawler, HTML to JSON parser, text indexer, and a query processor


# Operations Guide

## Installation

```bash
# Instructions to clone and setup the project
git clone [repository-url]
cd [project-directory] 
[Sneaker Space Web Crawler]
[Sneaker Space Indexer]
[Sneaker Space Processor]

pip install components as needed

```
## Configuration Guide

The project uses a `config.json` file to manage directory paths and command configurations for different components, ensuring that all parts of the system reference the correct locations and settings.

### Structure of `config.json`

- `crawler`: Contains the directory and command for running the crawler component.
- `scrappedDocuments`: Specifies where the crawled HTML documents are stored.
- `parser`: Defines the script path and input/output directories for the HTML to JSON parser.
- `indexer`: Includes the script path, input JSON file, and output paths for the corpus and index files created by the indexer.
- `processor`: Contains the script path for the query processor and the host and port configuration for the Flask server.

### Using `config.json`

To utilize the `config.json` file, each script should be modified to read the configuration settings at runtime. Here's an example of how you might read the config file in Python:

```python
import json

# Load the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Accessing the configuration for the crawler
crawler_directory = config['crawler']['directory']
crawler_command = config['crawler']['command']

## Setting Up the Project

1. **Creating a Virtual Environment:**
   To isolate the project dependencies, create a virtual environment at the root of the project directory.
   ```bash
   python -m venv venv
   ```

2. **Activating the Virtual Environment:**
   Before running any of the project components, make sure to activate the virtual environment with the following command:
   ```bash
   .\venv\Scripts\activate
   ```

## Running the Crawler

1. **Navigate to the Crawler Directory:**
   Change into the directory containing the crawler:
   ```bash
   cd CS429-IR-Project-Deployment\Sneaker Space Web Crawler\SneakerCrawler
   ```

2. **Start the Crawler:**
   Execute the following command to run the custom crawler `sneaker_crawler`. Note that you do not include the `.py` extension in the command.
   ```bash
   scrapy crawl sneaker_crawler
   ```
   Adjust the `DEPTH_LIMIT` in the `sneaker_crawler.py` to vary the penetration of the crawl. The scraped HTML files will be saved in the `ScrappedDocuments` folder.

## Indexing the Data

1. **Run the HTML to JSON Parser:**
   From the root of the project, navigate to the indexer directory and run the parser to convert HTML files to JSON:
   ```bash
   python ScrappedDocumentParser.py
   ```
   This script reads the HTML documents, extracts the relevant information, and saves it in the `ParsedDocument.json` file located in the `ParsedDocument` folder.

2. **Execute the Indexer Script:**
   Continue in the indexer directory to run the indexing script:
   ```bash
   python SneakerIndexer.py
   ```
   This will process the JSON data, create a document corpus, and generate the TF-IDF index, which are stored in `DocumentCorpus.txt` and `TF-IDF-index.pkl` respectively.

## Query Processing and Running the Flask Server

1. **Run the Query Processor:**
   First, run the query processing script to handle the search queries:
   ```bash
   python SneakerQueryProcessor.py
   ```

2. **Start the Flask Application:**
   Finally, navigate to the processor module and start the Flask server to host the project on `localhost:3000`:
   ```bash
   flask run
   ```

## Testing the Search Functionality

1. **Using Postman for Search Queries:**
   To perform search queries, use Postman or a similar API platform to send a POST request to `localhost:3000/search` with a JSON payload containing the query and the number of top results (`top_k`) desired.

   The response from the Flask server will be the top K relevant sneaker results based on the search query. An output example is provided as 'Output image.png' to showcase the expected search results.

One of the output has been addded as image below.

## Data Sources
Data is primarily sourced from Wikipedia, with the system designed to extend to other sneaker-related websites.

## Test Cases
Test frameworks and coverage details will be discussed to ensure the reliability and efficiency of the system.

## Source Code
All source code used in this project is open-source, adhering to MIT licensing, with detailed documentation provided for each component.

## Components

### Sneaker Crawler

The Sneaker Crawler is built using Scrapy to navigate and download relevant sneaker content from Wikipedia within predefined limits.

### HTML to JSON

This module converts the HTML content scraped by the crawler into JSON format, making it easier for further processing and indexing.


### Indexer

The Sneaker Indexer utilizes a TF-IDF approach implemented with Scikit-Learn to create an efficient search index from the JSON data.


### Query Processor

The Query Processor uses Flask to handle HTTP requests and outputs the top K relevant sneaker results based on user queries.



### Parser

This component parses detailed sneaker data from JSON, structuring it into a format ready for indexing or direct querying.

## Usage

To use the system, follow the detailed steps outlined in the Operation section to activate the crawler, run the indexer, and start the query processor.

## Sample Output

![alt text](https://github.com/Arup-Chauhan/CS429-IR-Project-Deployment/blob/main/Output%20image.png)


## Acknowledgements

Special thanks to Prof. Panchal and all TAs and my peers from class of CS 429 for their guidance and support throughout the project.

