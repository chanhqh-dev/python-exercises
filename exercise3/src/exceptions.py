class UriIsEmpty(Exception):
    """ Uri is Empty """
    def __str__(self):
        return "The URI is empty"

class DataIsEmpty(Exception):
    """ Data is empty """
    def __str__(self):
        return "Data is empty"
