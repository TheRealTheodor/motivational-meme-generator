class QuoteModel:
    def __init__(self, quote: str, author: str) -> None:
        self.quote = quote
        self.author = author

    @property
    def whole_quote(self) -> str:
        return f"{self.quote} - {self.author}"

    def __repr__(self) -> str:
        return self.whole_quote
