# 1. Python program to print the poem "Twinkle, Twinkle Little Star"

print("""Twinkle Twinkle Little Star 
How I wonder what you are? 
Up above the world so high
Like a diamond in the Sky.""")




# 2. Install the external module and use it to perform an operation of your interest.
#pip install pyttsx3, (text to speech module)

import pyttsx3
engine = pyttsx3.init()
engine.say("Twinkle Twinkle little Star, How i wonder what you are?, Up above the world so high, Like a diamond in the sky.")
engine.runAndWait()





# 3. Write the python program to print the contents of a directory using the os module. Search online for the function which does that.

import os
dir_path = "C:\\Users\\sonam\\Desktop\\Python"            # Specify the directory path
contents = os.listdir(dir_path)                     # Get the list of content (files and directories)
print("Content of", dir_path)                       # Print the content
for item in contents:
    print(item)
