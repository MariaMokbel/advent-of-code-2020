import unittest

from day_18.solution import evaluate_expression, compute_with_precedence_level


class MyTestCase(unittest.TestCase):
    def test_simple_expression(self):
        # Given
        given_operation = '1+2*3+4*5+6'

        # When
        solution = evaluate_expression(given_operation)

        # Then
        self.assertEqual(71, solution)

    def test_expression_with_parenthesis(self):
        # Given
        given_operation = '2*3+(4*5)'
        given_operation_2 = '5+(8*3+9+3*4*3)'
        given_operation_3 = '5*9*(7*3*3+9*3+(8+6*4))'
        given_operation_4 = '((2+4*9)*(6+9*8+6)+6)+2+4*2'

        # When
        solution = evaluate_expression(given_operation)
        solution_2 = evaluate_expression(given_operation_2)
        solution_3 = evaluate_expression(given_operation_3)
        solution_4 = evaluate_expression(given_operation_4)

        # Then
        self.assertEqual(26, solution)
        self.assertEqual(437, solution_2)
        self.assertEqual(12240, solution_3)
        self.assertEqual(13632, solution_4)

    def test_expression_with_precedence(self):
        # Given
        given_op = [1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6]

        # When
        solution = compute_with_precedence_level(given_op)

        # Then
        self.assertEqual(231, solution)


if __name__ == '__main__':
    unittest.main()
