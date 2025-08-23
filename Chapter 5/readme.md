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
Index starts from 0 (first element)
Negative index starts from the end (-1 is last element)

```bash
fruits = ["apple", "orange", "banana", "grapes", "guava"]

print(fruits[0])        # apple
print(fruits[-1])       # guava
print(fruits[2])        # banana
```
#### 👉 Slicing
We can get a part (sub-list) using slicing (we already saw in string these in string slicign):
```bash
cars = ["audi", "bmw", "lamborghini", "mercedes", "jaguar", "buggati", "skoda"]


# format : cars[start:stop:step]
print(cars[:::])       # ['audi', 'bmw', 'lamborghini', 'mercedes', 'jaguar', 'buggati', 'skoda']
print(cars[:3])        # ['audi', 'bmw', 'lamborghini']
print(cars[::-1])      # Reverse the list : ['skoda', 'buggati', 'jaguar', 'mercedes', 'lamborghini', 'bmw', 'audi']

print(cars[1:4])       # ['bmw', 'lamborghini', 'mercedes']
```

