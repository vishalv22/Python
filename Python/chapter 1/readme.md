# 📝Chapter 1  

## 1.1 Creating variables and assigning values
- python uses "=" to assign values to **variables**.
```<variable name> = <value>```

- Assigning values to different **data types**
```bash
#Inteegr
a=2
print(a)

#Output: 2
```
```bash
#Float
pi = 3.14
print(pi)

#Output: 3.14
```
```bash
#String
name = 'Vishal'
print(name)

#Output: Vishal
```
```bash
#Boolean
x = true
print(x)

#Output: True
```
```bash
#empty value or null data type
z = None
print(z)

#Output: None
```
<br>

### ✅Rules of Variable naming: 
- A variable name can contain alphabets, digits, and underscores.
- A variable name can only start with an alphabet and underscores.
- A variable name can not **start with the digit**.
- **NO** white **SPACE** is allowed to be used inside a variable name. <br>

- ❌We can *not* use **python's keywords** as a valid name. We can see the list of keyword by:
```bash
import keyword
print(keyword.kwlist)
```
<hr>

📌 When we use = to do an assignment operation, what's on the left of = is a **name** for the **object** on the right. Finally, what = does is assign the **reference** of the object on the right to the **name** on the left.
<br>

- You can assign multiple values to multiple variables in one line.
```bash
a, b, c = 1, 2, 3
print(a, b, c)

# Output: 1 2 3
```

<br>
Also,

```bash
a = b = c = 1       # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1

b = 2               # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1     # so output is as expected
```
## 1.2 DataType: 
In Python, a datatype is the classification or category of data that tells the interpreter what kind of value a variable holds and what operations can be performed on it.
#### Some common Built-in Data Types in Python:
```bash
name = "Vishal"       # str
age = 19              # int
pi = 3.14             # float
is_valid = True       # bool
fruits = ["apple", "banana"]            # list
person = {"name": "Vishal", "age": 19}  # dict
```
📌 We can check the type of any variable using :
```bash
print(type(name))   # Output: <class 'str'>
```
### Converting between datatypes
We can perform explicit datatype conversion.<br>
For example, '123' is of ```str``` type and it can be converted to integer using ```int``` function.
```bash
a = '123'
b = int(a)
```
Converting from a float string such as '123.456' can be done using ```float``` function.
```bash
a = '123.456'
b = float(a)
c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b) # 123
```

We can also convert sequence or collection types
```bash
a = 'hello'
list(a)  # ['h', 'e', 'l', 'l', 'o']
set(a)   # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')
```

## 1.3 Modules in Python:
Modules allow us to avoid writing everything from scratch by reusing existing, reliable code.
first install module using terminal, ```pip install pyjokes``` and then import it.
```bash
import pyjokes
joke = pyjokes.get_joke()
print(joke)

#this will print a random joke.
```
Built in modules (don't need to install) contains extra functionalities. For example to get square root of a number we need to include math module.
```bash
import math
print(math.sqrt(16)) # 4.0
```
To know all the functions in a module we can assign the functions list to a variable, and then print the variable.
```bash
import math
dir (math) #this will show all the functions available in math module.
#for example, we can use 'math.pi' to get the value of pi.
```

## 🎯 Exercise 1
#### 1. Python program to print the poem "Twinkle, Twinkle Little Star"
#### 2. Install the external module and use it to perform an operation of your interest.
#### 3. Write the python program to print the contents of a directory using the os module. Search online for the function which does that.
