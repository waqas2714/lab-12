def sumOfDigits(n):
    """
    Calculates the sum of the digits of a number.

    Args:
        n (int): The input number.

    Returns:
        int: The sum of the digits.
    """
    # Make sure that the number is positive
    n = abs(n)
    
    # Base case: Number is reduced to 0
    if n == 0:
        return 0
    
    # Recursive case: sum the last digit with the result of the remaining number
    return n % 10 + sumOfDigits(n // 10)
