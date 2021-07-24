from typing import List
import csv 

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Parser for quotes in CSV files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse quotes in CSV file."""
        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise Exception("File format not parsable Exception")

        quotes_retrieved = list()

        with open(path, 'r') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                body = str(row[0])
                author = str(row[1])
                quote = QuoteModel(body,author)
                quotes_retrieved.append(quote)
        return quotes_retrieved 



            
