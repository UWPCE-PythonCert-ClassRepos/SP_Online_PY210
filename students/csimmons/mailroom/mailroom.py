#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py
# Created 11/23/2020 - csimmons

# data table
 #[donor, gifts]

donorlist = [ 
    ['Craig Simmons', 10000, 2500, 300],
    ['Allen McConnell', 3000, 6000, 750, 20000],
    ['Martin Acevedo', 2000, 5000],
    ['Sutton Keaney', 24500, 500, 3000, 5000, 1000],
    ['David Basilio', 750, 750, 750, 750, 5000, 750, 750],
    ['Andrew McLaughlin', 2500, 500, 40000, 50],
    ['Hussein Saffouri', 1000, 1000, 2100, 7000, 55000] 
    ]
#print(mailroom_data1)
def mailroom(donorlist):
    new_donors =[]
    slicer = []
    cash_only = []
    for i in range(len(donorlist)):
        print((donorlist[i][0]))
        new_donors.append(donorlist[i][0])
        cash_only.append(new_donors[i])
        slicer.append(donorlist[i])
        #new_donors.append(donorlist[len(donorlist)-1][0])
        #print(donorlist[len(donorlist)-1][0])
    print(new_donors)
    print(slicer)
    print(cash_only)
    
mailroom(donorlist)

#single_row = "\n" + ("|{{i}:<10,.2f}" * len(numbers)).format(*numbers)
'''
print(donorlist[0][0])
print(donorlist[1][0])
print(donorlist[2][0])
print(donorlist[0][3])
print(donorlist[1][2])
print(donorlist[2][2])
print(donorlist[0][3])
print(donorlist[1][1])
print(donorlist[2][1])

    new_fruits = []
    for fruit in fruits:
        new_fruits.append(fruit[::-1])
    print(new_fruits)


listoflists.append((list(a), a[0]))
    name = "\n" + "| {0:<20s} |".format     {1:<} | {age:<5d} | ${price:<10,.2f} |".format
    single_row = "\n" + ("|{{i}:<10,.2f}" * len(numbers)).format(*numbers)

x = "{0:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(*datetime))
row = "| {0:<20s} | {1:<} | {age:<5d} | ${price:<10,.2f} |".format

print(data)
def test(seq):
    replacer = '{:d}, '
    make_fstring = 'The {:d} numbers are: ' + (replacer * len(seq))
    full = '"' + make_fstring[:-2] + '."'
    print(full.format(len(seq), *seq))

x = "{0:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(*datetime))

row = "| {0:<20s} | {1:<} | {age:<5d} | ${price:<10,.2f} |".format
for data in table_data:
    print(row(fname=data[0], lname=data[1], age=data[2], price=data[3]))

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
single_row = "\n" + ("|{:^5d}" * len(numbers)).format(*numbers)
print(single_row + "|\n")
'''