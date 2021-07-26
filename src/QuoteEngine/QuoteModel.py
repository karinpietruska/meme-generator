"""Module with class to encapsulate quote."""


class QuoteModel():
    """A class used to encapsulate body and author of a quote."""

    def __init__(self, body, author):
        """Initialize a QuoteModel instance."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent quote as body and author."""
        print(f'"{self.body}" - {self.author}')
