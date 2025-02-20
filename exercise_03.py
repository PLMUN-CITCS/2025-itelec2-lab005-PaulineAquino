# Your Name
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Arithmetic Operators, Operator Precedence, and Parentheses in Python

# Define numeric variables
a = 10 
b = 5 
c = 3

# Calculate expressions without parentheses (demonstrating precedence)
result1 = a + b * c  # Multiplication before addition 
print("Result of a + b * c:", result1)

# Calculate expressions with parentheses (overriding precedence)
result2 = (a + b) * c  # Addition within parentheses first 
print("Result of (a + b) * c:", result2)

# Use subtraction
result3 = a - b 
print("Result of a - b:", result3)

# Use standard and floor division
result4 = a / b  # Standard division 
result5 = a // b  # Floor division 
print("Result of a / b:", result4) 
print("Result of a // b (floor division):", result5)

# Use modulus and exponentiation
result6 = a % b  # Modulus (remainder) 
result7 = a ** c  # Exponentiation (power) 
print("Result of a % b (modulus):", result6) 
print("Result of a ** c (exponentiation):", result7)

# Combine operators in a more complex expression
result8 = (a + b - c) * (a / b) 
print("Result of (a + b - c) * (a / b):", result8)
