import sys

import my_mod
from my_mod import say_welcome as new_welcome

print(sys.path)

# Import the module directly
# my_mod.say_hello("Fady")
my_mod.say_welcome("Fady")

# Import a function with an alias
new_welcome("Fady")
