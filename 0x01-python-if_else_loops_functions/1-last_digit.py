#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s_last = str(number)
last = int(s_last[-1])
# turn number negative
if number < 0:
    last *= -1
else:
    pass
if last > 5:
    print(f'Last digit of {number:d} is {last:d} and is greater than 5')
if last == 0:
    print(f'Last digit of {number:d} is {last:d} and is 0')
if last < 6 and last != 0:
    print(f'Last digit of {number:d} is {last:d} and is less than 6 and not 0')
