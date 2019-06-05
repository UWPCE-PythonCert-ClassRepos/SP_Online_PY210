

super_tuple = ( 2, 123.4567, 10000, 12345.67)

# Task One
print('file{:0>3}: {:06.2f} {:.2E} {:.2E}'.format(super_tuple[0], super_tuple[1], super_tuple[2], super_tuple[3]))
print ("Hello, I am {} years old !".format(18))

# Task Two
second_super_tuple = ( 253, 123.4567, 10000, 12345.67)
print('file{:03X}: {:0>14} {:06.2f} {:2E}'.format(second_super_tuple[0], second_super_tuple[1], second_super_tuple[2], second_super_tuple[3]))

print(f"Hello, {second_super_tuple[0]:0>4}. You are {second_super_tuple[1]:0>14}.")

# Task Three
simple_dimple = (1, 2, 3, 4, 5)
def formatter(in_tuple):
    l = len(in_tuple)
    i = 0
    mylist = []
    while i < l:
        mylist.append("{:d}")
        i += 1
    string_form = ', '.join(mylist)
    new_out =  "the {} numbers are {}".format(l, string_form)
    super_new_out = new_out.format(*in_tuple)
    return super_new_out
print(formatter((2, 3, 5, 7, 88, 55)))

# Task Four
scruple = (4, 30, 2017, 2, 27)
scruple_out = "{3:0>2} {4:0>2} {2:0>2} {0:0>2} {1:0>2}".format(*scruple)
print(scruple_out)

# Task Five
list = ['oranges', 1.3, 'lemons', 1.1]

f'The weight of an {list[0][:-1]} is {list[1]} and the weight of a {list[2][:-1]} is {list[3]}'
f'The weight of an {list[0][:-1].upper()} is {list[1] * 1.2} and the weight of a {list[2][:-1].upper()} is {list[3] * 1.2}'

# Task Six
list = [["Fred", "26", "59.99"], ["Tammy", "33", "799.95"], ["Mike", "104", "1000.50"], ["Dr Evil", "49", "1000000.01"]]
for row in list:
 print('{:20}{:10}{:8}'.format(*row))

# Extra task
mytup = tuple(range(1,11))
print(("{:5d}" * 10).format(*mytup))


