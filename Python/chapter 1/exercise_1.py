#Q. print a poem using python.

print('''Twinkle, Twinkle Little Star
How i wonder what you are?
Up above the world so high
Like a diamond in the sky.''')


#Q. Install the external module and use it to perform an operation of your interest.
#pip install pyttx3, (text to speech module)
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


#Q. Write the python program to print the contents of a directory using the os module. Search online for the function which does that.

import os
directory_path = "C:\\Users\\sonam\\Desktop"    # Specify the directory path
contents = os.listdir(directory_path)     # Get the list of contents (files and directories)
print("Contents of", directory_path)     # Print the contents
for item in contents:
  print(item)