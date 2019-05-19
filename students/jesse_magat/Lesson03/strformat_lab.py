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


