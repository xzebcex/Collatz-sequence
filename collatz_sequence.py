# Collatz sequence.

"""The Collatz sequence, also called the 3n + 1 
problem, is the simplest impossible math 
problem. (But don't worry, the program 
itself is easy enough for beginners.) From a 
starting number, n, follow three rules to get the next 
number in the sequence:
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.
It is generally thought, but so far not mathematically proven, that 
every starting number eventually terminates at 1."""

import sys
import time

response = input('Enter a starting number (greater than 0) or QUIT: ')

if not response.isdecimal() or response == '0':
    print('You must Enter a Integer greater than zero.')
    sys.exit()

number = int(response)
print(number, end='', flush=True)
while number != 1:
    if number % 2 == 0:  # if number is even.
        number = number // 2
    else:  # Otherwise, number is odd.
        number = 3 * number + 1

    print(', ' + str(number), end='', flush=True)
    time.sleep(0.1)
