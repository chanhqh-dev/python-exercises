class RequestFail(Exception):
    """ The request is fail """
    def __str__(self):
        return "The request is fail"

class EndDateBeforeStartDate(Exception):
    """ The end date is before start date """
    def __str__(self):
        return "The end date is before start date"

class SymbolsIsEmpty(Exception):
    """ The symbol is empty """
    def __str__(self):
        return "The symbol is empty"

class StartDateIsEmpty(Exception):
    """ The start date is empty """
    def __str__(self):
        return "The start date is empty"

class EndDateIsEmpty(Exception):
    """ The end date is empty """
    def __str__(self):
        return "The end date is empty"