from unittest import TestCase
from unittest.mock import patch
from Lab05.functions_lab05 import create_character
from Lab05.functions_lab05 import generate_attribute
from Lab05.functions_lab05 import add_items_to_character
from Lab05.functions_lab05 import create_list


class TestCreate_character(TestCase):
    @patch("Lab05.functions_lab05.generate_name", return_value="Jerry the Barbarian")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Strength", 17])
    def test_create_character_barbarian(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Jerry the Barbarian', 'Strength', 17]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_name", return_value="Tommy the Assassin")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Dexterity", 16])
    def test_create_character_rogue(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Tommy the Assassin', 'Dexterity', 16]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_name", return_value="Timmy the Dumb")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Intelligence", 5])
    def test_create_character_dumb_timmy(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Timmy the Dumb', 'Intelligence', 5]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_name", return_value="Chris; God of Creation")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Wisdom", 40])
    def test_create_character_god(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Chris; God of Creation', 'Wisdom', 40]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_name", return_value="Jonathan the Hearty")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Constitution", 12])
    def test_create_character(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Jonathan the Hearty', 'Constitution', 12]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_name", return_value="Robert the Charming")
    @patch("Lab05.functions_lab05.generate_attribute", return_value=["Charisma", 14])
    def test_create_character_robert(self, mock_name, mock_attribute):
        expected_value = ['Name', 'Robert the Charming', 'Charisma', 14]
        actual_value = create_character(3)
        self.assertEqual(expected_value, actual_value)


class TestGenerate_attribute(TestCase):
    @patch("Lab05.functions_lab05.roll_die", return_value="15")
    def test_generate_attribute_strength(self, mock_roll):
        expected_value = ['Strength', '15']
        actual_value = generate_attribute("Strength", 3, 6)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.roll_die", return_value="7")
    def test_generate_attribute_dexterity(self, mock_roll):
        expected_value = ['Dexterity', '7']
        actual_value = generate_attribute("Dexterity", 3, 6)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.roll_die", return_value="3")
    def test_generate_attribute_constitution(self, mock_roll):
        expected_value = ['Constitution', '3']
        actual_value = generate_attribute("Constitution", 3, 6)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.roll_die", return_value="10")
    def test_generate_attribute_intelligence(self, mock_roll):
        expected_value = ['Intelligence', '10']
        actual_value = generate_attribute("Intelligence", 3, 6)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.roll_die", return_value="7")
    def test_generate_attribute_wisdom(self, mock_roll):
        expected_value = ['Wisdom', '7']
        actual_value = generate_attribute("Wisdom", 3, 6)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.roll_die", return_value="18")
    def test_generate_attribute_charisma(self, mock_roll):
        expected_value = ['Charisma', '18']
        actual_value = generate_attribute("Charisma", 3, 6)
        self.assertEqual(expected_value, actual_value)


class TestAdd_items_to_character(TestCase):
    def test_add_items_to_character_gnoll_ears(self):
        expected_value = ['sword', 'shield', ['57 gnoll ears']]
        actual_value = add_items_to_character(["sword", "shield"], ["57 gnoll ears"])
        self.assertEqual(expected_value, actual_value)

    def test_add_items_to_character_fish(self):
        expected_value = ['1 fish', '2 fish', ['red fish', 'blue fish']]
        actual_value = add_items_to_character(["1 fish", "2 fish"], ["red fish", "blue fish"])
        self.assertEqual(expected_value, actual_value)

    def test_add_items_to_character_realistic(self):
        expected_value = ['Name', 'Ugad', 'Strength', '14', 'Dexterity', '8', 'Constitution', '8', 'Intelligence', '15',
                          'Wisdom', '9', 'Charisma', '12', ['2 Health Potion', 'Broad Sword', 'Broad Sword',
                                                            'Chain-mail Armour', 'Iron Dagger']]
        actual_value = add_items_to_character(['Name', 'Ugad', 'Strength', '14', 'Dexterity', '8', 'Constitution', '8',
                                               'Intelligence', '15', 'Wisdom', '9', 'Charisma', '12'],
                                              ['2 Health Potion', 'Broad Sword', 'Broad Sword', 'Chain-mail Armour',
                                               'Iron Dagger'])
        self.assertEqual(expected_value, actual_value)


class TestCreate_list(TestCase):
    def test_create_list_numbers(self):
        expected_value = [1, 2, 3, 4, 5, 6, 7]
        actual_value = create_list([1], [2], [3], [4], [5], [6], [7])
        self.assertEqual(expected_value, actual_value)

    def test_create_list_numbers_and_letters(self):
        expected_value = ['A', 1, 'B', 2, 'C', 3, 'D', 4, 'E', 5, 'F', 6, 'G', 7]
        actual_value = create_list(["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6], ["G", 7])
        self.assertEqual(expected_value, actual_value)

    def test_create_list_stats(self):
        expected_value = ['Name', 'Ugad', 'Strength', 14, 'Dexterity', 8, 'Constitution', 8,
                          'Intelligence', 15, 'Wisdom', 9, 'Charisma', 12]
        actual_value = create_list(['Name', 'Ugad'], ['Strength', 14], ['Dexterity', 8], ['Constitution', 8],
                                   ['Intelligence', 15], ['Wisdom', 9], ['Charisma', 12])
        self.assertEqual(expected_value, actual_value)
