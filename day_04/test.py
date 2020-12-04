import unittest

from day_04.solution import check_byr_correct, check_iyr_correct, check_eyr_correct, check_hgt_correct, \
    check_ecl_correct, check_pid_correct, check_hcl_correct


class MyTestCase(unittest.TestCase):
    def test_byr_check_true(self):
        # Given
        potential_byr = '2002'

        # When Then
        self.assertTrue(check_byr_correct(potential_byr))

    def test_byr_check_false(self):
        # Given
        potential_byr = '2003'

        # When Then
        self.assertFalse(check_byr_correct(potential_byr))

    def test_iyr_check_true(self):
        # Given
        potential_iyr = '2015'

        # When Then
        self.assertTrue(check_iyr_correct(potential_iyr))

    def test_iyr_check_false(self):
        # Given
        potential_iyr = '2022'

        # When Then
        self.assertFalse(check_iyr_correct(potential_iyr))

    def test_eyr_check_true(self):
        # Given
        potential_eyr = '2020'

        # When Then
        self.assertTrue(check_eyr_correct(potential_eyr))

    def test_eyr_check_false(self):
        # Given
        potential_eyr = '20224'

        # When Then
        self.assertFalse(check_eyr_correct(potential_eyr))

    def test_hgt_check_true(self):
        # Given
        potential_hgt_in = '60in'
        potential_hgt_cm = '190cm'

        # When Then
        self.assertTrue(check_hgt_correct(potential_hgt_cm))
        self.assertTrue(check_hgt_correct(potential_hgt_in))

    def test_hgt_check_false(self):
        # Given
        potential_hgt = '60'
        potential_hgt_in = '190in'

        # When Then
        self.assertFalse(check_hgt_correct(potential_hgt))
        self.assertFalse(check_hgt_correct(potential_hgt_in))

    def test_ecl_check_true(self):
        # Given
        potential_ecl = 'brn'

        # When Then
        self.assertTrue(check_ecl_correct(potential_ecl))

    def test_ecl_check_false(self):
        # Given
        potential_ecl = 'wat'

        # When Then
        self.assertFalse(check_ecl_correct(potential_ecl))

    def test_pid_check_true(self):
        # Given
        potential_pid = '934693255'

        # When Then
        self.assertTrue(check_pid_correct(potential_pid))

    def test_pid_check_false(self):
        # Given
        potential_pid = '0123456789'

        # When Then
        self.assertFalse(check_pid_correct(potential_pid))

    def test_hcl_check_true(self):
        # Given
        potential_hcl = '#123abc'

        # When Then
        self.assertTrue(check_hcl_correct(potential_hcl))

    def test_hcl_check_false(self):
        # Given
        potential_hcl_1 = '#123abz'
        potential_hcl_2 = '123abc'

        # When Then
        self.assertFalse(check_hcl_correct(potential_hcl_1))
        self.assertFalse(check_hcl_correct(potential_hcl_2))


if __name__ == '__main__':
    unittest.main()
