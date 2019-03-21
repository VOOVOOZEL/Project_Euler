"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

n = 10001
i = 2
res = 0
while res != n:
    for j in range(i):
        j += 2
        if i % j == 0 and i != j:
            break
        elif i == j:
            res += 1
    i += 1
print(i - 1)