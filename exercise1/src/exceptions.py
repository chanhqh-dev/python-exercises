class UriIsEmpty(Exception):
    """The Uri should not be empty"""
    def __str__(self):
        return "The Uri should not be empty"

class DataIsEmpty(Exception):
    """The data should not be empty"""
    def __str__(self):
        return "The data should not be empty"
