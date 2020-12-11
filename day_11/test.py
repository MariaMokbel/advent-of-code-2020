import unittest

from day_11.solution import parse_input, find_left_seat, find_right_seat, find_bottom_left_seat, find_bottom_right_seat, \
    find_up_right_seat, find_up_left_seat, find_up_seat, find_bottom_seat


class MyTestCase(unittest.TestCase):
    def test_find_left_right_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 0
        given_column = 3

        # When
        left_seat = find_left_seat(content, given_row, given_column)
        right_seat = find_right_seat(content, given_row, given_column)

        # Then
        self.assertEqual(left_seat, (0, 2))
        self.assertEqual(right_seat, (0, 5))

    def test_find_up_bottom_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 5
        given_column = 3

        # When
        up_seat = find_up_seat(content, given_row, given_column)
        bottom_seat = find_bottom_seat(content, given_row, given_column)

        # Then
        self.assertEqual(up_seat, (4, 3))
        self.assertEqual(bottom_seat, (7, 3))

    def test_find_bottom_left_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 1
        given_column = 9

        # When
        left_seat = find_bottom_left_seat(content, given_row, given_column)

        # Then
        self.assertEqual(left_seat, (4, 6))

    def test_find_bottom_right_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 1
        given_column = 6

        # When
        bottom_right_seat = find_bottom_right_seat(content, given_row, given_column)

        # Then
        self.assertEqual(bottom_right_seat, (2, 7))

    def test_find_up_right_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 7
        given_column = 0

        # When
        up_right_seat = find_up_right_seat(content, given_row, given_column)

        # Then
        self.assertEqual(up_right_seat, (5, 2))

    def test_find_up_left_seat(self):
        # Given
        content = parse_input('test.txt')
        given_row = 7
        given_column = 9

        # When
        up_left_seat = find_up_left_seat(content, given_row, given_column)

        # Then
        self.assertEqual(up_left_seat, (4, 6))


if __name__ == '__main__':
    unittest.main()
