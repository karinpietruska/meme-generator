"""Module to import quotes from txt Files."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from Exceptions import FileNotIngestableError


class TextIngestor(IngestorInterface):
    """Parser class to import quotes from txt files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes in txt file."""
        if type(path) is not str:
            raise TypeError("path must be str")
        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise FileNotIngestableError("File format not ingestable Error")

        quotes_retrieved = list()

        with open(path, 'r') as f_txt:
            for text_line in f_txt.readlines():
                text_line = text_line.strip()
                if '-' in text_line and len(text_line) > 1:
                    text_lst = text_line.split('-')
                    body = text_lst[0].strip().replace('\ufeff', '')
                    author = text_lst[1].strip()
                    quote = QuoteModel(body, author)
                    quotes_retrieved.append(quote)

        return quotes_retrieved
