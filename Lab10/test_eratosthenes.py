from unittest import TestCase
from A01172483_1510_labs.Lab10.question_1 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes_no_prime_numbers(self):
        expected_value = []
        actual_value = eratosthenes(0)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_one_prime_number(self):
        expected_value = [2]
        actual_value = eratosthenes(3)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_two_prime_numbers(self):
        expected_value = [2, 3]
        actual_value = eratosthenes(4)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_three_prime_numbers(self):
        expected_value = [2, 3, 5]
        actual_value = eratosthenes(6)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_four_prime_numbers(self):
        expected_value = [2, 3, 5, 7]
        actual_value = eratosthenes(8)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_five_prime_numbers(self):
        expected_value = [2, 3, 5, 7, 11]
        actual_value = eratosthenes(12)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_six_prime_numbers(self):
        expected_value = [2, 3, 5, 7, 11, 13]
        actual_value = eratosthenes(14)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_seven_prime_numbers(self):
        expected_value = [2, 3, 5, 7, 11, 13, 17]
        actual_value = eratosthenes(18)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_eight_prime_numbers(self):
        expected_value = [2, 3, 5, 7, 11, 13, 17, 19]
        actual_value = eratosthenes(20)
        self.assertEqual(expected_value, actual_value)

    def test_eratosthenes_nine_prime_numbers(self):
        expected_value = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        actual_value = eratosthenes(24)
        self.assertEqual(expected_value, actual_value)
