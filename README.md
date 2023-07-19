# Quotes Scraper

## Introduction

Quotes Scraper is a web scraping application that extracts quotes, authors, and tags from the website "Quotes to Scrape". It mimics browser behavior using the `requests-html` library to render JavaScript content on the page and fetches quotes from multiple pages.

## Installation

To run the Quotes Scraper, you need to have Python 3.x and the required dependencies installed. Use the following steps to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/Tsyhankova/scraping_dojo_07_2023.git
   cd scraping_dojo_07_2023

2. Create a virtual environment (optional, but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
1. Set up the ".env" file:

Create a new file named ".env" in the root directory of the project.
Add the URL to be scraped and the output file name to the ".env" file.
Optionally, you can include a proxy URL in the ".env" file

2. Run the Quotes Scraper:
    ```bash
    python run.py
###### Due to time constraints, I didn't have a chance to implement the improvements that could be applied to this code. Below are the potential improvements for this project:


## Improvements
1. Enhance error handling to gracefully handle network failures, invalid URLs, and other exceptions that may occur during scraping.
2. Implement throttling mechanisms to avoid overloading the target website with too many requests in a short time.
3. Allow users to specify the number of pages to scrape and other customizations through command-line arguments or user prompts.
4. Add data validation checks to ensure the scraped data is valid and complete.
5. Implement logging to capture relevant information during the scraping process and assist with debugging.
6. Offer multiple output formats (e.g., CSV, Excel) for the scraped data to accommodate different use cases.
