from regress import *
import numpy as np
import random

R= PyRegress([2, 5, 2, 3, 8,4,8,3,11, 2,3, 5, 3])
print(R.mean(), R.Var(), R.SD())
print(R.sample())
print(R.mode())