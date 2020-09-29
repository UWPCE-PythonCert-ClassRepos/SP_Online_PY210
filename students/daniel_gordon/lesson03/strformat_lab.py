#Task One
example = (2, 123.4567, 10000, 12345.67)
f_string = f"file_{example[0]:03} : {example[1]:9.2f}, {example[2]:.2e}, {example[3]:.2e}"
print(f_string)

#Task Two
print("file_{:0>3} :    {:.2f}, {:<.2e}, {:^.2e}".format(*example))

#Task Three
values = list(range(6))
f_string = "the {:d} numbers are : " + ", ".join(["{:d}"]*len(values))
print(f_string.format(len(values), *values))