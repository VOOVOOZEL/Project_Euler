"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

arr = [20, 20]


def res(arr):
    if arr == [0, 0]:
        return 1
    path = 0
    if arr[0] > 0:
        path += res([arr[0] - 1, arr[1]])
    if arr[1] > 0:
        path += res([arr[0], arr[1] - 1])

    return path


if __name__ == '__main__':
    #recursive way
    print(res(arr))

    #solve with all kind of permutations
    print(math.factorial(40) // (math.factorial(20) ** 2))