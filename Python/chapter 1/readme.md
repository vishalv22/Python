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

- ❌We can *not* use **python's keywords** as a valid name. We can see the list of keyword by:
```bash
import keyword
print(keyword.kwlist)
```

<br>

- ### ✅Rules of Variable naming: 
 1. Variable names must start with a letter or an underscore.
```bash
x = True     #valid
_y = True    #valid
    
9x = False   #invalid, starts with numeral
#Output: SyntaxError: invalid syntax 

&y = False   #starts with symbol
#Output: SyntaxError: invalid syntax
```

2. The remainder of your variable name may consist of letters, numbers and underscores.

```bash
has_0_in_it = "still valid"
```
<br>

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
### DataType: 
In Python, a datatype is the classification or category of data that tells the interpreter what kind of value a variable holds and what operations can be performed on it.
#### Some common Built-in Data Types in Python:
```bash
name = "Alice"        # str
age = 25              # int
pi = 3.14             # float
is_valid = True       # bool
fruits = ["apple", "banana"]  # list
person = {"name": "Alice", "age": 25}  # dict
```
📌 We can check the type of any variable using :
```bash
print(type(name))   # Output: <class 'str'>
```

### Modules in Python:
Modules allow us to avoid writing everything from scratch by reusing existing, reliable code.
first install module using terminal, ```bash pip install pyjokes``` and then import it.
```bash
import pyjokes
joke = pyjokes.get_joke()
print(joke)

#this will print a random joke.
```