import os
import logging
from utils import read_csv, write_csv

ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
DATA1_CSV = os.path.join(ROOT_DIR, "data/data_1.csv")
OUTPUT1_CSV = os.path.join(ROOT_DIR, "tmp/output_1.csv")
DATA2_CSV = os.path.join(ROOT_DIR, "data/data_2.csv")
OUTPUT2_CSV = os.path.join(ROOT_DIR, "tmp/output_2.csv")


def main():
    # Read & write first csv file
    try:
        data1 = read_csv(uri=DATA1_CSV, filter_key="state")
        write_csv(uri=OUTPUT1_CSV, data=data1)
    except Exception as e:
        logging.error(e)
    
    # Read & write second csv file
    try:
        data2 = read_csv(uri=DATA2_CSV, filter_key="site_number")
        write_csv(uri=OUTPUT2_CSV, data=data2)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()
