#!/usr/bin/env python3

# string formatting exercises


def main():
    print(task_one())
    print(task_two())
    print(formatter((2, 3, 5, 7, 9))) #task three
    print(task_four())
    task_five()
    task_six()


def task_one(file_tuple=None):
    '''
    given a tuple, produce a specific string using string formatting
    :return: formatted string
    '''
    if file_tuple is None:
        file_tuple = (2, 123.4567, 10000, 12345.67)
    return "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(file_tuple[0], file_tuple[1], file_tuple[2], file_tuple[3])


def task_two(file_tuple=None):
    '''
    given a tuple, produce a specific string using string formatting
    :return: f-string
    '''
    if file_tuple is None:
        file_tuple = (2, 123.4567, 10000, 12345.67)
    return f"file_{file_tuple[0]:03} : {file_tuple[1]:{8}.{5}}, {file_tuple[2]:.2e}, {file_tuple[3]:.2e}"



def formatter(in_tuple):
    '''
    dynamically build format string to reflect tuple size in output
    :return: formatted string
    '''
    l = len(in_tuple)
    # return ("the {} numbers are: " + ", ".join(["{}"] * l)).format(l, *in_tuple)
    return f"the {l} numbers are: {', '.join(str(num) for num in in_tuple)}"


def task_four(file_tuple=None):
    '''
    use index numbers from tuple to specify positions in print formatting
    :return: f-string
    '''
    if file_tuple is None:
        file_tuple = (4, 30, 2017, 2, 27)
    return f"{file_tuple[3]:02} {file_tuple[4]} {file_tuple[2]} {file_tuple[0]:02} {file_tuple[1]}"


def task_five():
    '''
    create f-string that displays "The weight of an orange is 1.3 and the weight of a lemon is 1.1" from a provided list
    :return: None
    '''
    fruit_weight = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {fruit_weight[0][:-1]} is {fruit_weight[1]} and the weight of a {fruit_weight[2][:-1]} is {fruit_weight[3]}")
    print(f"The weight of an {fruit_weight[0][:-1].upper()} is {fruit_weight[1] * 1.2} and the weight of a {fruit_weight[2][:-1].upper()} is {fruit_weight[3] * 1.2}")
    return None


def task_six():
    '''
    print a table of several rows, each with a name, an age and a cost
    :return: None
    '''
    scotch = ["Glenmorangie", "Balvenie Single Malt", "Macallan Lalique", "Glenfiddich", "Ardbeg"]
    ages = ["18 years", "50 years", "62 years", "30 years", "10 years"]
    price = ["$130.00", "$50,000.00", "$47,285.00", "$799.00", "$90.00"]

    print(f"SCOTCH:{'':<30}AGE:{'':<20}PRICE:{'':>20}")
    for scotch, age, price in zip(scotch, ages, price):
        print(f"{scotch:<30}{age:^20}{price:>17}")
    return None


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)