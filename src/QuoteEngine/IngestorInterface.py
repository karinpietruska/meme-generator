"""Abstract Interface for Ingestor classes."""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class IngestorInterface."""
    
    allowed_extensions = ["csv", "docx", "pdf", "txt"]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return true if file has readable format."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes and return list of quotes."""
        pass
