# 📝Chapter 4
## 4.1 Strings
String is a sequence of characters enclosed in quotes, we can primarily write a string in these three ways:
```bash
name = "Vishal"     # 1. Single quoted String
a = 'Hello'         # 2. Double quoted String
b = '''World'''     # 3. Tripple quoted String
```


### ⪼ String Slicing :
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
### ⪼ String Slicing with Skip value :
We can provide a skip value as a part of our slice. <br>
for example:
```bash
a = "0123456789"
print(a[0:8:2])     # Output: 0246

word = "amazing"
print(word[1:6:2])  # Output: mzn
```
<br>

### ⪼ Reversing an Object :
We can use slices to very easily reverse a str, list, or tuple. <br>
for example:
```bash
word = 'reverse me!'
print(word[::-1])   # Output: !em esrever
```
The syntax [::-1] means that the slice should be from the beginning until the end of the string (because start and end are commited) and a step of -1 means that it should move through the string in reverse.

<br>

## 4.2 String Functions
String Functions are built-in method in Python used to perform operations or manipulate string data. <br>


- ```len()``` Function: Returns the length of the String.
```bash
name = "Vishal"
print(len(name))                   # Output: 6
```
- ```.endswith()``` : Check if string ends with given value.
```bash
name = "Vishal"
print(name.endswith("hal"))        # Output: True
```
- ```.startswith()``` : Check if string starts with given value.
```bash
name = "Vishal"
print(name.startswith("vish"))      # Output: False  (Case-sensitive)
```
- ```.count()``` : Count how many times a substring appears.
```bash
name = "Vishal"
print(name.count("a"))              # Output: 1
```
- ```.capitalize()``` : Capitalize the first letter of String.
```bash
capp = "he is a good boy"
print(capp.capitalize())            # Output: He is a good boy
```
- ```.find()``` : Find index of first match, -1 if not found.
```bash
capp = "he is a good boy"
print(capp.find("good"))            # Output: 8
```
- ```.replace()``` : Replace one substring with another.
```bash
capp = "he is a good boy"
print(capp.replace("is" , "was"))   # Output: he was a good boy
```
- ```.strip()``` : Remove space from start and end
```bash
a = " Hello "
print(a.strip())           # Output: Hello
```
- ```.split()``` : Splits string into a list
```bash
x = "He is playing Football"
print(x.split())           # Default splits by space
                           # Output:   ['He', 'is', 'playing', 'Football']
```
- ```.join()``` : Join list into a single String
```bash
words = ['He', 'is', 'playing', 'Football']
print(' '.join(words))     # Output: He is playing Football   (join with the " " (space))
```

## 4.3 Escape Sequences
Escape sequences are special characters used to represent certain whitespace characters or characters that are hard to type directly into a string. They start with a backslash (\), followed by a character that represents something else.
### Common Escape Sequences
```\n``` ⟶ New line
```\t``` ⟶ Tab (Horizontal)
```\\``` ⟶ Backslash
```\'``` ⟶ Single quote 
```\"``` ⟶ Double quote 
```\r``` ⟶ Carriage return 
```\b``` ⟶ Backspace 
```\a``` ⟶ Bell / Alert sound

Escape sequences only work in Strings.

