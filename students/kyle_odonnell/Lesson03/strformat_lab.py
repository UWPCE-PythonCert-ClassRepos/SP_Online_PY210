
# Task One
seq = (2, 123.4567, 10000, 12345.67)

x = '{}{:03}:   {:.2f}, {:.2e}, {:.2e}'.format("file_", seq[0], round(seq[1], 2), seq[2], seq[3])
print("Task 1:", x)


# Task Two
a = '{}{:03}'.format("file_", seq[0])
b = round(seq[1], 2)
c = format(seq[2], ".2e")
d = format(seq[3], ".2e")

e = f'{a}:   {b}, {c}, {d}'
print("Task 2:", e)


# Task Three
t = (1, 2, 3)


def formatter(in_tuple):
    form_string = "The {:d} numbers are: " + (",".join(["{}"] * len(in_tuple)))
    return form_string.format(len(in_tuple), *in_tuple)


print("Task 3:", formatter(t))


# Task Four
tup_two = (4, 30, 2017, 2, 27)
answer = '02 27 2017 04 30'

tup_formatted = '{3:02} {4:d} {2:d} {0:02} {1:d}'.format(*tup_two)
print("Task 4:", tup_formatted)


# Task Five
fruit = ['oranges', 1.3, 'lemons', 1.1]
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

fruit_string = f"The weight of an {fruit[0]} is {fruit[1]} and the weight of a {fruit[2]} is {fruit[3]}"
print("Task 5:", fruit_string)


# Task Six
'{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')

row = "{name:<5s} \t {age:>5d} {price:>10.2f}".format
x = [["Bob", 45, 10.00], ["Mary", 29, 1000.99], ["Max", 50, 1030.98]]
print("Task 6:")
for i in x:
    print(row(name=i[0], age=i[1], price=i[2]))


