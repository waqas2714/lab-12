from SC_Lab_Task2 import ExpressionParser 
import unittest  

class TestExpressionParser(unittest.TestCase):
    # Test case for basic arithmetic operations (addition, subtraction, multiplication, division)
    def test_basic_operations(self):
        # Test for addition
        self.assertAlmostEqual(ExpressionParser("3 + 5").evaluateExpression(), 8)
        # Test for subtraction
        self.assertAlmostEqual(ExpressionParser("10 - 4").evaluateExpression(), 6)
        # Test for multiplication
        self.assertAlmostEqual(ExpressionParser("6 * 7").evaluateExpression(), 42)
        # Test for division
        self.assertAlmostEqual(ExpressionParser("8 / 4").evaluateExpression(), 2)

    # Test case to check operator precedence (multiplication/division before addition/subtraction)
    def test_operator_precedence(self):
        # Test expression with mixed operators; multiplication should happen first
        self.assertAlmostEqual(ExpressionParser("3 + 5 * 2").evaluateExpression(), 13)
        # Test expression with division before subtraction
        self.assertAlmostEqual(ExpressionParser("10 - 6 / 2").evaluateExpression(), 7)

    # Test case to check if parentheses are handled correctly
    def test_parentheses(self):
        # Test expression with parentheses to change the order of operations
        self.assertAlmostEqual(ExpressionParser("(3 + 5) * 2").evaluateExpression(), 16)
        # Test expression with parentheses to change the order of operations
        self.assertAlmostEqual(ExpressionParser("10 - (2 + 3)").evaluateExpression(), 5)

    # Test case to check if floating-point numbers are handled correctly
    def test_floating_point(self):
        # Test expression with floating-point numbers (addition)
        self.assertAlmostEqual(ExpressionParser("3.5 + 2.5").evaluateExpression(), 6.0)
        # Test expression with floating-point numbers (multiplication)
        self.assertAlmostEqual(ExpressionParser("5.5 * 2").evaluateExpression(), 11.0)

    # Test case for invalid expressions to check error handling
    def test_invalid_expressions(self):
        # Test for incomplete expression with an operator at the end
        with self.assertRaises(ValueError):
            ExpressionParser("3 + ").evaluateExpression()
        # Test for mismatched parentheses (missing closing parenthesis)
        with self.assertRaises(ValueError):
            ExpressionParser("(3 + 5").evaluateExpression()
        # Test for division by zero
        with self.assertRaises(ZeroDivisionError):
            ExpressionParser("8 / 0").evaluateExpression()

# Run the tests when the script is executed directly
if __name__ == "__main__":
    unittest.main()
