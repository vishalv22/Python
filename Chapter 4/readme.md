# 📝Chapter 4
## 4.1 String Datatype
String is a DataType in Pyhton.<br>
String is a sequence of characters enclosed in quotes, we can primarily write a string in these three ways:
```bash
name = "Vishal"     # 1. Single quoted String
a = 'Hello'         # 2. Double quoted String
b = '''World'''     # 3. Tripple quoted String
```


### ⪼ String Slicing:
String slicing lets us “cut” and “pick” parts of a string the way we want.<br>
Format for Slicing:
```bash
print(text[start : stop : step])

# start = where to *start* (index)
# stop = where to *stop* (index, *not* included)
# step = how many characters to *skip* each time 
```
<br>

→ The index in a String (left to right) starts from '0' , means The first character is at position 0, second at 1, and so on. (0, 1, 2, ...)
<br><br>

→ Negative indexing (right to left) : here -1 refers to the last character, -2 to the second last, and so on. (..., -3, -2, -1)
<p align="center">
<img src="https://github.com/user-attachments/assets/2e62ed3c-cdf2-4881-89c7-13dd156a09e6" alt="Image" width="500">
</p>

Some examples: 
```bash
a = "abcdef"
a        # 'abcdef'
         # Same as a[:] or a[::] since it uses the defaults for all three indices   
a[-1]    # 'f'
a[:]     # 'abcdef'
a[::]    # 'abcdef'
a[3:]    # 'def' (from index 3, to end(defaults to size of iterable))
a[:4]    # 'abcd' (from beginning (default 0) to position 4(excluded))
a[2:4]   # 'cd' (form position 2, to position 4(excluded))
```
### ⪼ String Slicing with Skip value:
We can provide a skip value as a part of our slice. <br>
for example:
```bash
a = "0123456789"
print(a[0:8:2])     # Output: 0246

word = "amazing"
print(word[1:6:2])  # Output: mzn
```
## 4.2 Reversing an Object
We can use slices to very easily reverse a str, list, or tuple. <br>
for example:
```bash
word = 'reverse me!'
print(word[::-1])   # Output: !em esrever
```
The syntax [::-1] means that the slice should be from the beginning until the end of the string (because start and end are commited) and a step of -1 means that it should move through the string in reverse.
