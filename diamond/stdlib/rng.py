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

# Random choice
def pick(list):
    return random.choice(list)

# Weighted choice
def weight(population, weights=None, k=1):
    random.choices(population, weights, k)

# Unique weighted choice
def unique_weight(population, weights=None, k=1):
    if k > len(population):
        raise ValueError("sample size cannot be larger than population")
    is_running = True
    while is_running:
        non_unique = random.choices(population, weights, k)
        unique = []
        for value in non_unique:
            if value in unique:
                continue
            unique.append(value)
        if len(unique) < len(non_unique):
            continue
        is_running = False
    return unique

# Shuffle
def shuffle(objects):
    if type(objects) == list:
        random.shuffle(objects)
        return objects
    elif type(objects) == dict:
        dictionary = list(objects.items())
        random.shuffle(dictionary)
        objects = dict(dictionary)
        return objects
    else:
        raise ValueError("this function was not designed for data types that aren't lists and dictionaries")
