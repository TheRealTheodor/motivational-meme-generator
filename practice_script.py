from QuoteEngine.ingestors import CSVImporter, DOCXImporter, TXTImporter

listik = TXTImporter.parse()

for el in listik:
    print(el)
