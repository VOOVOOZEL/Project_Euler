"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

const = 600851475143
div = 2

while True:
    if const % div == 0:
        if const == div:
            print (div)
            break
        const /= div
    else:
        div += 1