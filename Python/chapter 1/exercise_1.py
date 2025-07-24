# 1. Python program to print the poem "Twinkle, Twinkle Little Star"

print('''Twinkle, Twinkle Little Star
How I wonder what you are?
Up above the world so high
Like a diamond in the sky.''')


# 2. Install the external module and use it to perform an operation of your interest.
#pip install pyttsx3, (text to speech module)
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# 3. Write the python program to print the contents of a directory using the os module. Search online for the function which does that.

import os
directory_path = "C:\\Users\\sonam\\Desktop\\Books"    # Specify the directory path
contents = os.listdir(directory_path)     # Get the list of contents (files and directories)
print("Contents of", directory_path)     # Print the contents
for item in contents:
  print(item)