"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

num = 2000000
sum = 0

sieve = [True] * (num + 1)
for i in range(2, int((num**0.5) + 1)):
    if sieve[i]:
        sieve[i*i::i] = [False] * len(sieve[i*i::i])
for i in range(2, num + 1):
    if sieve[i]:
        sum += i
print(sum)