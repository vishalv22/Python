#we don't need to write every code from scratch,thats why we use modules.
#first install module using terminal, 'pip install pyjokes', then import.

import pyjokes
joke = pyjokes.get_joke()
print(joke)

#this prints random jokes.