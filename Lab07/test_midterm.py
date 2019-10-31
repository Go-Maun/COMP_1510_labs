from unittest import TestCase
from Lab07.midterm import list_tagger
from Lab07.midterm import cutoff
from Lab07.midterm import prepender


class TestList_tagger(TestCase):
    def test_list_tagger_empty_list(self):
        expected_value = [0]
        actual_value = list_tagger([])
        self.assertEqual(expected_value, actual_value)

    def test_list_tagger_length_one(self):
        expected_value = [1, "Python"]
        actual_value = list_tagger(["Python"])
        self.assertEqual(expected_value, actual_value)

    def test_list_tagger_full_list(self):
        expected_value = [4, 'cat', 'dog', 'mouse', 'rabbit']
        actual_value = list_tagger(['cat', 'dog', 'mouse', 'rabbit'])
        self.assertEqual(expected_value, actual_value)


class TestCutoff(TestCase):
    def test_cutoff_empty_divisible_0(self):
        expected_value = 0
        actual_value = cutoff([], 0)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_empty_divisible_5(self):
        expected_value = 0
        actual_value = cutoff([], 5)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_zero_div(self):
        self.assertRaises(ZeroDivisionError, cutoff, [0], 0)

    def test_cutoff_count_one_from_zero(self):
        expected_value = 1
        actual_value = cutoff([0], 5)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_count_one_from_2(self):
        expected_value = 1
        actual_value = cutoff([2], 2)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_zero_result(self):
        expected_value = 0
        actual_value = cutoff([2], 4)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_zero_division_full_list(self):
        self.assertRaises(ZeroDivisionError, cutoff, [1, 2, 3, 4, 5], 0)

    def test_cutoff_full_list_2_divisible(self):
        expected_value = 2
        actual_value = cutoff([1, 2, 3, 4, 5], 2)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_identical_list_and_dividend(self):
        expected_value = 5
        actual_value = cutoff([2, 2, 2, 2, 2], 2)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_identical_list_cant_divide(self):
        expected_value = 0
        actual_value = cutoff([2, 2, 2, 2, 2], 10)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_different_list_all_divide(self):
        expected_value = 5
        actual_value = cutoff([3, 6, 9, 12, 15], 3)
        self.assertEqual(expected_value, actual_value)

    def test_cutoff_negative_divisor(self):
        expected_value = 2
        actual_value = cutoff([1, 2, 3, 4, 5], -2)
        self.assertEqual(expected_value, actual_value)


class TestPerpender(TestCase):
    def test_perpender_none(self):
        test_list = []
        test_prefix = ""
        expected_value = []
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_empty_with_prefix(self):
        test_list = []
        test_prefix = "Python"
        expected_value = []
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_python(self):
        test_list = ["Python"]
        test_prefix = ""
        expected_value = ["Python"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_Pythonic_love(self):
        test_list = ["Python"]
        test_prefix = "I Love "
        expected_value = ["I Love Python"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_list_with_no_prefix(self):
        test_list = ["Python", "is", "better", "than", "JavaScript"]
        test_prefix = ""
        expected_value = ["Python", "is", "better", "than", "JavaScript"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_umm(self):
        test_list = ["Python", "is", "better", "than", "JavaScript"]
        test_prefix = "Umm... "
        expected_value = ['Umm... Python', 'Umm... is', 'Umm... better', 'Umm... than', 'Umm... JavaScript']
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)

    def test_perpender_numbers(self):
        test_list = [1, 2, 3, 4, 5]
        test_prefix = 7
        expected_value = [8, 9, 10, 11, 12]
        prepender(test_list, test_prefix)
        self.assertEqual(expected_value, test_list)
