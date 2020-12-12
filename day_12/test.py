import unittest

from day_12.solution import turn_left


class MyTestCase(unittest.TestCase):
    def test_turn_left_S_180_should_return_N(self):
        # Given
        current_direct = 'S'
        degrees = 180

        # When
        new_directon = turn_left(current_direct, degrees)

        # Then
        self.assertEqual('N', new_directon)


if __name__ == '__main__':
    unittest.main()
