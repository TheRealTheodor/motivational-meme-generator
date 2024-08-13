from QuoteEngine.ingestors import CSVImporter

listik = CSVImporter.parse()
for q in listik:
    print(q)
