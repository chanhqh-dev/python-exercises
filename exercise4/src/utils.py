import requests
from datetime import datetime
from exceptions import RequestFail, EndDateBeforeStartDate, SymbolsIsEmpty, StartDateIsEmpty, EndDateIsEmpty

LATEST_EXCHANGE_API = "https://api.exchangeratesapi.io/latest?base=USD"
HISTORY_EXCHANGE_API = "https://api.exchangeratesapi.io/history"

def get_latest_exchange():
    """Get the latest exchange rate

    Raises:
        RequestFail: The request to API endpoint return error
    
    Returns:
        exchange_rates: The latest rate in json format
    """
    res = requests.get(LATEST_EXCHANGE_API)
    if(res.status_code == 200):
        return res.json()
    else:
        raise RequestFail()

def get_history_exchange(start_date, end_date, symbols=[]):
    """Get historical exchange rate

    Args:
        start_date (str) : The start date of historical data. Format YYYY/MM/DD.
        end_date (str) : The end date of historical data. Format YYYY/MM/DD.
        symbols (list) : The list of symbols to query

    Raises:
        StartDateIsEmpty: The start_date is empty
        EndDateIsEmpty: the end_date is empty
        EndDateBeforeStartDate: The end date is before the start date
        SymbolsIsEmpty: The symbols is empty

    Returns:
        history_rates: The historical exchange rate data
    """
    if not symbols:
        raise SymbolsIsEmpty()

    if not start_date:
        raise StartDateIsEmpty()

    if not end_date:
        raise EndDateIsEmpty()

    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    if end_date_obj < start_date_obj:
        raise EndDateBeforeStartDate()
    
    res = requests.get(f"{HISTORY_EXCHANGE_API}?start_at={start_date}&end_at={end_date}&symbols={','.join(symbols)}")
    if(res.status_code == 200):
        return res.json()
    else:
        raise RequestFail()
