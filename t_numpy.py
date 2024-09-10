import numpy as np
from numpy import random

x = random.randint(100, size=(2, 3, 2))
print(x)
print(x.shape)
print(x[0])
print(x[0][2][1])
