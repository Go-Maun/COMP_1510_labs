from unittest import TestCase
from unittest.mock import patch
from Lab05.functions_lab05 import generate_name
from Lab05.functions_lab05 import generate_vowel
from Lab05.functions_lab05 import generate_consonant
from Lab05.functions_lab05 import generate_syllable


class TestGenerate_name(TestCase):
    def test_generate_name_zero_syllables(self):
        self.assertEqual(generate_name(0), "Dummy")

    def test_generate_name_negative_syllables(self):
        self.assertEqual(generate_name(-11), "Dummy")

    @patch('random.randint', return_value=2)
    def test_generate_name_both_are_2(self, mock_value):
        actual_value = generate_name(1)
        expected_value = 'Ec'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=5)
    def test_generate_name_both_are_5(self, mock_value):
        actual_value = generate_name(1)
        expected_value = 'Ug'
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_syllable", return_value="ok")
    def test_generate_name_for_loop_ok(self, mock_value):
        expected_value = "Okokok"
        actual_value = generate_name(3)
        self.assertEqual(expected_value, actual_value)

    @patch("Lab05.functions_lab05.generate_syllable", return_value="bo")
    def test_generate_name_for_loop_bo(self, mock_value):
        expected_value = "Bobobobobobobo"
        actual_value = generate_name(7)
        self.assertEqual(expected_value, actual_value)


class TestGenerate_vowel(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_vowel_a(self, mock_value):
        actual_value = generate_vowel()
        expected_value = 'a'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=2)
    def test_generate_vowel_e(self, mock_value):
        actual_value = generate_vowel()
        expected_value = 'e'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=3)
    def test_generate_vowel_i(self, mock_value):
        actual_value = generate_vowel()
        expected_value = 'i'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=4)
    def test_generate_vowel_o(self, mock_value):
        actual_value = generate_vowel()
        expected_value = 'o'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=5)
    def test_generate_vowel_u(self, mock_value):
        actual_value = generate_vowel()
        expected_value = 'u'
        self.assertEqual(expected_value, actual_value)


class TestGenerate_consonant(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_consonant_b(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'b'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=3)
    def test_generate_consonant_d(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'd'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=5)
    def test_generate_consonant_g(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'g'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=7)
    def test_generate_consonant_j(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'j'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=9)
    def test_generate_consonant_l(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'l'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=11)
    def test_generate_consonant_n(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'n'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=13)
    def test_generate_consonant_q(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'q'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=15)
    def test_generate_consonant_s(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 's'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=17)
    def test_generate_consonant_v(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'v'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=19)
    def test_generate_consonant_x(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'x'
        self.assertEqual(expected_value, actual_value)

    @patch('random.randint', return_value=21)
    def test_generate_consonant_y(self, mock_value):
        actual_value = generate_consonant()
        expected_value = 'z'
        self.assertEqual(expected_value, actual_value)


class TestGenerate_syllable(TestCase):
    def test_generate_syllable_e_t(self):
        self.assertEqual('et', generate_syllable('e', 't'))

    def test_generate_syllable_a_q(self):
        self.assertEqual('aq', generate_syllable('a', 'q'))

    def test_generate_syllable_u_r(self):
        self.assertEqual('ur', generate_syllable('u', 'r'))

    def test_generate_syllable_a_c(self):
        self.assertEqual('ac', generate_syllable('a', 'c'))

    def test_generate_syllable_i_s(self):
        self.assertEqual('is', generate_syllable('i', 's'))
