from scipy import constants
from scipy.optimize import root 
from math import cos

print(constants.pi)
print(constants.golden)


def eqn(x):
    return x + cos(x)


myroot = root(eqn, 0)
print(myroot)
