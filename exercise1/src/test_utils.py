import csv
import unittest
from unittest.mock import mock_open, patch

from utils import read_csv, write_csv
from exceptions import UriIsEmpty, DataIsEmpty

class TestUtils(unittest.TestCase):
    def test_read_csv(self):
        data = "first_name,last_name,license_number,state\n" \
            "Chris,Smith,w34r90f,pennsylvania"
        expected_data = [{"first_name": "Chris", "last_name": "Smith", "license_number": "w34r90f", "state": "pennsylvania"}]
        m = mock_open(read_data=data)
        with patch("builtins.open", m):
            output_data = read_csv(uri="data/data_1.csv")
            self.assertEqual(output_data, expected_data)
    
    def test_read_csv_exception(self):
        try:
            read_csv(uri="")
        except:
            self.assertRaises(UriIsEmpty)

    def test_write_csv(self):
        data = [{"first_name": "Chris", "last_name": "Smith", "license_number": "w34r90f", "state": "pennsylvania"}]
        m = mock_open()
        with patch("builtins.open", m):
            write_csv(uri="tmp/output_1.csv", data=data)
            m.assert_called_once_with("tmp/output_1.csv", "w", newline="")

    def test_write_csv_exception(self):
        try:
            write_csv(uri="")
        except:
            self.assertRaises(UriIsEmpty)

        try:
            write_csv(uri="tmp/output_1.csv")
        except:
            self.assertRaises(DataIsEmpty)


if __name__ == "__main__":
    unittest.main()
