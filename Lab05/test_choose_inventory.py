from unittest import TestCase
from unittest.mock import patch
import io
from Lab05.functions_lab05 import choose_inventory
from Lab05.functions_lab05 import choose_inventory_messages
from Lab05.functions_lab05 import shop


class TestChoose_inventory(TestCase):
    def test_choose_inventory_entire_stock_min(self):
        self.assertEqual(choose_inventory(shop(), 12), ['100 Ball Barrings',
                                                        '2 Health Potion',
                                                        '50ft of Rope',
                                                        "An Adventurer's Kit",
                                                        'Broad Sword',
                                                        'Chain-mail Armour',
                                                        'Cloth Robes',
                                                        'Iron Dagger',
                                                        'Leather Armour',
                                                        'One Week of Provisions',
                                                        'Shield',
                                                        'War Axe'])

    def test_choose_inventory_entire_stock_large(self):
        self.assertEqual(choose_inventory(shop(), 100), ['100 Ball Barrings',
                                                         '2 Health Potion',
                                                         '50ft of Rope',
                                                         "An Adventurer's Kit",
                                                         'Broad Sword',
                                                         'Chain-mail Armour',
                                                         'Cloth Robes',
                                                         'Iron Dagger',
                                                         'Leather Armour',
                                                         'One Week of Provisions',
                                                         'Shield',
                                                         'War Axe'])

    def test_choose_inventory_negative_input(self):
        self.assertEqual(choose_inventory(shop(), -12), [])

    def test_choose_inventory_zero_input(self):
        self.assertEqual(choose_inventory(shop(), 0), [])

    @patch("random.randint", return_value=0)
    def test_choose_inventory_one_input(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 1), ['Broad Sword'])

    @patch("random.randint", return_value=2)
    def test_choose_inventory_dual_wield_axes(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 2), ['War Axe', 'War Axe'])

    @patch("random.randint", return_value=1)
    def test_choose_inventory_dagger_dagger_dagger(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 3), ['Iron Dagger', 'Iron Dagger', 'Iron Dagger'])

    @patch("random.randint", return_value=8)
    def test_choose_inventory_worried_wizard(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 5), ['2 Health Potion', '2 Health Potion', '2 Health Potion',
                                                       '2 Health Potion', '2 Health Potion'])

    @patch("random.randint", return_value=7)
    def test_choose_inventory_the_floor_is_ball_barrings(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 5), ['100 Ball Barrings', '100 Ball Barrings', '100 Ball Barrings',
                                                       '100 Ball Barrings', '100 Ball Barrings'])

    @patch("random.randint", return_value=4)
    def test_choose_inventory_armoured_up(self, mock_random):
        self.assertEqual(choose_inventory(shop(), 2), ['Chain-mail Armour', 'Chain-mail Armour'])


class TestChoose_inventory_messages(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_message_satisfaction(self, mock_stdout):
        expected_output = "\nYou are satisfied with your purchase.\n['crunchy pears']\n"
        choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], ["crunchy pears"], 1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_message_entire_stock(self, mock_stdout):
        expected_output = "\nYou walk out of the store with a smug look as you purchased everything Orvish had.\n" \
                          "['crunchy pears']\n"
        choose_inventory_messages(["crunchy pears"], ["crunchy pears"], 1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_message_walk_away(self, mock_stdout):
        expected_output = "\nYou walk back out, confident that your abilities will carry you on your adventure.\n[]\n"
        choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], [], 0)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_message_request_negative(self, mock_stdout):
        expected_output = '\n"I uh... I dont think I can muster a negative amount of my wares." ' \
                          'replied a confused Orvish\n "Get out you creep!"\n[]\n'
        choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], [], -2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
