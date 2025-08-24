# 📝Chapter 2  

## 2.1 Creating variables and assigning values
- python uses "=" to assign values to **variables**.
```<variable name> = <value>```

- Assigning values to different **data types**
```python
#Inteegr
a=2
print(a)

#Output: 2
```
```python
#Float
pi = 3.14
print(pi)

#Output: 3.14
```
```python
#String
name = 'Vishal'
print(name)

#Output: Vishal
```
```python
#Boolean
x = true
print(x)

#Output: True
```
```python
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
```python
import keyword
print(keyword.kwlist)
```
<hr>

📌 When we use = to do an assignment operation, what's on the left of = is a **name** for the **object** on the right. Finally, what = does is assign the **reference** of the object on the right to the **name** on the left.
<br>

- You can assign multiple values to multiple variables in one line.
```python
a, b, c = 1, 2, 3
print(a, b, c)

# Output: 1 2 3
```

<br>
Also,

```python
a = b = c = 1       # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1

b = 2               # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1     # so output is as expected
```
## 2.2 DataType: 
In Python, a datatype is the classification or category of data that tells the interpreter what kind of value a variable holds and what operations can be performed on it.
#### Some common Built-in Data Types in Python:
```python
name = "Vishal"       # str
age = 19              # int
pi = 3.14             # float
is_valid = True       # bool
fruits = ["apple", "banana"]            # list
person = {"name": "Vishal", "age": 19}  # dict
```
📌 We can check the type of any variable using :
```python
name = "Vishal"
print(type(name))   # Output: <class 'str'>
```
### Converting between datatypes
We can perform explicit datatype conversion.<br>
For example, '123' is of ```str``` type and it can be converted to integer using ```int``` function.
```python
a = '123'
b = int(a)
```
Converting from a float string such as '123.456' can be done using ```float``` function.
```python
a = '123.456'
b = float(a)
c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b) # 123
```

We can also convert sequence or collection types
```python
a = 'hello'
list(a)  # ['h', 'e', 'l', 'l', 'o']
set(a)   # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')
```