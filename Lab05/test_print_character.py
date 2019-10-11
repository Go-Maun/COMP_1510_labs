from unittest import TestCase
from unittest.mock import patch
from unittest.mock import io
from Lab05.functions_lab05 import shop
from Lab05.functions_lab05 import print_character
from Lab05.functions_lab05 import print_items


class TestPrint_character(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_preferences(self, mock_stdout):
        expected_output = 'bananas? : yes\nsoft pears? : no\ncats and dogs? : cute\n'
        actual_value = print_character(["bananas?", "yes", "soft pears?", "no", "cats and dogs?", "cute"])
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_daily_check_list(self, mock_stdout):
        expected_output = 'Keys? : Yes\nPhone? : Yes\nSunglasses? : Yes\nWallet? : *GASP*\nI LEFT MY : WALLET AT HOME\n'
        actual_value = print_character(["Keys?", "Yes", "Phone?", "Yes", "Sunglasses?", "Yes", "Wallet?", "*GASP*",
                                        "I LEFT MY", "WALLET AT HOME"])
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_actual(self, mock_stdout):
        expected_output = 'Name : Ugad\nStrength : 14\nDexterity : 8\nConstitution : 8\nIntelligence : 15\n' \
                          'Wisdom : 9\nCharisma : 12\n'
        actual_value = print_character(['Name', 'Ugad', 'Strength', 14, 'Dexterity', 8, 'Constitution', 8,
                                        'Intelligence', 15, 'Wisdom', 9, 'Charisma', 12])
        self.assertEqual(expected_output, mock_stdout.getvalue())


class TestPrint_inventory(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory_basic(self, mock_stdout):
        expected_output = "tim's items: c, a, \n"
        actual_value = print_items(["name", "tim", ["c", "a"]], ["a", "b", "c", "d"], 2)
        self.assertEqual( expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory_daily_check_list(self, mock_stdout):
        expected_output = "Keegan's items: Keys, Phone, Sunglasses, \n"
        actual_value = print_items(["name", "Keegan", ["Keys", "Phone", "Sunglasses"]], ["Keys", "Phone", "Sunglasses",
                                                                                         "Wallet"], 3)
        self.assertEqual( expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory_actual(self, mock_stdout):
        expected_output = "Ugad's items: 2 Health Potion, Broad Sword, Broad Sword, Chain-mail Armour, Iron Dagger, \n"
        actual_value = print_items(['Name', 'Ugad', 'Strength', '14', 'Dexterity', '8', 'Constitution', '8',
                                    'Intelligence', '15', 'Wisdom', '9', 'Charisma', '12',
                                    ['2 Health Potion', 'Broad Sword', 'Broad Sword', 'Chain-mail Armour',
                                     'Iron Dagger']], shop(), 5)
        self.assertEqual( expected_output, mock_stdout.getvalue())
