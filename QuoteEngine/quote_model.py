"""Python module with QuoteModel class."""


class QuoteModel:
    """A class that represents a quote and its author."""

    def __init__(self, body: str, author: str) -> None:
        """
        Initialize a new instance of `QuoteModel`.

        :param body: A string representing the body of quote.
        :param author: A string representing the author of the quote.
        """
        self.body = body
        self.author = author

    @classmethod
    def model_from_whole_quote(cls, whole_quote: str) -> "QuoteModel":
        """
        Create a `QuoteModel` instance from a whole quote string.

        :param whole_quote: A string in the format "quote - author".
        """
        q_and_auth = whole_quote.split("-")
        return QuoteModel(body=q_and_auth[0].strip(), author=q_and_auth[-1].strip())

    @property
    def whole_quote(self) -> str:
        """Get the full quote string in the format "body - author"."""
        return f"{self.body} - {self.author}"

    def __repr__(self) -> str:
        """Return a string representation of the `QuoteModel` instance."""
        return self.whole_quote
