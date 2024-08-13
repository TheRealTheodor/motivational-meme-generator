"""Python module with QuoteModel class."""


class QuoteModel:
    """A class that represents a quote and its author."""

    def __init__(self, quote: str, author: str) -> None:
        """
        Initialize a new instance of `QuoteModel`.

        :param quote: A string representing the quote.
        :param author: A string representing the author of the quote.
        """
        self.quote = quote
        self.author = author

    @classmethod
    def model_from_whole_quote(cls, whole_quote: str) -> "QuoteModel":
        """
        Create a `QuoteModel` instance from a whole quote string.

        :param whole_quote: A string in the format "quote - author".
        """
        q_and_auth = whole_quote.split("-")
        return QuoteModel(quote=q_and_auth[0].strip(), author=q_and_auth[-1].strip())

    @property
    def whole_quote(self) -> str:
        """Get the full quote string in the format "quote - author"."""
        return f"{self.quote} - {self.author}"

    def __repr__(self) -> str:
        """Return a string representation of the `QuoteModel` instance."""
        return self.whole_quote
