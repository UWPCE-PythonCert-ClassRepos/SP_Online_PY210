#!/usr/bin/env python3

#Task One

s = "file_{:0>3d} :  {:.2f}, {:.2e}, {:.2e}"

print(s.format( 2, 123.4567, 10000, 12345.67))

#Task Two
file = 2
num1 = 123.4567
num2 = 10000
num3 = 12345.67

print(f"file_{file:0>3d} :  {num1:.2f}, {num2:.2e}, {num3:.2e}")

#Task Three
#"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

def formatter(in_tuple):
    l = len(in_tuple)
    form_string = "the {} numbers are: " + ",".join(["{}"]*l)
    return form_string.format(l,*in_tuple)


print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))


#Task Four
def task_four(tup):
    new_string = "{:0>2d}, {}, {}, {:0>2d}, {}"
    return new_string.format(tup[3], tup[4], tup[2], tup[0], tup[1])

print(task_four((4, 30, 2017, 2, 27)))
#'02 27 2017 04 30'

#Task Five

test_list = ['oranges', 1.3, 'lemons', 1.1]

#The weight of an orange is 1.3 and the weight of a lemon is 1.1
print(f'''The weight of an {(test_list[0][:-1]).upper()} is {(test_list[1]) *1.2} and the weight of a {(test_list[2][:-1]).upper()} is {(test_list[3])*1.2}''')


#Task 6
def align_test(item):
    print("{:^15} {:^10} {:^15}".format("Name", "Age", "Cost"))
    for x in item:
        print("{:^15} {:^10} {:^15}".format(*x))

align_test((('Eric', 45, '$100'), ('Vivie', 4, "$1,000"), ('Jack', 1,'$10,000'),('Christina', 42, '$10')))

#bonus: given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns 
#that are 5 charaters wide? It can be done on one short line!

tup_ex = (1,2,3,4,5,6,7,8,9,10)
print(''.join([f"{i:^5}" for i in tup_ex]))


