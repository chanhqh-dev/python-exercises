import csv
from exceptions import UriIsEmpty, DataIsEmpty


class CsvHelper:
    def read_csv(self, uri="", filter_key=""):
        if not uri:
            raise UriIsEmpty()
        else:
            with open(uri) as csvfile:
                reader = csv.DictReader(csvfile)
                return [row for row in reader if not filter_key or (filter_key and row[filter_key])]

    def write_csv(self, uri="", data=[]):
        if not uri:
            raise UriIsEmpty()
        if not data:
            raise DataIsEmpty()
        else:
            with open(uri, 'w', newline='') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
