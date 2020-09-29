#!/usr/bin/env python3
#Task One - format string

"file_%.03d: %.2f, %.2e, %.2e" % ( 2, 123.4567, 10000, 12345.67) 

#Task Two - format string using .format()

f = 2
flnm = 123.4567
intr = 10000
flnm2 = 12345.67
seq = (f, flnm, intr, flnm2)
"file_{:>03d}: {:.2f}, {:.2e}, {:.2e}".format(*seq)

#Task Three - Dynamically Building up formating strings

nums = [1,2,3,4]
l = len(nums)
#"the {} numbers are: ".format(l)+", ".join(["{}"]*l).format(*nums)
#or
("the {} numbers are: "+", ".join(["{}"]*l)).format(l, *nums)

def display_seq(nums):
    l = len(nums)
    print(("the {} numbers are: "+", ".join(["{}"]*l)).format(l, *nums))

#Task Four - string formating 

seq = ( 4, 30, 2017, 2, 27)
def print_a_tuple(seq):
    result = (seq[-2:]+seq[2:3]+seq[0:1]+seq[1:2])
    print(("{:>02d}, {}, {}, {:>02d}, {}").format(*result))

#Task Five - f-strings

list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {list[0].upper()} is {list[1]} and the weight of a {list[2].upper()} is {list[3]}")

#Task Six - string formating table

data = [
    [ "Jhon Whitehouse", 19, "$3000"],
    [ "Michael Mot", 21, "$10000"],
    [ "Steve Warner", 30, "$4000"],
    [ "David Brown", 25, "$4500"],
    [ "Vicky Benz", 27, "$3700"],
]
row = "|{name:<20s}|{age:2d}|{income:6s}|".format
for i in data:
    print(row(name=i[0],age=i[1],income=i[2]))
