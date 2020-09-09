import pandas as pd

from exceptions import UriIsEmpty, DataIsEmpty

def read_csv(uri):
    if not uri:
        raise UriIsEmpty()

    data = pd.read_csv(uri)
    data.drop_duplicates()
    data["attendee_name"] = data["attendee_name"].apply(lambda x: x.title())
    return data

def write_csv(uri, data):
    if not uri:
        raise UriIsEmpty()

    if data.empty:
        raise DataIsEmpty()

    data.to_csv(uri, index=False)
