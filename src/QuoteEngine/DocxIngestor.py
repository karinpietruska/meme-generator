"""Module to import quotes from Docx Files."""
import docx
from typing import List

from Exceptions import FileNotIngestableError
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parser class to import quotes from Docx files."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes in Docx file."""
        if type(path) is not str:
            raise TypeError("path must be str")

        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise FileNotIngestableError("File format not ingestable Error")

        quotes_retrieved = list()

        document = docx.Document(path)
        for p in document.paragraphs:
            text_line = p.text
            if len(text_line) > 0:
                text_lst = text_line.split('-')
                body = text_lst[0].replace('"', '').rstrip()
                author = text_lst[1].lstrip()
                quote = QuoteModel(body, author)
                quotes_retrieved.append(quote)

        return quotes_retrieved
