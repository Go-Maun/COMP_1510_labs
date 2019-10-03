from unittest import TestCase

from Lab04.roman_numbers import convert_to_roman_numeral
from Lab04.roman_numbers import thousands
from Lab04.roman_numbers import hundreds
from Lab04.roman_numbers import tens
from Lab04.roman_numbers import ones


class TestThousands(TestCase):
    def test_thousands_one(self):
        self.assertEqual("M", thousands(1000, ""))

    def test_thousands_five(self):
        self.assertEqual("MMMMM", thousands(5000, ""))

    def test_thousands_nine(self):
        self.assertEqual("MMMMMMMMM", thousands(9000, ""))


class TestHundreds(TestCase):
    def test_hundreds_one(self):
        self.assertEqual("C", hundreds(100, ""))

    def test_hundreds_four(self):
        self.assertEqual("CD", hundreds(400, ""))

    def test_hundreds_five(self):
        self.assertEqual("D", hundreds(500, ""))

    def test_hundreds_six(self):
        self.assertEqual("DC", hundreds(600, ""))

    def test_hundreds_nine(self):
        self.assertEqual("CM", hundreds(900, ""))


class TestTens(TestCase):
    def test_tens_one(self):
        self.assertEqual("X", tens(10, ""))

    def test_tens_four(self):
        self.assertEqual("XL", tens(40, ""))

    def test_tens_five(self):
        self.assertEqual("L", tens(50, ""))

    def test_tens_six(self):
        self.assertEqual("LX", tens(60, ""))

    def test_tens_nine(self):
        self.assertEqual("XC", tens(90, ""))


class TestOnes(TestCase):
    def test_ones_one(self):
        self.assertEqual("I", ones(1, ""))

    def test_ones_four(self):
        self.assertEqual("IV", ones(4, ""))

    def test_ones_five(self):
        self.assertEqual("V", ones(5, ""))

    def test_ones_six(self):
        self.assertEqual("VI", ones(6, ""))

    def test_ones_nine(self):
        self.assertEqual("IX", ones(9, ""))


class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral_one(self):
        self.assertEqual("I", convert_to_roman_numeral(1))

    def test_convert_to_roman_numeral_four(self):
        self.assertEqual("IV", convert_to_roman_numeral(4))

    def test_convert_to_roman_numeral_five(self):
        self.assertEqual("V", convert_to_roman_numeral(5))

    def test_convert_to_roman_numeral_six(self):
        self.assertEqual("VI", convert_to_roman_numeral(6))

    def test_convert_to_roman_numeral_nine(self):
        self.assertEqual("IX", convert_to_roman_numeral(9))

    def test_convert_to_roman_numeral_ten(self):
        self.assertEqual("X", convert_to_roman_numeral(10))

    def test_convert_to_roman_numeral_twenty(self):
        self.assertEqual("XX", convert_to_roman_numeral(20))

    def test_convert_to_roman_numeral_forty(self):
        self.assertEqual("XL", convert_to_roman_numeral(40))

    def test_convert_to_roman_numeral_fifty(self):
        self.assertEqual("L", convert_to_roman_numeral(50))

    def test_convert_to_roman_numeral_sixty(self):
        self.assertEqual("LX", convert_to_roman_numeral(60))

    def test_convert_to_roman_numeral_ninety(self):
        self.assertEqual("XC", convert_to_roman_numeral(90))

    def test_convert_to_roman_numeral_one_hundred(self):
        self.assertEqual("C", convert_to_roman_numeral(100))

    def test_convert_to_roman_numeral_four_hundred(self):
        self.assertEqual("CD", convert_to_roman_numeral(400))

    def test_convert_to_roman_numeral_five_hundred(self):
        self.assertEqual("D", convert_to_roman_numeral(500))

    def test_convert_to_roman_numeral_nine_hundred(self):
        self.assertEqual("CM", convert_to_roman_numeral(900))

    def test_convert_to_roman_numeral_one_thousand(self):
        self.assertEqual("M", convert_to_roman_numeral(1000))

    def test_convert_to_roman_numeral_two_thousand(self):
        self.assertEqual("MM", convert_to_roman_numeral(2000))

    def test_convert_to_roman_numeral_five_thousand(self):
        self.assertEqual("MMMMM", convert_to_roman_numeral(5000))

    def test_convert_to_roman_numeral_nine_thousand(self):
        self.assertEqual("MMMMMMMMM", convert_to_roman_numeral(9000))

    def test_convert_to_roman_numeral_ten_thousand(self):
        self.assertEqual("MMMMMMMMMM", convert_to_roman_numeral(10000))
