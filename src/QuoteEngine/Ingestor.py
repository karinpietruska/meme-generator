"""Module for reading in quotes from files."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Class for reading in quotes from files."""

    allowed_parsers = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a given file."""
        for file_parser in cls.allowed_parsers:
            if file_parser.can_ingest(path):
                qmodel_list = file_parser.parse(path)
                return qmodel_list
