#Modules allow us to avoid writing everything from scratch by reusing existing, reliable code.
#first install module using terminal, 'pip install pyjokes', and then import it.

import pyjokes
joke = pyjokes.get_joke()
print(joke)

#this will print a random joke.