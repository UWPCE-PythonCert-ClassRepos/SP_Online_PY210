# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:14:26 2020

@author: miriam
"""

# Task one
print('file_''{:03d} :''  {:.2f},'' {:.2e},'' {:.2e}'"'".format(2, 123.4567, 10000, 12345.67))

# Task two

print(f'file_{2:0>3d} :  ' f'{123.4567:.2f}, '  f'{10000:.2e}, '  f'{12345.67:.2e}'"'")

# Task three
def formatter(in_tuple):
    l = len(in_tuple)
    format_string = ", ".join(["{}"]*l)
    return("'"+"the {} numbers are: "+format_string +"'").format(l, *in_tuple)

# Task four
print("0{3} {4} {2} 0{0} {1}".format(4, 30, 2017, 2, 27))

# Task five
L = ['orange', 1.3, 'lemon', 1.1]
print(f"The weight of an {L[0]} is {L[1]} and the weight of a {L[2]} is {L[3]}")
print(f"The weight of an {L[0].upper()} is {L[1]*1.2} and the weight of a {L[2].upper()} is {L[3]*1.2}")

# Task six
data = [
   ['Name', 'Age', 'Cost'],
   ['Miriam', 30, 30000.00],
   ['Waleed', 26, 1100.10],
   ['Dina', 32, 101.20],
   ['Ricardo', 36, 33.40]
   ]

row = "{:<8} {:<4} {:<8}".format

for p in data:
    print(row(p[0], p[1], p[2]))
    
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}' * len(tup)).format(*tup))
