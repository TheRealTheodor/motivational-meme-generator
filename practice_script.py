from QuoteEngine.ingestors import CSVImporter, DOCXImporter, PDFImporter, TXTImporter

listik = PDFImporter.parse()

for el in listik:
    print(el)
