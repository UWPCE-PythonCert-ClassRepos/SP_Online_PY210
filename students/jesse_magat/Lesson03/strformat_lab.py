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

sample3 = (4,30,2017,2,27)

y = '{:02d} '.format(sample3[0])
y1 = '{} '.format(sample3[1])
y2 =  '{} '.format(sample3[2])
y3 = '{:02d} '.format(sample3[3])
y4 = '{} '.format(sample3[4])

output4 = f"{y3} {y4} {y2} {y} {y1}"
print(output4)







