import unittest
import os
from scraper import QuoteScraper

class TestQuoteScraper(unittest.TestCase):

    def test_fetch_quotes(self):
        scraper = QuoteScraper()
        quotes = scraper.fetch_quotes()

        # Check if quotes is a list
        self.assertIsInstance(quotes, list)

        # Check if each quote has required fields: text, by, and tags
        for quote in quotes:
            self.assertIn("text", quote)
            self.assertIn("by", quote)
            self.assertIn("tags", quote)

            # Check if text, by, and tags are not empty
            self.assertTrue(quote["text"])
            self.assertTrue(quote["by"])
            self.assertTrue(quote["tags"])

    def test_save_to_file(self):
        # Create a temporary file for testing
        test_file = "test_output.jsonl"

        quotes = [
            {
                "text": "Quote 1",
                "by": "Author 1",
                "tags": ["tag1", "tag2"]
            },
            {
                "text": "Quote 2",
                "by": "Author 2",
                "tags": ["tag3", "tag4"]
            }
        ]

        # Test saving to file
        scraper = QuoteScraper()
        scraper.save_to_file(quotes, test_file)

        # Check if the file was created and not empty
        with open(test_file, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertTrue(content)

        # Clean up the temporary file
        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
