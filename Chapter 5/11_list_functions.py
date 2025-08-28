# Some functions example to test

fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)         # Output: ['apple', 'banana', 'mango']


cars = ["audi", "bmw", "mercedes"]
cars.insert(1, "jaguar")
print(cars)     # Output: ['audi', 'jaguar', 'bmw', 'mercedes']


numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)       # Output: []



numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)            # [5, 4, 3, 2, 1]  


# min() & map()
# Example 1 :
numbers = [40, 25, 10, 256]
print(min(numbers))          # Output: 10
print(max(numbers))          # Output: 256

# Example 2 :
fruits = ["apple", "banana", "mango", "cherry"]
print(min(fruits))           # Output: apple        a → Unicode 97
print(max(fruits))           # Output: mango        m → Unicode 109

# Example 3 :
word = "hello"
print(min(word))  # 'e'  (smallest character by Unicode value)
print(max(word))  # 'o'  (largest character)



# (only works with numbers)
numbers = [40, 25, 10, 256]
print(sum(numbers))          # Output: 331


fruits = ['apple', 'banana', 'guava', 'pineapple', 'grapes']
print("apple" in fruits)     # Output: True
print("mango" in fruits)    # Output: False