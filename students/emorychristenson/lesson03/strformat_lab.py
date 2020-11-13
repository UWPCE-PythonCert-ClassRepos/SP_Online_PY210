#!/usr/bin/env python3

# Task 1
n = (2, 123.4567, 10000, 12345.67)

string = "file_{:03d} : {:05.2f}, {:.2e}, {:.2e}".format(*n)
print(string)

# Task 2

string = f"file_{n[0]:03} : {n[1]:.2f}, {n[2]:.2e}, {n[3]:.2e}"
print(string)

# Task 3
n = (1, 2, 3, 4, 5)
def formatted(n):
    l = len(n)
    string = ("the {} numbers are: " + ", ".join(["{}"]*l)).format(l,*n)
    print(string)
    return

formatted(n)

# Task 4

n = (4,30,2017,2,27)
string = f'{n[3]:02}, {n[4]}, {n[2]}, {n[0]:02}, {n[1]}'
print(string)

# Task 5

e = ['orange', 1.3, 'lemon', 1.1]

print(f"The weight of an {e[0]} is {e[1]} and the weight of a {e[2]} is {e[3]}")
print(f"The weight of an {e[0].upper()} is {e[1] * 1.2} and the weight of a {e[2].upper()} is {e[3] * 1.2}.")

# Task 6
things = [
        ("John", 27, 4200.42),
        ("Jacob", 50, 3020),
        ("Jingleheimer", 12, 275.60),
        ("Schmidt", 8, 1000.45),
    ]
for thing in things:
    print(f"{thing[0]:^12} {thing[1]:^10d} ${thing[2]:06.2f}")

# Extra Task

print(("{:5d}" * 10).format(*range(10)))
