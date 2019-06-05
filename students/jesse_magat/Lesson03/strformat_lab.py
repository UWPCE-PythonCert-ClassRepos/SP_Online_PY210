#Task1
print('Task 1')
sample = (2,123.4567,10000,12345.67)
output = 'file_{:03d}: {:.2f}, {:.2e}, {:.2e}'.format(*sample)
print(output)


#Task2

print('Task 2')
sample2 = (2,123.4567,10000,12345.67)
x = 'file_{:03d}:'.format(sample2[0])
x1 = '{:.2f},'.format(sample2[1])
x2 = '{:.2e},'.format(sample2[2])
x3 = '{:.2e}'.format(sample2[3])

output2 = f"{x} {x1} {x2} {x3}"

print(output2)

#Task 3

print('Task 3')
t = (1,2,3)
l = len(t)
output3 = ("the {} numbers are: "+", ".join(["{}"]*l)).format(l,*t)

print(output3)

#Task 4
print('Task 4')
sample3 = (4,30,2017,2,27)

y = '{:02d} '.format(sample3[0])
y1 = '{} '.format(sample3[1])
y2 =  '{} '.format(sample3[2])
y3 = '{:02d} '.format(sample3[3])
y4 = '{} '.format(sample3[4])

output4 = f"{y3} {y4} {y2} {y} {y1}"
print(output4)


#Task 5

print('Task 5')
sample4 = ['oranges',1.3,'lemons',1.1]

print(f"The weight of an {sample4[0].upper()[:-1]} is {sample4[1]} and the weight of a {sample4[2].upper()[:-1]} is {sample4[3]}")

#Task 6

print('Task 6')

column_names = ['Name', 'Age','Cost']
emp_list = [['Employee1', 33, 25000],['Employee2',45,50000]]
format1 = "{:12}" + "{:12}" + "{:5}"
format2= "{:10}" + "{:5}" + "{:14}"
l = len(emp_list)
print(format1.format(*column_names))
for i in range(l):
	print(format2.format(*emp_list[i]))
	






