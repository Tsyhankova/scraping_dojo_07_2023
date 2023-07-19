# run.py
from dotenv import load_dotenv
from scraper import QuoteScraper
import os

if __name__ == "__main__":
    load_dotenv()

    output_file = os.getenv("OUTPUT_FILE")
    if not output_file:
        print("Please set the OUTPUT_FILE environment variable.")
    else:
        scraper = QuoteScraper()
        all_quotes = scraper.fetch_quotes()
        scraper.save_to_file(all_quotes, output_file)