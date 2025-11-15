import random

def randint(bottom, top):
    return random.randint(bottom, top)

def increment(bottom, top, increment):
    return random.randrange(bottom, top, increment)

def chance(percent):
    try:
        num = random.randint(1, 100)
        if num <= percent:
            return True
        else:
            return False
    except Exception as e:
        print(e)

def random_float():
    return random.random()
