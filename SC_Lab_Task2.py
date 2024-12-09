class ExpressionParser:
    def __init__(self, expression):
        """
        Initialize the parser with the given expression.

        Args:
            expression (str): The mathematical expression.
        """
        # Remove all spaces from the expression and store it in self.tokens
        self.tokens = expression.replace(" ", "")  
        self.index = 0  # Initialize the index to keep track of the current position in the expression

    def evaluateExpression(self):
        """
        Evaluate the entire expression.

        Returns:
            float: The result of the expression evaluation.
        """
        # Start parsing from the addition/subtraction level
        return self.parseAdditionSubtraction()

    def parseMultiplicationDivision(self):
        """
        Parse multiplication and division operations.

        Returns:
            float: The result of multiplication/division operations.
        """
        # First, parse the expression within parentheses (if any) or a number
        result = self.parseParentheses()

        # Continue parsing for multiplication or division operations
        while self.index < len(self.tokens):
            # If there's a '*' (multiplication), process it
            if self.tokens[self.index] == '*':
                self.index += 1  # Move past the '*' operator
                result *= self.parseParentheses()  # Multiply the result with the next value
            # If there's a '/' (division), process it
            elif self.tokens[self.index] == '/':
                self.index += 1  # Move past the '/' operator
                divisor = self.parseParentheses()  # Parse the divisor value
                if divisor == 0:  # Check for division by zero
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= divisor  # Divide the result by the divisor
            else:
                break  # If no more multiplication/division operators are found, exit the loop

        return result

    def parseParentheses(self):
        """
        Parse expressions enclosed in parentheses.

        Returns:
            float: The result of the expression within parentheses.
        """
        # Check if the current token is a '(' indicating a sub-expression inside parentheses
        if self.tokens[self.index] == '(':
            self.index += 1  # Move past the opening parenthesis
            result = self.parseAdditionSubtraction()  # Parse the expression inside the parentheses
            # Check if there is a closing parenthesis after the sub-expression
            if self.index >= len(self.tokens) or self.tokens[self.index] != ')':
                raise ValueError("Mismatched parentheses.")
            self.index += 1  # Move past the closing parenthesis
            return result
        # If no parentheses, parse the number directly
        return self.parseNumber()

    def parseAdditionSubtraction(self):
        """
        Parse addition and subtraction operations.

        Returns:
            float: The result of addition/subtraction operations.
        """
        # Start by parsing multiplication/division first, since it has higher precedence
        result = self.parseMultiplicationDivision()

        # Continue parsing for addition or subtraction operations
        while self.index < len(self.tokens):
            # If there's a '+' (addition), process it
            if self.tokens[self.index] == '+':
                self.index += 1  # Move past the '+' operator
                if self.index >= len(self.tokens):  # Check for incomplete expression
                    raise ValueError("Expression ends with an operator.")
                result += self.parseMultiplicationDivision()  # Add the next value to the result
            # If there's a '-' (subtraction), process it
            elif self.tokens[self.index] == '-':
                self.index += 1  # Move past the '-' operator
                if self.index >= len(self.tokens):  # Check for incomplete expression
                    raise ValueError("Expression ends with an operator.")
                result -= self.parseMultiplicationDivision()  # Subtract the next value from the result
            else:
                break  # If no more addition/subtraction operators, exit the loop

        return result

    def parseNumber(self):
        """
        Parse a number (integer or floating-point).

        Returns:
            float: The parsed number.
        """
        number_start = self.index  # Remember the starting position of the number
        # Continue moving the index as long as the current character is part of a number (digits or '.')
        while self.index < len(self.tokens) and (self.tokens[self.index].isdigit() or self.tokens[self.index] == '.'):
            self.index += 1

        # If no valid number was found, raise an error
        if number_start == self.index:
            raise ValueError(f"Expected a number at index {self.index}, but found '{self.tokens[self.index]}'.")
        
        # Return the parsed number as a float
        return float(self.tokens[number_start:self.index])
