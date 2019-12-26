#!/usr/bin/env python3


def main():
    # test task_one function
    assert task_one() == "file_002 :   123.46, 1.00e+04, 1.23e+04"

    # test task_two function
    assert task_two() == "file_002 :   123.46, 1.00e+04, 1.23e+04"

    # test task_three function
    assert task_three((2, 3, 5)) == "the 3 numbers are: 2, 3, 5"
    assert task_three((2, 3, 5, 7, 9)) == "the 5 numbers are: 2, 3, 5, 7, 9"

    # test task_four function
    assert task_four() == "02 27 2017 04 30"

    # test task_five function
    assert task_five() == "The weight of an Orange is 1.56" \
        " and the weight of a Lemon is 1.32"

    # run task_six function (assert is impractical)
    task_six()

    # test task_six_point_one function
    assert task_six_point_one() == "    1    2    3    4    5" \
        "    6    7    8    9   10"


def task_one():
    t = (2, 123.4567, 10000, 12345.67)
    s = "file_{:03d} : {:8.2f}, {:.2e}, {:.2e}".format(*t)
    return s


def task_two():
    t = (2, 123.4567, 10000, 12345.67)
    s = f"file_{t[0]:03d} : {t[1]:8.2f}, {t[2]:.2e}, {t[3]:.2e}"
    return s


def task_three(t):
    s = "the {} numbers are: ".format(len(t))
    s += ", ".join(["{:d}"] * len(t)).format(*t)
    return s


def task_four():
    t = (4, 30, 2017, 2, 27)
    s = "{3:02d} {4:d} {2:d} {0:02d} {1:d}".format(*t)
    return s


def task_five():
    # doesn't handle 'a' vs 'an'
    li = ['oranges', 1.3, 'lemons', 1.1]
    s = f"The weight of an {li[0][:-1].capitalize()} is {li[1]*1.2}" \
        f" and the weight of a {li[2][:-1].capitalize()} is {li[3]*1.2}"
    return s


def task_six():
    # define list of users
    users = [
            {
                "name": "Matthew",
                "age": 25,
                "cost": 123.45
            },
            {
                "name": "Mark",
                "age": 42,
                "cost": 1234.56
            },
            {
                "name": "Luke",
                "age": 38,
                "cost": 12345.67
            },
            {
                "name": "John",
                "age": 107,
                "cost": 123456.78
            }
         ]
    # print nicely formatted table
    print("{:>10} | {:>5} | {:>15}".format("Name", "Age", "Cost"))
    print("{:->36s}".format(""))
    for user in users:
        s = "{:>10} | {:>5} | {:>15,.2f}".format(
                user["name"], user["age"], user["cost"])
        print(s)


def task_six_point_one():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return ("{:>5}" * len(t)).format(*t)


if __name__ == "__main__":
    main()
