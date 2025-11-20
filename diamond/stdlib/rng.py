"""
the rng module with random features
"""
import random

# random.randint() simplified
def randint(bottom, top):
    return random.randint(bottom, top)

# randrange is now easier to read
def increment(bottom, top, steps):
    return random.randrange(bottom, top, increment)

# Brand new percent that checks if the statement is true based on a percent chance
def chance(percent):
    try:
        num = random.randint(1, 100)
        if num <= percent:
            return True
        else:
            return False
    except Exception as e:
        print(e)

# Random float
def random_float():
    return random.random()
