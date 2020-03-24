#!/usr/bin/env python3

## TASK 1 ##
string = 'file_{:03d} : {:05.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67)
print(string)

## TASK 2 ##
a = 2
b = 123.4567
c = 10000
d = 12345.67

string2 = f'file_{a:03} : {b:.2f}, {c:.2e}, {d:.2e}'
print(string2)

## TASK 3 ##
seq = (1,2,3)

def formatter(seq):
    l = len(seq)
    string3 = ("the {} numbers are: " + ", ".join(["{}"]*l)).format(l,*seq)
    return string3

## TASK 4 ##
tup4 = (4,30,2017,2,27)
string4 = f'{tup4[3]:02}, {tup4[4]}, {tup4[2]}, {tup4[0]:02}, {tup4[1]}'
print(string4)

## TASK 5 ##
list5 = ['orange', 1.3, 'lemon', 1.1]
string5 = f'The weight of an {list5[0]} is {list5[1]} and the weight of a {list5[2]} is {list5[3]}'
string5plus = f'The weight of an {list5[0].upper()} is {list5[1]*1.2} and the weight of a {list5[2].upper()} is {list5[3]*1.2}'
print(string5)
print(string5plus)

## TASK 6 ##
## example string '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
tab1 = '{:20}{:20}{:>20}'.format('John Smith', 38,'$88.09')
tab2 = '{:20}{:20}{:>20}'.format('Jack Baker', 9,'$1002.43')
tab3 = '{:20}{:20}{:>20}'.format('Jimmy Johnson', 59,'$322.83')
print(tab1)
print(tab2)
print(tab3)

# Bonus task
tup6 = (1,2,3,4,5,6,7,8,9,10)
string6 = (", ".join(["{:5}"]*10)).format(*tup6)
print(string6)