"""Module to import quotes from PDF files."""
import subprocess
import os

from typing import List
from Exceptions import FileNotIngestableError
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Parser class to import quotes from PDF files."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes in pdf file."""
        if type(path) is not str:
            raise TypeError("path must be str")

        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise FileNotIngestableError("File format not ingestable Error")

        quotes_retrieved = list()

        ca_id = subprocess.call(['pdftotext', '-layout',
                                 path, 'temp-pdf-converted.txt'])

        with open('temp-pdf-converted.txt', 'r') as f_txt:
            for text_line in f_txt.readlines():
                text_line = text_line.strip()
                if '-' in text_line and len(text_line) > 1:
                    text_lst = text_line.split('-')
                    body = text_lst[0].replace('"', '').rstrip()
                    author = text_lst[1].lstrip()
                    quote = QuoteModel(body, author)
                    quotes_retrieved.append(quote)

        # remove temporary file
        os.remove('temp-pdf-converted.txt')
        return quotes_retrieved
