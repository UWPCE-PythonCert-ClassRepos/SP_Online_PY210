#!/usr/bin/env python3

for x in range(1, 101):
    line = ''
    if x%3 == 0:
        line = line + 'Fizz'
    if x%5 == 0:
        line = line + 'Buzz'

    if line:
        print (line)
    else:
        print (x)
