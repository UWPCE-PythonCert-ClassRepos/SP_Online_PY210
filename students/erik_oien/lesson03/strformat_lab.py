#!/usr/bin/env python3

# Task 1

print("file_00{}: {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))

# Task 2

file_name = 2
v1 = 123.4567
v2 = 10000
v3 = 12345.67

print(f"file_00{file_name}: {v1:.2f}, {v2:.2e}, {v3:.2e}")

# Task 3

t = (1,2,3)

def formatter(t):
    l = len(t)
    form_string = ("the {} numbers are: " + ", ".join(["{}"] * l))
    return form_string.format(l, *t)
  
print(formatter(t))
print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))

# Task 4

t = (4, 30, 2017, 2, 27)
organized_t = (t[-2:]+t[2:3]+t[:2])
print(("{:>02d} {} {} {:>02d} {}").format(*organized_t))

# Task 5

info_list = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {info_list[0]} is {info_list[1]} and the weight of a {info_list[2]} is {info_list[3]}")
print(f"The weight of an {info_list[0].upper()} is {info_list[1] * 1.2} and the weight of a {info_list[2].upper()} is {info_list[3] * 1.2}")

# Task 6

data = [
    ["Erik", 36, "$100"],
    ["Michelle", 32, "$10,000"],
    ["Patrick", 34, "$3000"]
]

def row_formatter(row):
    return "|name: {:10}|age: {:2}|cost: {:7}|".format(*row)

for row in data:
    print(row_formatter(row))

# Task 6 addtional problem

t10 = (13, 41, 71, 1, 19, 92, 60, 78, 3, 58)

for i in t10: print(f"|{i:5}|")