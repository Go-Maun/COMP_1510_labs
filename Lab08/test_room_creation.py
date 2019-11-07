from unittest import TestCase
from unittest.mock import patch
import io
from Lab08.maze import return_scenario
from Lab08.maze import print_room
from Lab08.maze import print_tile
from Lab08.maze import print_player


class TestReturn_scenario(TestCase):
    def test_return_scenario_square(self):
        expected_value = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2]}
        actual_value = return_scenario(3, 3)
        self.assertEqual(expected_value, actual_value)

    def test_return_scenario_more_long_than_wide(self):
        expected_value = {0: [0, 1], 1: [0, 1], 2: [0, 1], 3: [0, 1]}
        actual_value = return_scenario(2, 4)
        self.assertEqual(expected_value, actual_value)

    def test_return_scenario_more_wide_than_long(self):
        expected_value = {0: [0, 1, 2, 3], 1: [0, 1, 2, 3]}
        actual_value = return_scenario(4, 2)
        self.assertEqual(expected_value, actual_value)

    def test_return_scenario_0(self):
        expected_value = {}
        actual_value = return_scenario(0, 0)
        self.assertEqual(expected_value, actual_value)


class TestPrint_room(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_room_square(self, mock_print):
        expected_value = "You're currently at [0, 0]\n◘ X X X X\nX X X X X\nX X X X X\nX X X X X\nX X X X X\n"
        print_room(5,
                   {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]},
                   {"position": [0, 0]})
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_room_wider_than_long(self, mock_print):
        expected_value = "You're currently at [0, 0]\n◘ X X X X\nX X X X X\nX X X X X\n"
        print_room(5,
                   {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4]},
                   {"position": [0, 0]})
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_room_longer_than_wide(self, mock_print):
        expected_value = "You're currently at [0, 0]\n◘ X X\nX X X\nX X X\nX X X\nX X X\n"
        print_room(3,
                   {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]},
                   {"position": [0, 0]})
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_tile(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_tile_new_line(self, mock_print):
        expected_value = "X\n"
        print_tile([2, 3], 3, 3)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_tile_same_line(self, mock_print):
        expected_value = "X "
        print_tile([2, 2], 3, 3)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_player(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_player_new_line(self, mock_print):
        expected_value = "◘\n"
        print_player([2, 3], 3, 3)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_player_same_line(self, mock_print):
        expected_value = "◘ "
        print_player([2, 2], 3, 3)
        self.assertEqual(expected_value, mock_print.getvalue())

