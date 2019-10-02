from unittest import TestCase
from unittest.mock import patch
import io

from Lab04.time_calculator import time_calculator


class TestTime_calculator(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_one_second(self, mock_stdout):
        expected_output = "That is 0 days, 0 hours, 0 minutes, and 1 seconds.\n"
        time_calculator(1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_one_minute(self, mock_stdout):
        expected_output = "That is 0 days, 0 hours, 1 minutes, and 0 seconds.\n"
        time_calculator(60)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_one_hour(self, mock_stdout):
        expected_output = "That is 0 days, 1 hours, 0 minutes, and 0 seconds.\n"
        time_calculator(3600)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_one_day(self, mock_stdout):
        expected_output = "That is 1 days, 0 hours, 0 minutes, and 0 seconds.\n"
        time_calculator(86400)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_all_one(self, mock_stdout):
        expected_output = "That is 1 days, 1 hours, 1 minutes, and 1 seconds.\n"
        time_calculator(90061)
        self.assertEqual(mock_stdout.getvalue(), expected_output)