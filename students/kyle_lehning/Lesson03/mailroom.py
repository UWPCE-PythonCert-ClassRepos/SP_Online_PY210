#!/usr/bin/env python3
donors = [
    ["Steve Jobs", 1002.40, 2, 501.20],
    ["Jeff Bezos", 877.33, 1, 877.33],
    ["Bill Gates", 653784.49, 2, 326892.24],
    ["Mark Zuckerberg", 16396.10, 3, 5465.37],
    ["Paul Allen", 708.42, 3, 236.14]
]


def menu_input():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Quit\n"
    )


def list_donors():
    for name in donors:
        print(name[0])


def add_donor(new_name):
    donors.append([new_name, 0, 0, 0])
    return donors[-1]


def add_donation(donor, donation_value):
    donor[2] += 1
    donor[1] += float(donation_value)
    donor[1] = round(donor[1], 2)
    donor[3] = round(donor[1]/donor[2], 2)


def print_report():
    header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    header_string = "{0:<{w1}} | {1:>{w2}} | {2:>{w3}} | {3:>{w4}}"
    data_string = "{0:<{w1}}  ${1:>{w2}}   {2:>{w3}}  ${3:>{w4}}"
    report_list = donors[:]
    width_list = donors[:]
    report_list.sort(reverse=True, key=lambda x: int(x[1]))
    width_list.insert(0, header)
    w = find_widths(width_list)
    header_to_print = print_line(header_string, header, w)
    print(header_to_print)
    print('-' * len(header_to_print))
    for row in report_list:
        print(print_line(data_string, row, w))


def find_widths(seq):
    return [max(len(str(row[i])) for row in seq) for i in range(len(seq[0]))]


def print_line(line_format, info, width):
    row_string = (line_format.format(*info, w1=width[0], w2=width[1], w3=width[2], w4=width[3]))
    return row_string


def main():
    while True:
        user_selection = menu_input()
        if user_selection == "1":
            while True:
                user_selection = (
                    input("\nPlease provide a full name to send thank you note to (options 'list' and 'menu'): ")
                )
                if user_selection.upper() == 'MENU':
                    break
                if user_selection.upper() == 'LIST':
                    list_donors()
                    continue
                for name in donors:
                    if user_selection.upper() == name[0].upper():
                        current_donor = name
                        break
                else:
                    current_donor = add_donor(user_selection)
                donation_amount = input("\nHow much did {} donate?: ".format(user_selection))
                add_donation(current_donor, donation_amount)
        if user_selection == "2":
            print_report()
        if user_selection == "3":
            break


if __name__ == '__main__':
    main()
