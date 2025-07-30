# OPERATORS IN PYTHON

print("=== Arithmetic Operators ===")

# Arithmetic Operators: + , - , * , / , //, %, ** etc.
a = 6
b = 8
print("Addition:", a + b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponentiation:", a ** b)



print("=== Assignment Operator ===")

# Assignment Operators: = , += , -= , etc.
a = 7
b = 5
b += 3  # Adds 3 to b and stores the result in b (b becomes 8)
print(b)

b -= 4  # Subtracts 4 from b and stores the result in b (8 - 4 = 4)
print(b)



print("=== Comparison Operators ===")

# Comparison Operators: == , != , > , < , >= , <=
a = 7 == 7
print(a)  # Output: True (because 7 is equal to 7)

d = 5 < 4
print(d)  # Output: False (5 is not less than 4)

e = 5 >= 4
print(e)  # Output: True (5 is greater than or equal to 4)



print("=== Logical Operators ===")

# Logical Operators: and , or , not
x = True or False
print(x)  # Output: True

# Truth table of 'or' (returns True if any one is True)
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

print("____________________d")

# Truth table of 'and' (returns False if any one is False)
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print("____________________e")

# 'not' operator reverses the boolean value
print(not(True))   # Output: False
print(not(False))  # Output: True


# Identity Operators: is, is not

# Membership Operators: in, not in