# 📝Chapter 2
## 2.1 Operators in Python
### Arithematics Operators:
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

### Assignment Operators:
```bash
a = 7
b = 5
b += 3      #increment the value of b by 3 and then assign it to b. (b=8)
print(b)
#Output: 8

b -= 4      #decrement the value of b by 4 and then assign it to b. (8-4=b=4)
print(b)
#Output: 4
```
### Comparision Operators:
```bash
a = 7 == 7
print(a)      #Output: True ,   7 = 7.

d = 5 < 4
print(d)      #OutPut: False ,  5 is not < 4.

e = 5 >= 4
print(e)      #Output: True ,   5>4.
```
### Logical Operators:
Truth Table of ```or``` Operator
```bash
print("True or False is ", True or False)        #Output: True or False is True
print(True or True)                              #Output: True
print(False or True)                             #Output: True
print(False or False)                            #Output: False
# 🤔 If one is True, then True
```

Truth Table of ```and``` Operator
```bash
print("True and False is ", True and False)      #Output: True and False is False
print(True and True)                             #Output: True
print(False and True)                            #Output: False
print(False and False)                           #Output: False
# 🤔 If one is False, then False
```

#### Not Operator
```bash 
print(not(True))          #Output: False
```

## 2.2 User-Input

```a = input()```