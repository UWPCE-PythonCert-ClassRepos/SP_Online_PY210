# Task 1
a_tuple = (2, 123.4567, 10000, 12345.67)

file_name = a_tuple[0]
ele2 = a_tuple[1]
ele3 = a_tuple[2]
ele4 = a_tuple[3]

print(f"file_{file_name:03} :    {ele2:.2f}, {ele3:.2e}, {ele4:.3g}")

# Task 2
print("file_{:03} :    {:.2f}, {:.2e}, {:.3g}".format(file_name, ele2, ele3, ele4))

# Task 3
def formatter(in_tuple):
    tup_length = len(in_tuple)

    build_string = "the {} numbers are: {}" + (", {}" * (tup_length - 1))

    return build_string.format(tup_length, *in_tuple[:])

# Task 4
tup_5 = (4, 30, 2017, 2, 27)

zero = tup_5[0]
one = tup_5[1]
two = tup_5[2]
three = tup_5[3]
four = tup_5[4]

print(f"{three:02} {four} {two} {zero:02} {one}")

# Task 5
list4 = ['oranges', 1.3, 'lemons', 1.1]

fruit = list4[0]
weight = list4[1]
fruit2 = list4[2]
weight2 = list4[3]

print(f"The weight of an {fruit[:-1]} is {weight} and the weight of a {fruit2[:-1]} is {weight2}")

print(f"The weight of an {fruit[:-1].upper()} is {weight * 1.2} and the weight of a {fruit2[:-1].upper()} is {weight2 * 1.2}")

# Task 6
row1 = ['Larry', 23, 190.00]
row2 = ['Sabine', 12, 4500.00]
row3 = ['Katy', 89, 42.50]
row4 = ['Ben', 6, 10500.23]

table = [row1, row2, row3, row4]

for row in table:
    print("{:20}{:^20}{:>20.2f}".format(*row[:]))

# come back and finish task 6 extra