import csv
import subprocess
from abc import ABC, abstractmethod
from typing import List

from docx import Document

from QuoteEngine.quote_model import QuoteModel


class IngestorInterFace(ABC):
    """Abstract parent class for different file importers."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extension = path.split(".")[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        pass


class CSVImporter(IngestorInterFace):
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception("Cannot ingest.")

        with open(path, "r") as infile:
            whole_list = list(csv.reader(infile))
            whole_list.pop(0)
            list_of_quotes = []
            for quote in whole_list:
                list_of_quotes.append(QuoteModel(quote=quote[0], author=quote[-1]))
            return list_of_quotes


class DOCXImporter(IngestorInterFace):
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesDOCX.docx") -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception("Cannot ingest.")

        document = Document(path)
        return [
            QuoteModel.model_from_whole_quote(par.text)
            for par in document.paragraphs
            if par.text != ""
        ]


class TXTImporter(IngestorInterFace):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesTXT.txt") -> List[QuoteModel]:
        with open(path, "r") as infile:
            return [QuoteModel.model_from_whole_quote(row) for row in infile]


class PDFImporter(IngestorInterFace):
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesPDF.PDF") -> List[QuoteModel]:
        "convert to text via subprocess and parse it as txt"
        pass


class Ingestor(IngestorInterFace):
    IMPORTERS = [CSVImporter, DOCXImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        for importer in cls.IMPORTERS:
            if importer.can_ingest(path=path):
                return importer.parse(path=path)
