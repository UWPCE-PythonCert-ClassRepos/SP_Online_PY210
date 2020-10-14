### Lesson_3 - String Format

### Task 1 ###
""" Origignal - ( 2, 123.4567, 10000, 12345.67) """
""" Desired - 'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
print("\nTask 1:\n")
print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))

###Task 2###
""" Alternate Method """
print("\nTask 2:\n")
alternate = (2, 123.4567, 10000, 12345.67)

def sorted(lst):
    return "file_{0:03d}:      {1:.2f}, {2:.2e}, {3:.2e}".format(lst[0],lst[1],lst[2],lst[3])
print(sorted(alternate))

###Task 3 ###
"""In [20]: formatter((2,3,5))"""
"""Out[20]: 'the 3 numbers are: 2, 3, 5'"""

"""In [21]: formatter((2,3,5,7,9))"""
"""Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'"""

print("\nTask 3:\n")
def formatter(in_tuple):
    fstring = ""
    for _ in range(0, len(in_tuple)):
        fstring += '{:d}, '
    return fstring.format(*in_tuple)[:-2]

print(formatter((1, 2, 3)))

### Task 4 ###
"""Given a 5 element tuple:"""
"""( 4, 30, 2017, 2, 27)"""
"""use string formating to print:"""
"""'02 27 2017 04 30'"""

print("\nTask 4:\n")
t = ( 4, 30, 2017, 2, 27)

print("{:02d} {} {} {:02d} {}".format(t[3],t[4],t[2],t[0],t[1]))


### Task 5 ###
""" Provided ['oranges', 1.3, 'lemons', 1.1] """
""" Produce 'The weight of an orange is 1.3 and the weight of a lemon is 1.1' """

print("\nTask 5:\n")

orange = ("orange", 1.3)
lemon = ("lemon",1.1)

print(f'The weight of an {orange[0]} is {orange[1]} and the weight of a {lemon[0]} is {lemon[1]}')

""" Modify f-string to display the names of the fruit in upper, and weight 20 percent higher"""

print(f'\nThe weight of an {orange[0].upper()} is {orange[1] * 1.2} and the weight of a {lemon[0].upper()} is {lemon[1] * 1.2}')

### Task 6 ###
""" Format """
print("\nTask 6:\n")
items = [("BMW M3", 2004, 18988.00),
         ("Mercedes AMG", 2018, 94508.99),
         ("Audi S8", 2007, 62000.00),
         ("Lexus GS400", 1998, 15849.99)]

for item in items:
    print("|Name: {0:15} | Age: {1:5} | Price: {2:10}|\n".format(*item))

print(' '.join(('%*s' % (5, i) for i in range(10))))
