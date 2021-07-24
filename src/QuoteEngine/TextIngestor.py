from typing import List 
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse quotes in txt file."""
        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise Exception("File format not parsable Exception")

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

