import os
from utils import read_csv, write_csv

ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
CSV_FILE = os.path.join(DATA_DIR, 'data.csv')
TMP_DIR = os.path.join(ROOT_DIR, 'tmp')
OUTPUT_FILE = os.path.join(TMP_DIR, 'output.csv')

def main():
    data = read_csv(CSV_FILE)
    write_csv(OUTPUT_FILE, data)

if __name__ == "__main__":
    main()