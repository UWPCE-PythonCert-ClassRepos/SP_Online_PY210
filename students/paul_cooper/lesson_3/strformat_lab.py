#Task 1
tup = (2, 123.4567, 10000, 12345.67)
formatter = "'file_{0:03d} : {1:.2f}, {2:.2e}, {3:.2e}'"
print(formatter.format(*tup))

#Task 2
print("'file_%.3i : %.2f, %.2e, %.2e'" % tup)

#Task 3
t = (1, 2, 3, 4, 5, 6)
def formatter(t):
	l = len(t)
	old_formatter = ('the {} numbers are: '+', '.join(['{}'] * l)).format(l, *t)
	return old_formatter
print(formatter(t))

#Task 4
tup2 = ( 4, 30, 2017, 2, 27)
tup_to_list = list(tup2)
first2 = tup_to_list[0:2]
last2 = tup_to_list[-2:]
tup_to_list[0:2] = last2
tup_to_list[-2:] = first2
print("'"+' '.join(str(x).zfill(2) for x in tup_to_list)+"'")

#Task 5
fruit_W = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {fruit_W[0][:-1].upper()} is {fruit_W[1]*1.2} \
and the weight of a {fruit_W[2][:-1].upper()} is {fruit_W[3]*1.2}')

#Task 6
person1 = ['Tom', '32', '$35']
print('{:20}{:10}{:>10}'.format('Tom', '34','$9.01'))
print('{:20}{:10}{:>10}'.format('Sally','23', '$99.01'))
print('{:20}{:10}{:>10}'.format('Mike','60', '$999.01'))
print('{:20}{:10}{:>10}'.format('Charlie','30', '$9999.01'))
print('{:20}{:10}{:>10}'.format('Bill','20', '$2399.34'))
print('{:20}{:10}{:>10}'.format('Phill','60', '$24.78'))


#Print tuple of 10 numbers in pne line
# This is the only way I can think to print them in one line, it would be much
# easier with a for loop but that would requiare more than one line
tup_of_10 = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(tup_of_10[0:5], '\n' , tup_of_10[5:10])
