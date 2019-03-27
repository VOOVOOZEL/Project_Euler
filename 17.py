"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.
"""

one_to_9 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
ten_to_19 = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,17: 9, 18: 8, 19: 8}
tens = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}

number = 999
res = 0

while(number > 0):
    num = number
    if num > 99:
        if num % 100 != 0:
            res += 3
        res += one_to_9[num // 100] + 7
        num %= 100

    if num < 20 and num > 9:
        res += ten_to_19[num]

    if num > 19 and num < 100:
        res += tens[num // 10]
        res += one_to_9[num % 10]

    if num < 10:
        res += one_to_9[num]
    number -= 1
print(res)