# Ways to write a String. 

name = "Vishal"      # double quoted
a = 'Hello'          # Single quoted 
b = '''World'''      # Tripple quoted 



# String Slicing                            #yaha sidhi counting 0 se start hoti h, or ulti counting -1, -2, ... hoti h.

full_name = "Mr. Vishal Kumar"
short_name = full_name[4:10]                # 4:10 means, 4 se (with 4) --> 10 tak (without 10).   also remember counting starts from 0.
print(short_name)



"""Other advanced slicing techniques: (ALL GIVES SAME RESULT)
print(full_name[0:17])
#OR
print(full_name[:])
#OR 
print(full_name[:17])
#OR
print(full_name[0:])
"""


# Negative slicing
name = "Namya"

print(name[-4:-1])
# OR
# print(name[1:4])     # Output: amy



# Slicing with skip Value 
a = "0123456789"
print(a[0:8:2])            # This means, 0 se 7th tak and then uska 2nd-2nd characters..  Output: 0246

word = "amazing"
print(word[1: 6: 2])       # Output: mzn