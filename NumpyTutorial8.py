"""
Python, Numpy and Probability
Random using numpy

"""
import numpy as np

outcome = np.random.randint(1, 7, size=10)
print(outcome)

# generated 5*4 matrix using the random number range from 1 - 7
"""
output:
[[4 4 5 4]
 [4 4 5 2]
 [3 3 3 4]
 [3 5 4 5]
 [6 1 2 6]]
"""
print(np.random.randint(1, 7, size=(5, 4)))


# Random Choices with Python
"""
choice' is another extremely useful function of the random module.
This function can be used to choose a random element from a non-empty sequence.

"""
# using choice we can pick random from string or list
from random import choice
professions = ["scientist", "philosopher", "engineer", "priest"]
print(choice("abcdefghij"))
print(choice(professions))
print(choice(("apples", "bananas", "cherries")))


