import random
import time

seed = int(time.time())
random.seed(seed)

lower = len("")
upper = len("random") * len("generator")
value = random.randint(lower, upper)

print("Random value:", value)
