import unittest
from unittest.mock import patch, Mock
from requests import Response

from utils import get_latest_exchange
from exceptions import RequestFail

class TestUtils(unittest.TestCase):
    def test_get_latest_exchange(self):
        expected_data = {"rates": {"USD": 1}}
        mock_res = Response()
        mock_res.status_code = 200
        mock_res.json = lambda : expected_data
        mock_get = Mock(return_value=mock_res)
        with patch('requests.get', mock_get):
            res = get_latest_exchange()
            self.assertEqual(res, expected_data)

    def test_get_latest_exchange_failure(self):
        mock_res = Response()
        mock_res.status_code = 500
        mock_get = Mock(return_value=mock_res)
        with patch('requests.get', mock_get):
            try:
                get_latest_exchange()
            except:
                self.assertRaises(RequestFail)
