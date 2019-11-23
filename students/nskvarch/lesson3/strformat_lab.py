#!/usr/bin/env python3
#The Sring formatting lab exercise, created by Niels Skvarch

#part 1
a_tuple = (2, 123.4567, 10000, 12345.67)

formatted_tuple = "file_{:03d}: {:.2f}, {:.2e}, {:.3g}".format(a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3])
print(formatted_tuple)


#part 2
formatted_tuple2 = f'file_{a_tuple[0]:03d}: {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.3g}'
print(formatted_tuple2)


#part 3
def formatter(in_tuple):
    """Takes an input in the form of a tuple and re-formats the values then displays the new format"""
    formatted_tuple3 = []
    for i in in_tuple:
        formatted_tuple3.append("{:d}")
    new_tuple3 = ", ".join(formatted_tuple3)
    print("the {} numbers are: {}".format(len(in_tuple), new_tuple3.format(*in_tuple)))
test_a = (2,3,5)
test_b = (2,3,5,7,9)
formatter(test_a)
formatter(test_b)


#part 4
a_tuple4 = (4, 30, 2017, 2, 27)
print("{3:02d} {4:02d} {2:02d} {0:02d} {1:02d}".format(a_tuple4[0], a_tuple4[1], a_tuple4[2], a_tuple4[3], a_tuple4[4]))


#part 5
a_tuple5 = ["oranges", 1.3, "lemons", 1.1]
print(f'The weight of an {a_tuple5[0][:-1]} is {a_tuple5[1]} and the weight of a {a_tuple5[2][:-1]} is {a_tuple5[3]}.')
print(f'The weight of an {a_tuple5[0][:-1].upper()} is {a_tuple5[1]*1.2} and the weight of a {a_tuple5[2][:-1].upper()} is {a_tuple5[3]*1.2}.')


#part 6
a_list6 = []
a_list6.append(["Danny", 23, "$275.99"])
a_list6.append(["Marcus", 45, "$1,034.75"])
a_list6.append(["Johnson", 138, "$15,999.00"])

for i in a_list6:
    print('{:15}{:>10}{:>15}'.format(*i))

a_tuple6 = tuple(range(10))
print(("{:<5}"*len(a_tuple6)).format(*a_tuple6))



