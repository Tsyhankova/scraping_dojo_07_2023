# scraper.py
import random
import requests
import time
import json
import os
from requests_html import HTMLSession

class QuoteScraper:
    def __init__(self):
        self.base_url = os.getenv("URL")
        self.session = HTMLSession()

    def fetch_quotes(self):
        all_quotes = []
        page = 1

        while True:
            url = f"{self.base_url}page/{page}/"
            try:
                response = self.session.get(url)
                response.raise_for_status()
                response.html.render(sleep=10, keep_page=True)
                quotes_elements = response.html.find('.quote')
                if not quotes_elements:
                    break

                for quote_element in quotes_elements:
                    text = quote_element.find('.text', first=True).text.strip('“”')
                    author = quote_element.find('.author', first=True).text
                    tags = [tag.text for tag in quote_element.find('.tag')]
                    all_quotes.append({"text": text, "by": author, "tags": tags})

                # Introduce a random delay to simulate human-like behavior
                delay = random.uniform(10, 13)
                time.sleep(delay)

                page += 1

            except (requests.exceptions.RequestException, ValueError) as e:
                print(f"Error fetching data from {url}: {e}")
                break

        return all_quotes

    def save_to_file(self, quotes, output_file):
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                for quote in quotes:
                    json.dump(quote, file, ensure_ascii=False)
                    file.write("\n")
            print(f"Quotes saved to {output_file} successfully.")
        except IOError as e:
            print(f"Error saving quotes to {output_file}: {e}")
