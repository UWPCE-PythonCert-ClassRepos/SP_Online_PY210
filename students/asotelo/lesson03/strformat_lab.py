#!/usr/bin/python3
'''
Author: Alex Sotelo
Exercise 3.3
Python 3 required
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
'''

#Task One
fString = ( 2, 123.4567, 10000, 12345.67)
element1 = int(fString[0])
element2 = float(fString[1])
element3 = int(fString[2])
element4 = float(fString[3])

print(f"'file_{element1:03d} :   {element2:.2f}, {element3:.2e}, {element4:.2e}'")

#Task Two
print("'file_{:03d} :   {:.2f}, {:.2e}, {:.2e}'".format(*fString))

#Task Three
in_tuple = ()

def formatter(in_tuple):
    numbers = len(in_tuple)
    make_a_format_string = (f"the {numbers} are: ") + ", ".join(["{:d}"]*numbers)
    return(make_a_format_string).format(*in_tuple)

formatter(in_tuple)

#Task Four
og = ( 4, 30, 2017, 2, 27)

def sFormat(og):
    new_print = "{:02d} {} {} {:02d} {}".format(og[3], og[4], og[2], og[0], og[1])
    return new_print

print(sFormat(og))

#Task Five
fElements = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {fElements[0][:-1]} is {fElements[1]} and'
      f' the weight of a {fElements[2][:-1]} is {fElements[3]}')

print(f'The weight of an {fElements[0][:-1].upper()} is {fElements[1]*1.2} and'
      f' the weight of a {fElements[2][:-1].upper()} is {fElements[3]*1.2}')

#Task Six
headers = ('name', 'age', 'cost')
brackets = '{:10}{:<10}{}'
print(brackets.format(headers[0],headers[1],headers[2]))

dataFeed = [('Obi', 29, '$70.00'), ('Luke', 24, '$800.00'), ('Han', 25, '$1000.00'), ('Yoda', 21, '$20000.00')]
for data in dataFeed:
    for item in data:
        print(brackets.format(data[0], data[1], data[2]))
        break

if __name__ == '__main__':
    in_tuple = (1, 2, 3, 4, 5)
    assert formatter(in_tuple) == ('the 5 are: 1, 2, 3, 4, 5')