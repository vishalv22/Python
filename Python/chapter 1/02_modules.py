#Modules allow us to avoid writing everything from scratch by reusing existing, reliable code.
#first install module using terminal, 'pip install pyjokes', and then import it.

import pyjokes
joke = pyjokes.get_joke()
print(joke)

#this will print a random joke.

#Built in modules contains extra functionalities. For example to get square root of a number we need to include math module.
import math
print(math.sqrt(16)) # 4.0

dir (math) #this will show all the functions available in math module.
#for example, we can use 'math.pi' to get the value of pi.