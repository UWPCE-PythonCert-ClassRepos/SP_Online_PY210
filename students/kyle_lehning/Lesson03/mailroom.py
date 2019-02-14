#!/usr/bin/env python3


def menu_input():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Quit\n"
    )


def print_report(seq):
    w = [max(len(str(row[i])) for row in seq) for i in range(len(seq[0]))]
    for row in seq:
        row_string = "{0:>{w1}}{1:>{w2}}{2:>{w3}}{3:>{w4}}".format(*row, w1=w[0]+2, w2=w[1]+2, w3=w[2]+2, w4=w[3]+2)
        print(row_string)


if __name__ == '__main__':
    donors = [
        ["Bill Gates", 653784.49, 2, 326892.24],
        ["Mark Zuckerberg", 16396.10, 3, 5465.37],
        ["Jeff Bezos", 877.33, 1, 877.33],
        ["Paul Allen", 708.42, 3, 236.14],
        ["Steve Jobs", 1002.40, 2, 501.20]
    ]
    while True:
        user_selection = menu_input()
        if user_selection == "1":
            pass
        if user_selection == "2":
            print_report(donors)
        if user_selection == "3":
            break

