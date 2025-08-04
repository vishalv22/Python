# String Functions

# len()
name = "Vishal"
print(len(name))                   # Output: 6

# .endswith()
name = "Vishal"
print(name.endswith("hal"))        # Output: True

# .startswith()
print(name.startswith("vish"))      # Output: False

# .count()
print(name.count("a"))              # Output: 1

# .capitalize()
capp = "he is a good boy"
print(capp.capitalize())            # Output: He is a good boy

# .find()
print(capp.find("good"))            # Output: 8

# .replace()
print(capp.replace("is" , "was"))   # Output: he was a good boy

# .strip()
a = " Hello "
print(a.strip())           # Output: Hello

# .split()
x = "He is playing Football"
print(x.split())           # Output:   ['He', 'is', 'playing', 'Football']  

# .join()
words = ['He', 'is', 'playing', 'Football']
print(' '.join(words))     # Output: He is playing Football
