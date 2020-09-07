import csv
import unittest
from unittest.mock import mock_open, patch

from csvhelper import CsvHelper
from exceptions import UriIsEmpty, DataIsEmpty

class TestCsvHelper(unittest.TestCase):
    def test_read_csv(self):
        csv_helper = CsvHelper()
        try:
            csv_helper.read_csv(uri="")
        except:
            self.assertRaises(UriIsEmpty)

        data = "first_name,last_name,license_number,state\n" \
            "Chris,Smith,w34r90f,pennsylvania"
        expected_data = [{"first_name": "Chris", "last_name": "Smith", "license_number": "w34r90f", "state": "pennsylvania"}]
        m = mock_open(read_data=data)
        with patch("builtins.open", m):
            output_data = csv_helper.read_csv(uri="data/data_1.csv")
            self.assertEqual(output_data, expected_data)

    def test_write_csv(self):
        csv_helper = CsvHelper()
        try:
            csv_helper.write_csv(uri="")
        except:
            self.assertRaises(UriIsEmpty)

        try:
            csv_helper.write_csv(uri="tmp/output_1.csv")
        except:
            self.assertRaises(DataIsEmpty)

        data = [{"first_name": "Chris", "last_name": "Smith", "license_number": "w34r90f", "state": "pennsylvania"}]
        m = mock_open()
        with patch("builtins.open", m):
            csv_helper.write_csv(uri="tmp/output_1.csv", data=data)
            m.assert_called_once_with("tmp/output_1.csv", "w", newline="")


if __name__ == "__main__":
    unittest.main()
