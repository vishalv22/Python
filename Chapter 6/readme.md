# 📝Chapter 6
## 6.1 Tuples
- Tuples are represented as comma-separated value of any data type within parentheses (round brackets).
- It can hold different data types.
- A tuple is very similar to list, but a big difference is Tuples are **immutable** (cannot be changed after creation)

Example: 
```python
var = ("Vishal", 20, False, 49.55)

print(type(var))      # Output : <class 'tuple'>
```

## 6.2 Tuple Creation
```python
# Tuple with round brackets ()
numbers = (1, 2, 3, 4, 5)

# can store different data types
var = ("Vishal", 20, False, 49.55)

# Tuple with single element (comma is must!)
var1 = (49,)

# Tuple without brackets (packing)
p = 10, ""Vishal"", 40
```

<br>

### What is Packing and Unpacking?
#### *Packing* :
Multiple values are combined into a single variable. And this is how we normally write lists and tuples, multiple elements packed together into one variable..
```python
t = 10, 20, 40        # Tuple packing 
l = [10, 20, 40]      # List packing
```

#### *Unpacking* :
Unpacking means distributing elements into multiple variables (each gets its own)
```python
t = (10, 20, 40)      # Tuple 

a, b, c = t           # Tuple unpacking
print(a, b, c)        # 10 20 40
```
Also, there is a special case called *Extended Unpacking*, For example:
```python
t = (10, 20, 40, 50)      # Tuple

# Example: 1
a, *b = t
print(a)        # 10
print(b)        # [20, 40, 50]     # a List, not Tuple

# Example: 2
a, *b, c = t
print(a)        # 10
print(b)        # [20, 30]
print(c)        # 50
```
So, with the ```*``` operator, one variable can collect the remaining elements (always as a *list*).