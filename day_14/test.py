import unittest

from day_14.solution import apply_mask, apply_mask_to_address, find_all_possible_addresses


class MyTestCase(unittest.TestCase):
    def test_apply_mask(self):
        # Given
        given_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        given_number = 11

        # When
        converted_number = apply_mask(given_number, given_mask)

        # Then
        self.assertEqual(73, converted_number)

    def test_find_all_possible_masks(self):
        # Given
        mask = '000000000000000000000000000000X1001X'
        address = apply_mask_to_address(42, mask)

        # When
        all_addresses = find_all_possible_addresses(address, 0)

        # Then
        self.assertListEqual([26, 27, 58, 59], all_addresses)


if __name__ == '__main__':
    unittest.main()
