import random
import time

def telescope(with_pattern=False):
    symbols = ['.', '-', ' ', '\n']
    stream = ''.join(random.choices(symbols, k=500))
    if with_pattern:
        pos = random.randint(100, 400)
        stream = stream[:pos] + "... --- ..." + stream[pos+11:]
    return stream
