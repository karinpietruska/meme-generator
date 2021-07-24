import docx 
from typing import List 
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse quotes in Docx file."""
        ingestable = cls.can_ingest(path)
        if not ingestable:
            raise Exception("File format not parsable Exception")

        quotes_retrieved = list()

        document = docx.Document(path)
        for p in document.paragraphs:
            text_line = p.text
            if len(text_line) > 0: 
                text_lst = text_line.split('-')
                body = text_lst[0].replace('"','').rstrip()
                author = text_lst[1].lstrip()
                quote = QuoteModel(body, author)
                quotes_retrieved.append(quote)

        return quotes_retrieved

