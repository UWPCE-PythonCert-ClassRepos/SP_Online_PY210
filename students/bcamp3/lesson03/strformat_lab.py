#!/usr/bin/env python3

"""
String Formatting Lab

"""

"""
Task One
"""
print('\n----------\n Task One\n----------\n')

a = ( 2, 123.4567, 10000, 12345.67)

s = f'file_{a[0]:03d} : {a[1]:8.2f}, {a[2]:8.2e}, {a[3]:8.2e}'

print(s)

"""
Task Two
"""
print('\n----------\n Task Two\n----------\n')

s = 'file_{:03d} : {:8.2f}, {:8.2e}, {:8.3g}'.format(*a)

print(s)

"""
Task Three
"""
print('\n----------\n Task Three\n----------\n')

t = (1,2,3)

f1 = 'the 3 numbers are:'
f2 = [' {:d}']
print((f1+','.join(f2*len(t))).format(*t))

def formatter(seq):
    f1 = f'the {len(seq)} numbers are:'
    f2 = [' {:d}']
    return (f1+','.join(f2*len(seq))).format(*seq)

t = (4, 5, 6, 7, 8, 9)
print(formatter(t))

"""
Task Four
"""
print('\n----------\n Task Four\n----------\n')
t = ( 4, 30, 2017, 2, 27)

print('{3:02d} {4:} {2:} {0:02d} {1:}'.format(*t))

"""
Task Five
"""
print('\n----------\n Task Five\n----------\n')
a = ['oranges', 1.3, 'lemons', 1.1]

s = f"The weight of an {a[0].rstrip('s')} is {a[1]}" \
    f" and the weight of a {a[2].rstrip('s')} is {a[3]}"

print(s) 
print()

s = f"The weight of an {(a[0].rstrip('s')).upper()} is {a[1]*1.2:.1f}" \
    f" and the weight of a {(a[2].rstrip('s')).upper()} is {a[3]*1.2:.1f}"

print(s)

"""
Task Six
"""
print('\n----------\n Task Six\n----------\n')
origins = ['England','Scotland','New Zealand','Washington','Oregon','Moon']
ages = [10, 12, 4, 8, 1, 4530000000]
prices = [7.99, 11.63, 20.74, 9.43, 0.49, 10453.15]

labels = ['Origin','Age','Price']
units = ['','(years)','(per pound)']
header_fmt = ' {:^12} | {:^12}| {:^12}' 
print('  -----------  Fine Cheeses  -----------\n')
print(header_fmt.format(*labels))
print(header_fmt.format(*units))
print('_'*42)
for i,_ in enumerate(origins):
    print(f" {origins[i]:12} |{ages[i]:>12} |{f'${prices[i]:.2f}':>12}")
print('_'*42)
print()

a = (1,2,3,4,5,6,7,8,9,10)
n_cols = 7
for i in a: print(f'{i:5d}'*n_cols)

