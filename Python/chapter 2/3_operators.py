#OPERATORS IN PYTHON

# Arithmetic Operators: + , - , * , / , etc.
a = 6
b = 8
print(a+b)

# Assignment Operators: = , += , -= , etc.
a = 7
b = 5
b += 3  #increment the value of b by 3 and then assign it to b. (b=8)
print(b) 

b -= 4 #decrement the value of b by 4 and then assign it to b. (8-4=b=4)
print(b) 

# Comparison Operators: == , != , > , < , >= , <= , etc.
a = 7 == 7
print(a)      #Output: True, 7 == 7.
d = 5 < 4
print(d)      #Output: False, 5 is not < 4.
e = 5 >= 4
print(e)      #Output: True, 5 >= 4.

# Logical Operators: and  , or , not , etc.
x = True or False
print(x)
#truth table of 'or'                        (ek bhi true hua to true)
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

#truth table of 'and'                           (ek bhi false hua to false)
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)


print(not(True))          #Output: False
print(not(False))         #Output: True
