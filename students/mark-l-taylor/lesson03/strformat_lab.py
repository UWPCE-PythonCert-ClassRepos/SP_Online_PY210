#!/usr/bin/env python3
#
#Task 1
#
################################
print('Task 1')

tuple_to_format = ( 2, 123.4567, 10000, 12345.67)
print('Tuple to format: {}\n'.format(tuple_to_format))

print('Formated:')
print('file_{:03d} :{:>9.2f},{:>9.2e},{:>9.2e}'.format(*tuple_to_format))

#
#Task 2
#
#################################

print('\n\nTask 2')

print('\nAlernate print with a format string:')
f_string = 'file_{:03d} :{:>9.2f},{:>9.2e},{:>9.2e}'
print(f_string.format(*tuple_to_format))

print('\nUsing Keywords:')
id,first,second,third = tuple_to_format
print(f'file_{id:03d} :{first:>9.2f},{second:>9.2e},{third:>9.2e}')

#
#Task 3
#
##################################

print('\n\nTask 3')
# Rewrite the following to accept an arbitrary number of values
#"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

def formatter(in_tuple):
    print(in_tuple)
    form_string = 'the {} numbers are: ' + ','.join(len(in_tuple) * [' {:d}'])
    return form_string.format(len(in_tuple),*in_tuple)

print('formatter examples:')
print(formatter((1,2,3)))
print(formatter(range(5,15,2)))

#
#Task 4
#
###################################

print('\n\nTask 4')

t = (4, 30, 2017, 2, 27)

print('using indices:')
print('{:02d} {:02d} {:02d} {:02d} {:02d}'.format(t[3],t[4],t[2],t[0],t[1]))
print('using variables:')
t0,t1,t2,t3,t4 = t
print(f'{t3:02d} {t4:02d} {t2:02d} {t0:02d} {t1:02d}')

#
#Task 5
#
###################################

print('\n\nTask 5')

f1,w1,f2,w2 = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {f1} is {w1} and the weight of a {f2} is {w2}')
print('Make fruit uppercase and increase weight 20%:')
print(f'The weight of an {f1.upper()} is {w1*1.2} and the weight of a {f2.upper()} is {w2*1.2}')

#
#Task 6
#
####################################

print('\n\nTask 6')

header = ['Name','Age','Cost']
data = [['John',25,'$500.00'],
        ['Jane',42,'$10,000.00'],
        ['George',89,'8,456.00'],
        ['Elizabeth',14,'$10.67']]

form_table = '{:<12}{:>4}{:>15}'
print(form_table.format(*header))
for d in data:
    print(form_table.format(*d))
    
print('Extra task, print tuple in column 5 characters wide')
t = tuple(range(10))
print(('\n'.join(len(t) * ['{:5}'])).format(*t))


