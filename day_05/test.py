import unittest

from day_05.solution import find_seat_row, find_seat_column


class MyTestCase(unittest.TestCase):
    def test_find_seat_row_returns_seat_row(self):
        # Given
        seat = 'BFFFBBFRRR'

        # When Then
        self.assertEqual(find_seat_row(seat), 70)

    def test_find_seat_columns_returns_seat_column(self):
        # Given
        seat = 'BFFFBBFRRR'

        # When Then
        self.assertEqual(find_seat_column(seat), 7)


if __name__ == '__main__':
    unittest.main()
