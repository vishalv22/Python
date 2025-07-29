# 📝Chapter 1  
## 1.1 Basics

- #### The ```print``` function is used to print output :
```bash
print("Hii My name is Vishal")
# Output: Hii My name is Vishal
```


- #### Comments
Python ignores comments, and so will not execute code in there. It is used to explain code when basic code itself isn't clear.<br>
**Single Line Comments**
```bash
# This is a Single Line Comment in Python
```

**Inline Comment**
```bash
print("Hello")   # This line prints Hello 
```

**Multiline Comments**: Comments spanning multiple lines have """ or ''' on either end.
```bash
"""
This type of comment spans multiple lines.
These are mostly used for documentation of functions, classes and modules.
"""
```
## 1.2 Modules in Python:
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