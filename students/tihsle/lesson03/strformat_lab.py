#!/usr/bin/env python3

tuple = (2, 123.4567, 10000, 12345.67)

# One
print("One\n")
print("file_{:03d} :  {:.2f}, {:.2e}, {:.2e}".format(*tuple))

# Two
print("\nTwo\n")
fn = "{:03d}".format(tuple[0])
float1 = "{:.2f}".format(tuple[1])
sci = "{:.2e}".format(tuple[2])
float2 = "{:.2e}".format(tuple[3])
print(f"file_{fn} :  {float1}, {sci}, {float2}")

# Three
print("\nThree\n")
def formatter(in_tuple):
	# add the length to the front of the tuple
	in_tuple = (len(in_tuple),) + in_tuple
	form_string = "the {:d} numbers are: " + "{:d}, "*(len(in_tuple)-2) + "{:d}"
	return(form_string.format(*in_tuple))

print(formatter((2, 3, 5, 7, 9)))

# Task Four
print("\nFour\n")
tuple = (4, 30, 2017, 2, 27)
pos1 = "{:02d}".format(tuple[3])
pos4 = "{:02d}".format(tuple[0])
print(f"{pos1} {tuple[4]} {tuple[2]} {pos4} {tuple[1]}")

# Task Five
print("\nFive\n")
tuple = ["oranges", 1.3, "lemons", 1.1]

print(f"The weight of an {tuple[0][:-1]} is {tuple[1]} and the weight of a {tuple[2][:-1]} is {tuple[3]}")

print(f"The weight of an {tuple[0][:-1].upper()} is {tuple[1]*1.2} and the weight of a {tuple[2][:-1].upper()} is {tuple[3]*1.2}")

# Task Six
print("\nSix\n")
tuple = ("Tom Thomas", 30, 325.23), ("Benny Jet", 42, 9000.24), ("Timmy", 7, 10.95)
for item in tuple:
	print("{:<20} {:>3} {:>10}".format(*item))

newtuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print((("{:<5}") * len(newtuple)).format(*newtuple))
