""" Problem 005 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive
number that is evenly divisible by all the numbers from 1 to 20?
"""

from math import gcd
from functools import reduce


def lcm(a, b):
    """Return the lowest common multiple of a and b"""
    return abs(a*b) // gcd(a, b)


if __name__ == '__main__':
    n = 20
    print(reduce(lcm, range(1, n + 1)))
