from SC_Lab_Task3 import sumOfDigits  
import unittest 

class TestSumOfDigits(unittest.TestCase):
    # Test case for positive numbers
    def test_positive_numbers(self):
        # Test with a small positive number (123), sum of digits: 1 + 2 + 3 = 6
        self.assertEqual(sumOfDigits(123), 6)  
        # Test with a larger positive number (9876), sum of digits: 9 + 8 + 7 + 6 = 30
        self.assertEqual(sumOfDigits(9876), 30)  
        # Test with 0, sum of digits is 0
        self.assertEqual(sumOfDigits(0), 0)  

    # Test case for negative numbers
    def test_negative_numbers(self):
        # Test with a negative number (-123). The absolute value is 123, sum of digits: 1 + 2 + 3 = 6
        self.assertEqual(sumOfDigits(-123), 6)  
        # Test with a larger negative number (-9876). The absolute value is 9876, sum of digits: 9 + 8 + 7 + 6 = 30
        self.assertEqual(sumOfDigits(-9876), 30)  

    # Test case for large numbers
    def test_large_numbers(self):
        # Test with a large number (1234567890), sum of digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 0 = 45
        self.assertEqual(sumOfDigits(1234567890), 45)  
        # Test with a large negative number (-1234567890). The absolute value is 1234567890, sum of digits: 45
        self.assertEqual(sumOfDigits(-1234567890), 45)  

# Run the tests when the script is executed directly
if __name__ == "__main__":
    unittest.main()
