# 📝Chapter 3
## 3.1 Operators in Python
### ⪼ Arithematics Operators:
```bash
a = 6
b = 8
print(a+b)           #Output: 14
```
Similarly for, <br>
Addition ```+``` , 
Subtraction ```-```, 
Multiplication ```*```, 
Exponentiation ```**```, 
Division ```/```, 
Floor Division ```//```, 
Modulus ```%```

### ⪼ Assignment Operators:
example - ```=```, ```+=```, ```-=```, etc.
```bash
a = 7
b = 5
b += 3      # Adds 3 to b and stores the result in b (b becomes 8)
print(b)
#Output: 8

b -= 4      # Subtracts 4 from b and stores the result in b (8 - 4 = 4)
print(b)
#Output: 4
```
### ⪼ Comparision Operators:
example - ```==```, ```!=```, ```>```, ```<```, ```>=```, ```<=```
```bash
a = 7 == 7
print(a)      # Output: True (because 7 is equal to 7)

d = 5 < 4
print(d)      # Output: False (5 is not less than 4)

e = 5 >= 4
print(e)      # Output: True (5 is greater than or equal to 4)
```
### ⪼ Logical Operators:
example - ```or```, ```and```, ```not```

- Truth table of ```or```
```bash
print("True or False is :", True or False)      # Output: True or False is : True
print("True or True is :", True or True)        # Output: True or True is : True
print("False or True is :", False or True)      # Output: False or True is : True
print("False or False is :", False or False)    # Output: False or False is : False

# (returns True if any one is True)
```

- Truth Table of ```and``` Operator
```bash
print("True and False is", True and False)    # Output: True and False is : False
print("True and True is", True and True)      # Output: True and True is : True
print("False and True is", False and True)    # Output: False and True is : False
print("False and False is", False and False)  # Output: False and False is : False

# (returns False if any one is False)
```

- ```not``` Operator
```bash
print(not(True))          #Output: False
print(not(False))         #Output: True
```

### ⪼ Identity Operators:
example - ```is``` and ```is not```
```bash
a = 9
b = 9
print(a is b)       # True
print(a is not b)   # True
```

### ⪼ Membership Operators
example - ```in```, ```not in``` <br>
We can use ```in``` and ```not in``` with lists, tuples, strings, dictionaries (checks keys)

```bash
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)                   # Output: True 

text = "I am Vishal"
print("Ironman" not in text, "but He is")   #Output: True but He is 
```
<br>
<br>

## 3.2 User-Input
To get input from the user, we use the ```input``` function
```bash
name = input("What is your name? ")
#Output: What is your name? 
```
If user types *Vishal* and hit enter, the variable ```name``` will be assigned to the string ```"Vishal"```
```bash
name = input("What is your name? ")
#Output: What is your name? Vishal
print(name)
#Output: Vishal
```

📌 Note that the input is always of type ```str```, which is important if we want the user to enter numbers. Therefore, we need to convert the ```str``` before trying to use it as a number:
```bash
a = int(input("Enter the first Number: "))          # int(), now it will take input from user as a Number. 
b = int(input("Enter the second Number: "))

print("The sum of both Numbers is: ", a + b)
```
another example:
```bash
x = input("Write a number:")
# Out: Write a number: 10
x / 2
# Out: TypeError: unsupported operand type(s) for /: 'str' and 'int'
float(x) / 2
# Out: 5.0
```

## 🎯 Exercise 2
#### 1. Write a python program to add two numbers.
#### 2. Write a python program to find remainder when a number is divided by 2.
#### 3. Check the type of Variable assigned using input() function.
#### 4. Use Comparision Operator to find out whether a given variable is greater than 'b' or not. Take a = 34 and b = 80.
#### 5. Write a python program to find an average numbers entered by the user.
#### 6. Write a Python program to calculate the Square of a Number entered by the user.