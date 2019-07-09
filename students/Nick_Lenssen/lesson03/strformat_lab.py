#!/usr/bin/env python3

def formatter(my_tup):
	l = len(my_tup)
	out_tup = ", ".join(["{:^5}"]*l)
	return ('the {} numbers are: '+out_tup).format(l, *my_tup)

tup = (2,123.4567,10000,12345.67)
tup_2 = (1,12,2,3,3333,5,6,12,1,23)
list_1 = ['oranges', 1.3, 'lemons', 1.1]

print ('file{:>03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))

print (f'file00{round(tup[0],2)} : {tup[1]:.2f}, {tup[2]:.2E}, {tup[3]:.2E}')

print (formatter(tup))

print ("0{3} {4} {3} 0{0} {1}".format(4, 30, 2017, 2, 27))

print (f'The weight of an {list_1[0].upper()} is {list_1[1]} and the weight of a {list_1[2]} is {list_1[3]*1.2}')

table_data = [
    ['First', '99.011', 'Second', '88.1'],
    ['First', '99.000001', 'Second', '88.0011'], 
    ['First', 'b98.5004', 'Second', '88.0001']
]
for row in table_data:
    print("{} {: >20} {: >20} {: >20}".format(*row))

print ("".join(["{:{width}}"]*10).format(10, *tup_2, width = '5'))

