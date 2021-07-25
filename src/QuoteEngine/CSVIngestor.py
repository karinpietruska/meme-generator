"""Module to import quotes in CSV files."""
from typing import List
import pandas as pd

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Parser to import quotes in CSV files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes in CSV file."""
        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise Exception("File format not parsable Exception")

        quotes_retrieved = list()

        data_df = pd.read_csv(path, header='infer')

        for index, row in data_df.iterrows():
            body = str(row['body'])
            author = str(row['author'])
            quote = QuoteModel(body, author)
            quotes_retrieved.append(quote)
        return quotes_retrieved
