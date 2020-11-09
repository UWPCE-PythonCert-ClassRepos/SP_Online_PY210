tup = (2, 123.4567, 10000, 12345.67)
print('TASK 1')
# Creates formatted string
str1 = 'file_{:0>3} :\t{:.2f}, {:.2e}, {:.3g}'.format(tup[0], tup[1], tup[2], tup[3])
str2 = f'file_{tup[0]:03} :\t{tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.3g}'
print(str1)

print('TASK 2')
print(str2)

print('TASK 3')
def formatter(tup):
    str3 = f'the {len(tup)} numbers are: '
    for num in tup:
        str3 = str3 + (f'{int(num)}, ')
    return str3
print(formatter(tup))

print('TASK 4')
five_tup = (4, 30, 2017, 2, 27)
str4 = f'{five_tup[3]:02} {five_tup[4]:02} {five_tup[2]:02} {five_tup[0]:02} {five_tup[1]:02}'
print(str4)

print('TASK 5')
ls = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {ls[0][:-1]} is {ls[1]} and the weight of a {ls[2][:-1]} is {ls[3]}')
print(f'The weight of an {ls[0][:-1].upper()} is {ls[1]*1.2} and the weight of a {ls[2][:-1].upper()} is {ls[3]*1.2}')

print('TASK 6')
tup = ('Alex', 27, 20, 'Seth', 26, 300, 'Randall', 101, 5000)
# printing Aligned Header
print(f"{'Name' : <10}{'Age' : ^10}{'Cost' : ^10}")
for i in range(0,len(tup),3):
    print(f"{tup[i] : <10}{tup[i+1] : ^10}{tup[i+2] : ^10}")
