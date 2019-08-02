#! /usr/bin/env python3


def main():
    a_tuple = (2, 123.4567, 10000, 12345.67)
    print("'file_{:03d} :    {:.2f}, {:.2e}, {:.2e}'".format(
        a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3]))

    # Task Two
    print(
        f"'file_{a_tuple[0]:03d} :    {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}'")

# Task Three


def formatter(in_tuple):
    form_string = "'The {} numbers are: ".format(len(in_tuple))
    form_string += (len(in_tuple) - 1) * "{:d}, " + "{:d}'"
    return form_string.format(*in_tuple)

# Task Four


def formatter3(test_tuple):
    print("'{:02d} {} {} {:02d} {}'".format(test_tuple[3], test_tuple[4], test_tuple[2],
                                            test_tuple[0], test_tuple[1]))


def fruit_weight(weights):
    print(f"The weight of an {weights[0][:-1]} is {weights[1]} and  the weight of a {weights[2][:-1]} is {weights[3]}")
    print(f"The weight of an {weights[0][:-1].upper()} is {weights[1]*1.2} and  the weight of a {weights[2][:-1].upper()} is {weights[3]*1.2}")


if __name__ == '__main__':
    main()
    formatter((1, 2, 3, 4, 5, 6))
    formatter3((4, 30, 2017, 2, 27))
    fruit_weight(['oranges', 1.3, 'lemons', 1.1])
