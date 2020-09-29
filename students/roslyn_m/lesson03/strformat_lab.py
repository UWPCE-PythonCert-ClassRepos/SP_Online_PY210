# Title: Str Lab
# Dev: Roslyn Melookaran
# Date: 9/15/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/15/20, created script)
# --------------------------------------------------------------


def formatter(string, touple):
    """ enable dynamically built string formatting.
              :param: string (starter string)
              :param: tuple (tuple that will drive the number of variables to be formatted into string)
              :return: string (returns the end elongated string)
              """
    count = len(touple)
    string = "the " + str(count) + " numbers are: "
    for i in range(count):
        if i == (count - 1):
            string = string + "{:d}"
        else:
            string = string + "{:d}, "
    return string


# -------TASK 1--------#
t = (2, 123.4567, 10000, 12345.67)
print('file{:0>3}: {:.2f}, {:.2e}, {:.3g}'.format(t[0], t[1], t[2], t[3]))
print('file{:0>3}: {:.2f}, {:.2e}, {:.3g}'.format(*t))  # Trimmed down version

# -------TASK 2--------#
print(f"file{t[0]:0>3}: {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3g}")

# -------TASK 3--------#
x = (1, 2, 3, 5, 6)
final_string = ""
print(formatter(final_string, x).format(*x))

# -------TASK 4--------#
y = (4, 30, 2017, 2, 27)
string = "{:0>2} {} {} {:0>2} {}"
print(string.format(y[3], y[4], y[2], y[0], y[1]))

# -------TASK 5--------#
# Here’s a task for you: Given the following four element list:
fruit_lst = ['orange', 1.3, 'lemon', 1.1]
fruit1 = fruit_lst[0]
weight1 = fruit_lst[1]
fruit2 = fruit_lst[2]
weight2 = fruit_lst[3]
fruit_str = f"The weight of the {fruit1} is {weight1} and the weight of the {fruit2} is {weight2}"
print(fruit_str)
# Now with fruit in upper case, and the weight 20% higher.
fruit_str2 = f"The weight of the {fruit1.upper()} is {weight1 * 1.2} and the weight of the {fruit2.upper()} is {weight2 * 1.2}"
print(fruit_str2)

# -------TASK 6--------#
print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))
person1 = {'name': "john", 'age': 24, 'cost': 13.53}
person2 = {'name': "jane", 'age': 28, 'cost': 1400}
person3 = {'name': "smith", 'age': 87, 'cost': 100000}
person4 = {'name': "carol", 'age': 54, 'cost': 1353}
table_str = f'{person1["name"]:20} {person1["age"]:20} {person1["cost"]:20}' + \
            '\n' + f'{person2["name"]:20} {person2["age"]:20} {person2["cost"]:20}' + \
            '\n' + f'{person3["name"]:20} {person3["age"]:20} {person3["cost"]:20}' + \
            '\n' + f'{person4["name"]:20} {person4["age"]:20} {person4["cost"]:20}'
print(table_str)
z = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}' * 10).format(*z))
