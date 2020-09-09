import csv
from exceptions import UriIsEmpty, DataIsEmpty

def read_csv(uri="", filter_key=""):
    """Read CSV file and preprocessing data

    Args:
        uri (str): the absolute path of csv file
        filter_key (str) : the column name of csv that will filter data.

    Raises:
        UriIsEmpty: The uri is empty

    Returns:
        data: The preprocessed data from csv file
    """
    if not uri:
        raise UriIsEmpty()
    else:
        with open(uri) as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader if not filter_key or (filter_key and row[filter_key])]

def write_csv(uri="", data=[]):
    """Write csv to file

    Args:
        uri (str): the absolute path of output file
        data (list): The list of dict to write to csv file

    Raises:
        UriIsEmpty: The uri is empty
        DataIsEmpty: The data is empty
    """
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