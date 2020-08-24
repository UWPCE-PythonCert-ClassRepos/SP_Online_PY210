import os
filename = os.path.basename(__file__)
_string = [(2, 123.4567, 100000, 12345.67, 98765.4321000), (6, 12.3333, 4444.1, 123.321),
           (10, 321.3121, 11.2, 9876543.1), (3, 3213.2222, 222.123, 3.123)]


def task_one():
    temp_list = []
    for i in _string:
        item = "00000" + str(i[0])
        temp_list.append(item)
    _sort = temp_list.sort()
    for i in temp_list:
        print(f"{filename}{i[]} {i[1:]}")

    # Works
    # task_one()

    def task_two():
        temp_list = []
        for i in _string:
            item = "00000" + str(i[0])
            temp_list.append(item)
        _sort = temp_list.sort()
        for i in temp_list:
            print(f"{filename}{i[0]}{i[1:]}")

    # Works
    # task_two()


def task_three(in_tuple):
    t = []
    for i in range(in_tuple):
        t.append(i)
    _tuple = tuple(t)
    print(
        f"There are {len(_tuple)} items in the tuple: {_tuple}")

# Works
# task_three(51)


def task_four():
    _tuple = (1231, 23, 64, -2, .1, 34, 304)
    _sorted_tuple = sorted(_tuple)
    print(_sorted_tuple)

# Works
# print(task_four())


_list = ['orange', 1.3, 'lemon', 1.1]


def task_five():
    print(
        f"The weight of an {_list[0]} is {_list[1]}, while the weight of a {_list[-2]} is {_list[-1]}")
    print(
        f"The weight of an {str(_list[0]).title()} is {int(_list[1]) * 1.2}, while the weight of a {str(_list[-2]).title()} is {int(_list[-1]) * 1.2}")

# Works
# task_five()


_dict = [["fruit", 2.55, "yes", 1], ["car", 15000, "yes", 10],
         ["house", 355000, "yes", 20], ["boat", 32500, "no", 5], ["book", 15, "no", 2]]


def task_six():
    row = "| {item:<16s} | {price:<0f} | {necessary:<3s} | {lifespan:<2f}".format
    for i in _dict:
        print(row(item=i[0], price=i[1], necessary=i[2], lifespan=i[3]))


task_six()
