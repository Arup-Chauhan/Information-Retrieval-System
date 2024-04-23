# Web-based Information Retrieval System for Sneakers

## Project Report Overview

### Abstract
This document outlines the development, objectives, and future steps of our sneaker information retrieval system. The project focuses on automating the extraction, processing, and querying of sneaker-related information from the web.

### Overview
The system is designed using modern Python-based technologies to crawl, parse, index, and retrieve sneaker data. It aims to provide a user-friendly interface for sneaker enthusiasts and researchers.

### Design
Our system integrates multiple components that work in conjunction to provide efficient data retrieval. These components include a web crawler, HTML to JSON parser, text indexer, and a query processor.

### Architecture
The architecture consists of modular components with defined interfaces, allowing for scalable and maintainable software development.

### Operation
The operation of the system is handled through scripted commands which manage the workflow from data crawling to query processing.

### Conclusion
Preliminary results indicate a successful implementation with potential areas for improvement in data accuracy and query speed.

### Data Sources
Data is primarily sourced from Wikipedia, with the system designed to extend to other sneaker-related websites.

### Test Cases
Test frameworks and coverage details will be discussed to ensure the reliability and efficiency of the system.

### Source Code
All source code used in this project is open-source, adhering to MIT licensing, with detailed documentation provided for each component.

## Components

### Sneaker Crawler

The Sneaker Crawler is built using Scrapy to navigate and download relevant sneaker content from Wikipedia within predefined limits.

```python
# Code found in reference GitHub repo
```

### HTML to JSON

This module converts the HTML content scraped by the crawler into JSON format, making it easier for further processing and indexing.

```python
# Code found in reference GitHub repo
```

### Sneaker Indexer

The Sneaker Indexer utilizes a TF-IDF approach implemented with Scikit-Learn to create an efficient search index from the JSON data.

```python
# Code found in reference GitHub repo
```

### Query Processor

The Query Processor uses Flask to handle HTTP requests and outputs the top K relevant sneaker results based on user queries.

```python
# Code found in reference GitHub repo
```

### Sneaker Parser

This component parses detailed sneaker data from JSON, structuring it into a format ready for indexing or direct querying.

```python
# Code found in reference GitHub repo
```

## Installation

```bash
# Instructions to clone and setup the project
git clone [repository-url]
cd [project-directory]
pip install as prompted
# Additional installation steps
```

## Usage

To use the system, follow the detailed steps outlined in the Operation section to activate the crawler, run the indexer, and start the query processor.

## Sample Output

![alt text](https://github.com/Arup-Chauhan/CS429-IR-Project-Deployment/blob/main/Output%20image.png)


## Acknowledgements

Special thanks to Prof. Panchal and all TAs and my peers from class of CS 429 for their guidance and support throughout the project.


