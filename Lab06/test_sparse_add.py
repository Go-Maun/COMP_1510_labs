from unittest import TestCase
from Lab06.sparse_vector import sparse_add


class TestSparse_add(TestCase):
    def test_sparse_add_empty(self):
        dict_1 = {}
        dict_2 = {}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_dict_1_empty(self):
        dict_1 = {}
        dict_2 = {2: 1, 5: 8, 9: 1}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {2: 1, 5: 8, 9: 1}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_dict_2_empty(self):
        dict_1 = {1: 4, 5: 6, 8: 9}
        dict_2 = {}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {1: 4, 5: 6, 8: 9}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_same_indices(self):
        dict_1 = {1: 2, 4: 7, 10: 5}
        dict_2 = {1: 4, 4: 5, 10: 2}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {1: 6, 4: 12, 10: 7}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_some_indices(self):
        dict_1 = {1: 2, 8: 7, 11: 5}
        dict_2 = {1: 4, 4: 5, 10: 2}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {1: 6, 4: 5, 8: 7, 10: 2, 11: 5}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_different_indices(self):
        dict_1 = {1: 2, 3: 1, 5: 8}
        dict_2 = {2: 3, 4: 5, 6: 1}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {1: 2, 2: 3, 3: 1, 4: 5, 5: 8, 6: 1}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_a_value_becomes_zero(self):
        dict_1 = {1: 5, 6: 8}
        dict_2 = {2: 4, 6: -8, 10: 2}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {1: 5, 2: 4, 10: 2}
        self.assertEqual(expected_value, actual_value)

    def test_sparse_add_dictionary_becomes_empty(self):
        dict_1 = {1: 5, 6: 8, 10: -2}
        dict_2 = {1: -5, 6: -8, 10: 2}
        actual_value = sparse_add(dict_1, dict_2)
        expected_value = {}
        self.assertEqual(expected_value, actual_value)