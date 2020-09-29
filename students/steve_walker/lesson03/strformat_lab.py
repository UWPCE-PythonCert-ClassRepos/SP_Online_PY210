#!/usr/bin/env python3

a_tuple = (2, 123.4567, 10000, 12345.67)

# Task One
print("file_{:03d} :  {:.2f}, {:.2e}, {:.2e}".format(*a_tuple))

# Task Two
filenumber, float2pts, int2sci, float2sci = "{:03d}".format(a_tuple[0]), "{:.2f}".format(a_tuple[1]), "{:.2e}".format(a_tuple[2]), "{:.2e}".format(a_tuple[3])
print(f"file_{filenumber} :  {float2pts}, {int2sci}, {float2sci}")

# Task Three
def formatter(in_tuple):
	in_tuple= (len(in_tuple),) + in_tuple
	form_string = "the {:d} numbers are: " + "{:d}, "*(len(in_tuple)-2) + "{:d}"
	return(form_string.format(*in_tuple))

formatter((1, 2, 3, 4, 77))

# Task Four
t4 = (4, 30, 2017, 2, 27)
first, fourth = "{:02d}".format(t4[3]), "{:02d}".format(t4[0])
print(f"{first} {t4[4]} {t4[2]} {fourth} {t4[1]}")

# Task Five
t5 = ["oranges", 1.3, "lemons", 1.1]
print(f"The weight of an {t5[0][:-1]} is {t5[1]} and the weight of a {t5[2][:-1]} is {t5[3]}")
print(f"The weight of an {t5[0][:-1].upper()} is {t5[1]*1.2} and the weight of a {t5[2][:-1].upper()} is {t5[3]*1.2}")

# Task Six
t6 = ("Benny John", 32, 4.99), ("Rhianna", 31, 100000.06), ("Gorpy", 7, 3003.82)
for i in t6:
	print("{0:<12} {1:>5} {2:>12}".format(*i))

t6x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
print((("{:<5}") * len(t6x)).format(*t6x))
