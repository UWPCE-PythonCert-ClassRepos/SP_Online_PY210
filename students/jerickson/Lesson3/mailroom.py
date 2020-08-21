donation_data_header = ["Name", "Total Given", "Num Gifts", "Average Gift"]
donation_data = [
    ("Usama Black", 10101, 3),
    ("Malachy Krause", 4242, 1),
    ("Kezia Hassan", 3023, 3),
    ("Lyla Moody", 580, 1),
    ("Pamela Guerra", 32, 2),
    ("Bob Barker", 1, 1),
]


def report():
    # Format report lines
    title = donation_data_header[:]
    report_header = f"|{title[0]:^16}|  {title[1]:^12}|{title[2]:^13}|  {title[3]:^13}|"
    report_break_list = []
    for char in report_header[:]:
        break_char = "+" if char == "|" else "-"
        report_break_list.append(break_char)
    report_break = "".join(report_break_list)
    report_length = len(report_break)
    report_end = "-" * report_length
    report_title = "|{{:^{:d}}}|".format(report_length - 2).format("Donor Report")

    # Print report Title and Header
    print(report_end)
    print(report_title)
    print(report_break)
    print(report_header)

    # Print Donor Records
    for donor in donation_data:
        print(report_break)
        donor_average = int(donor[1] / donor[2])
        donor_string = f"|{donor[0]:^16}| ${donor[1]:>12.2f}|{donor[2]:^13d}| ${donor_average:>13.2f}|"
        print(donor_string)
    print(report_end)


if __name__ == "__main__":
    print("\nBack to the grind in the mailroom.", end="\n\n")
    report()
