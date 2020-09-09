import requests
import logging
from utils import get_latest_exchange, get_history_exchange

def main():
    try:
        latest_exchange = get_latest_exchange()
        history_exchange = get_history_exchange("2020-03-01", "2020-03-10", ["USD", "JPY"])
        usd_rates = list(map(lambda x: x['USD'], history_exchange["rates"].values()))
        max_usd = max(usd_rates)
        min_usd = min(usd_rates)
        avg_usd = sum(usd_rates) / len(usd_rates)
        print(f"Max USD rate: {max_usd}")
        print(f"Min USD rate: {min_usd}")
        print(f"Average USD rate: {avg_usd}")
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()
