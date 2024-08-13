class QuoteModel:
    def __init__(self, quote: str, author: str) -> None:
        self.quote = quote
        self.author = author

    @classmethod
    def model_from_whole_quote(cls, whole_quote: str) -> "QuoteModel":
        q_and_auth = whole_quote.split("-")
        return QuoteModel(quote=q_and_auth[0].strip(), author=q_and_auth[-1].strip())

    @property
    def whole_quote(self) -> str:
        return f"{self.quote} - {self.author}"

    def __repr__(self) -> str:
        return self.whole_quote
