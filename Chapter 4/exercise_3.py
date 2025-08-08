# 1. Write a python program to display a user entered name followed by Good Afternoon using input() function.
name = input("Enter your Name: ")
print("Good Afternoon!", name, "How was your Day?")

#OR
print(f"Good Afternoon! {name} How was your Day?")  # f-string is a way to insert variables directly into a string by putting an 'f' before string and using '{}' inside string 
                                                    # it was introduced in Python 3.6 , more cleaner and faster way to format string




# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|name|>, 
# You are selected! 
# <|Date|>
# '''
letter = '''
Dear <|name|>, 
You are selected! 
<|Date|>
'''
# Method 1
# letter = letter.replace("<|name|>", "Vishal")
# letter = letter.replace("<|Date|>", "07 Aug 2025")
# print(letter)

# Method 2 (better)
print(letter.replace("<|name|>", "Vishal").replace("<|Date|>", "07 Aug 2025")) #chain two replace method together, means we are performing two consecutinve replacements on the string.




# 3. Write a program to detect double space in a string.
c = "The cat jumped onto  the windowsill to watch the rain fall outside."
print(c.find("  "))      # Output : 19 - means the double space "  " starts at index 19 in the string.


# 4. Replace the double space from 'question 3' with single spaces.
print(c.replace("  ", " "))


# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, This python course is nice. Thanks!"
print("Dear Harry,\nThis python course is nice.\nThanks!")