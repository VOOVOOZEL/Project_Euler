"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt


for i in range(1000):
    for j in range(1000):
        if sqrt(i**2 + j**2) - int(sqrt(i**2 + j**2)) == 0:
            if i + j + sqrt(i**2 + j**2) == 1000 and i and j:
                print(i * j * sqrt(i**2 + j**2))
