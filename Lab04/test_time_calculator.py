from unittest import TestCase
from unittest.mock import patch
import io

from Lab04.time_calculator import time_calculator
from Lab04.time_calculator import days
from Lab04.time_calculator import subtract_days_from_seconds
from Lab04.time_calculator import hours
from Lab04.time_calculator import subtract_hours_from_seconds
from Lab04.time_calculator import minutes
from Lab04.time_calculator import subtract_minutes_from_seconds


class TestDays(TestCase):
    def test_days_zero(self):
        self.assertEqual(0, days(86399))

    def test_days_one(self):
        self.assertEqual(1, days(86400))

    def test_days_five(self):
        self.assertEqual(5, days(432000))

    def test_days_ten(self):
        self.assertEqual(10, days(864000))


class TestSubtract_days_from_seconds(TestCase):
    def test_subtract_days_from_seconds_zero(self):
        self.assertEqual(1, subtract_days_from_seconds(0, 1))

    def test_subtract_days_from_seconds_one(self):
        self.assertEqual(1, subtract_days_from_seconds(1, 86401))

    def test_subtract_days_from_seconds_five(self):
        self.assertEqual(1, subtract_days_from_seconds(5, 432001))

    def test_subtract_days_from_seconds_ten(self):
        self.assertEqual(1, subtract_days_from_seconds(10, 864001))


class TestHours(TestCase):
    def test_hours_zero(self):
        self.assertEqual(0, hours(3599))

    def test_hours_one(self):
        self.assertEqual(1, hours(3600))

    def test_hours_five(self):
        self.assertEqual(5, hours(18000))

    def test_hours_ten(self):
        self.assertEqual(10, hours(36000))


class TestSubtract_hours_from_seconds(TestCase):
    def test_subtract_hours_from_seconds_zero(self):
        self.assertEqual(1, subtract_hours_from_seconds(0, 1))

    def test_subtract_hours_from_seconds_one(self):
        self.assertEqual(1, subtract_hours_from_seconds(1, 3601))

    def test_subtract_hours_from_seconds_five(self):
        self.assertEqual(1, subtract_hours_from_seconds(5, 18001))

    def test_subtract_hours_from_seconds_ten(self):
        self.assertEqual(1, subtract_hours_from_seconds(10, 36001))


class TestMinutes(TestCase):
    def test_minutes_zero(self):
        self.assertEqual(0, minutes(59))

    def test_minutes_one(self):
        self.assertEqual(1, minutes(60))

    def test_minutes_five(self):
        self.assertEqual(5, minutes(300))

    def test_minutes_ten(self):
        self.assertEqual(10, minutes(600))


class TestSubtract_minutes_from_seconds(TestCase):
    def test_subtract_minutes_from_seconds_zero(self):
        self.assertEqual(1, subtract_minutes_from_seconds(0, 1))

    def test_subtract_minutes_from_seconds_one(self):
        self.assertEqual(1, subtract_minutes_from_seconds(1, 61))

    def test_subtract_minutes_from_seconds_five(self):
        self.assertEqual(1, subtract_minutes_from_seconds(5, 301))

    def test_subtract_minutes_from_seconds_ten(self):
        self.assertEqual(1, subtract_minutes_from_seconds(10, 601))


class TestTime_calculator(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_zero(self, mock_stdout):
        expected_output = "That is 0 days, 0 hours, 0 minutes, and 0 seconds.\n"
        time_calculator(0)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

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