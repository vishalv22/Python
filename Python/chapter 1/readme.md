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

2. The remainder of your variable name may consist of letters, numbers and underscores

```bash
has_0_in_it = "still valid"
```
<br>

📌When we use = to do an assignment operation, what's on the left of = is a **name** for the **object** on the right. Finally, what = does is assign the **reference** of the object on the right to the **name** on the left.