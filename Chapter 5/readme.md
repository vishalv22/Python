# 📝Chapter 5
## 5.1 List 📋
- A list is a collection of items stored in a single variable. 
- It can hold different data types (integers, strings, float, etc.).
- Lists are ordered, changable (mutable), and allow duplicate values. 
- It is written inside square brackets ```[]```.
<br>
Example:

```bash
my_list = ["Apple", "Orange", 10, 456.89, True, "Vishal"]
```

## 5.2 Accessing Elements in a List
We can access items in a list using indexing and slicing.
#### 👉 Indexing :
- Index starts from ```0``` (first element) 
- Negative index starts from the end (```-1``` is last element)

```bash
fruits = ["apple", "orange", "banana", "grapes", "guava"]

print(fruits[0])        # apple
print(fruits[-1])       # guava
print(fruits[2])        # banana
```
#### 👉 Slicing :
We can get a part (sub-list) using slicing (we already saw in string these in string slicign):
```bash
cars = ["audi", "bmw", "lamborghini", "mercedes", "jaguar", "buggati", "skoda"]

# format : cars[start:stop:step]
print(cars[:::])       # ['audi', 'bmw', 'lamborghini', 'mercedes', 'jaguar', 'buggati', 'skoda']
print(cars[:3])        # ['audi', 'bmw', 'lamborghini']
print(cars[::-1])      # Reverse the list : ['skoda', 'buggati', 'jaguar', 'mercedes', 'lamborghini', 'bmw', 'audi']
print(cars[1:4])       # ['bmw', 'lamborghini', 'mercedes']
```

## 5.3 Mutability of List :
- A list is mutable, which means we can change its element after creation. 
- In contrast, string are immutable (cannot be changed once created). 

Example on changing list item:
```bash
cars = ["audi", "bmw", "lamborghini"]

# changing the second element
cars[1] = "mercedes"

print(cars)

# Output: ['audi', 'mercedes', 'lamborghini'] 
```

Example that string are mutable: 
```bash
name = "vishal"

# we can't do -
# name[0] = "Ironman"

print(name) # Output: vishal
```
<br>
<br>

📋 Note :
- Lists → mutable (can modify)
- Strings, tuples → immutable (cannot modify)


## 5.4 Adding or Removing elements to a List
Python provides different ways to add new items to a list.
#### 👉 ```append()``` – Add at the End
```bash 
fruits = ["apple", "banana"]
fruits.append("mango")

print(fruits)         # Output: ['apple', 'banana', 'mango']
```

#### 👉 ```insert()``` – Add at a Specific Position
```bash
cars = ["audi", "bmw", "mercedes"]
cars.insert(1, "jaguar")

print(cars)           # Output: ['audi', 'jaguar', 'bmw', 'mercedes']
```

#### 👉 ```extend()``` – Add Multiple Elements
```bash
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])

print(numbers)       # Output: [1, 2, 3, 4, 5, 6]
```
<br>
<br>

We can remove elements from a list in different ways:
#### 👉 ```remove()``` – Remove by Value
```bash 
fruits = ["apple", "banana", "mango", "banana"]
fruits.remove("banana")

print(fruits)        # Output: ['apple', 'mango', 'banana']
# only the first 'banana' is removed
```

#### 👉 ```pop()``` – Remove by Index
```bash
cars = ["audi", "bmw", "mercedes"]
cars.pop(1)          # it will remove element at 1 position, which is "bmw"

print(cars)          # Output: ['audi', 'mercedes']
```

#### 👉 ```clear()``` – Remove All Elements
```bash
numbers = [1, 2, 3, 4]
number.clear()

print(numbers)       # Output: []
```
<br>
<br>

📋 Summary :
- We use ```append()``` for single items, ```extend()``` for multiple, and ```insert()``` when we need control over the position.


- We use ```remove()``` when we know the value, ```pop()``` when we know the index, and ```clear()``` when we want an empty list.

## 5.5 Useful functions with Lists 
#### 👉 len() - Length of List
```bash
fruits = ["banana", "orange", "papaya", "mango"]
print(len(fruits))           # Output: 4
```
#### 👉 min() and max() - Smallest & Largest Value
```bash
# Example 1 :
numbers = [40, 25, 10, 256]
print(min(numbers))          # Output: 10
print(max(numbers))          # Output: 256
```
```min()``` and ```max()``` compare strings based on Unicode values of characters.
```bash
# Example 2 :
fruits = ["apple", "banana", "mango", "cherry"]
print(min(fruits))           # Output: apple        a → Unicode 97
print(max(fruits))           # Output: mango        m → Unicode 109

# Example 3 :
word = "hello"
print(min(word))  # 'e'  (smallest character by Unicode value)
print(max(word))  # 'o'  (largest character)
```

#### 👉 sum() - Sum of All Elements
```bash
# (only works with numbers)

numbers = [40, 25, 10, 256]
print(sum(numbers))          # Output: 326
```
#### 👉 in - Check if Elements Exists
```bash
fruits = ['apple', 'banana', 'guava', 'pineapple', 'grapes']
print("apple" in fruits)     # Output: True
print("manago" in fruits)    # Output: False

```
