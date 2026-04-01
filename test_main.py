import unittest
from unittest.mock import patch
from main import calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    def test_get_numbers_from_user_retry_then_success(self):
        with patch("builtins.input", side_effect=["1 -2 3", "4 5 6"]):
            with patch("builtins.print") as mock_print:
                result = get_numbers_from_user()

        self.assertEqual(result, [4, 5, 6])
        mock_print.assert_called_once_with(
            "Lỗi: Tất cả các số phải là số nguyên dương.. Vui lòng nhập lại."
        )

if __name__ == '__main__':
    unittest.main()
