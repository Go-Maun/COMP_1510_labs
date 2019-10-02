from unittest import TestCase
from unittest.mock import patch
from Lab04.computing_club import print_number
from Lab04.computing_club import get_input
from Lab04.computing_club import number_generator
import io


class TestGet_input(TestCase):
    @patch('builtins.input', side_effect=[10])
    def test_get_input(self, mock_input):
        actual_value = get_input()
        expected_output = 10
        self.assertEqual(expected_output, actual_value)


class TestPrint_number(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_number(self, mock_stdout):
        expected_output = "10\n"
        print_number("10")
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestNumber_generator(TestCase):
    @patch('random.randint', return_value=50)
    def test_number_generator(self, mock_random):
        actual_value = number_generator()
        expected_value = 50
        self.assertEqual(expected_value, actual_value)