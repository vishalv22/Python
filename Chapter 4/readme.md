# 📝Chapter 4
## 4.1 Strings
String is a sequence of characters enclosed in quotes, we can primarily write a string in these three ways:
```python
name = "Vishal"     # 1. Double quoted String
a = 'Hello'         # 2. Single quoted String
b = '''World'''     # 3. Triple quoted String (multi-line also possible)
```


### ⪼ String Slicing :
String slicing lets us “cut” and “pick” parts of a string the way we want.<br>
Format for Slicing:
```python
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
```python
a = "abcdef"
a        # 'abcdef'
         # Same as a[:] or a[::] since it uses the defaults for all three indices   
a[-1]    # 'f'
a[:]     # 'abcdef'
a[::]    # 'abcdef'
a[3:]    # 'def' (from index 3, to end(defaults to size of iterable))
a[:4]    # 'abcd' (from beginning (default 0) to position 4(excluded))
a[2:4]   # 'cd' (from position 2, to position 4(excluded))
```
### ⪼ String Slicing with Skip value :
We can provide a skip value as a part of our slice. <br>
for example:
```python
a = "0123456789"
print(a[0:8:2])     # Output: 0246

word = "amazing"
print(word[1:6:2])  # Output: mzn
```
<br>

### ⪼ Reversing an Object :
We can use slices to very easily reverse a str, list, or tuple. <br>
for example:
```python
word = 'reverse me!'
print(word[::-1])   # Output: !em esrever
```
The syntax [::-1] means that the slice should be from the beginning until the end of the string (because start and end are ommitted) and a step of -1 means that it should move through the string in reverse.

<br>

## 4.2 String Functions
String Functions are built-in method in Python used to perform operations or manipulate string data. <br>


- ```len()``` Function: Returns the length of the String.
```python
name = "Vishal"
print(len(name))                   # Output: 6
```
- ```.endswith()``` : Check if string ends with given value.
```python
name = "Vishal"
print(name.endswith("hal"))        # Output: True
```
- ```.startswith()``` : Check if string starts with given value.
```python
name = "Vishal"
print(name.startswith("vish"))      # Output: False  (Case-sensitive)
```
- ```.count()``` : Count how many times a substring appears.
```python
name = "Vishal"
print(name.count("a"))              # Output: 1
```
- ```.capitalize()``` : Capitalize the first letter of String.
```python
capp = "he is a good boy"
print(capp.capitalize())            # Output: He is a good boy
```
- ```.find()``` : Find index of first match, -1 if not found.
```python
capp = "he is a good boy"
print(capp.find("good"))            # Output: 8
```
- ```.replace()``` : Replace one substring with another.
```python
capp = "he is a good boy"
print(capp.replace("is" , "was"))   # Output: he was a good boy
```
- ```.strip()``` : Remove space from start and end
```python
a = " Hello "
print(a.strip())           # Output: Hello
```
- ```.split()``` : Splits string into a list
```python
x = "He is playing Football"
print(x.split())           # Default splits by space
                           # Output:   ['He', 'is', 'playing', 'Football']
```
- ```.join()``` : Join list into a single String
```python
words = ['He', 'is', 'playing', 'Football']
print(' '.join(words))     # Output: He is playing Football   (join with the " " (space))
```

## 4.3 Escape Sequences
Escape sequences are special characters used to represent certain whitespace characters or characters that are hard to type directly into a string. They start with a backslash (```\```), followed by a character that represents something else.
### Common Escape Sequences
```\n``` ⟶ New line <br>
```\t``` ⟶ Tab (Horizontal) <br>
```\\``` ⟶ Backslash <br>
```\'``` ⟶ Single quote <br>
```\"``` ⟶ Double quote <br>
```\r``` ⟶ Carriage return <br>
```\b``` ⟶ Backspace <br>
```\a``` ⟶ Bell / Alert sound <br>

Escape sequences only work in Strings.

<br>

## 🎯 Exercise 3
#### 1. Write a python program to display a User entered name followed by Good Afternoon using input() function.
#### 2. Write a program to fill in a letter template given below with name and date.
```python
letter = '''
Dear <|name|>, 
You are selected! 
<|Date|>
'''
```
#### 3. Write a program to detect double space in a string.
#### 4. Replace the double space from 'question 3' with single spaces.
#### 5. Write a program to format the following letter using escape sequence characters.
```python
letter = "Dear Harry, this python course is nice. Thanks!"
```
