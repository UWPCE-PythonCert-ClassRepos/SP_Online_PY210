#!/usr/bin/env python

"""
The Mailroom assignment.

The data is a global list.

Appending donations was repetitive, so was made into its own function 'add_donations()'

As the assignment becomes more complex, parts may be broken into separate functions.
"""

import sys

# This was originally a list of lists.  I changed it based on the recommendation in the notes.
data = [('Bob', [17.56]), ('Billy', [500.00, 1000.00]), ('Joe Schmoe', [2.00, 0.03, 45.00]), ('This Guy', [1.00, 100000]), ('That Gal', [9876.54])]

# Generate a list of names to make looping easier.
Name_List = []
for item in data:
    Name_List.append(item[0])

prompt = """\nPlease choose between the following option numbers:
(enter the digit only)
'1' - Send a Thank You
'2' - Create a Report
'3' - Quit
: """

# This was originally a single function called 'Part1()' which called another function to add
# donations.  It worked, but I restructured it based on the recommendation in the notes.
def main():
    while True:
        action = input(prompt)
        if action == '1':
            Send_Thank_You(data)
        elif action == '2':
            Create_a_Report(data)
        elif action == '3':
            Quit_Program()


def Send_Thank_You(data):
    Full_Name = 'list'
    while Full_Name == 'list':  # loop if 'list' is provided
        Full_Name = input("""Please provide a full name (case sensitive).
                          'list will show the list of donor names.
                          'quit' exits script.
                          : """)
        if Full_Name == 'quit':  # exit option, break while loop
            Quit_Program()
        if Full_Name == 'list':
            print('\n\n')
            for item in Name_List:
                print(item)
    if Full_Name not in Name_List:  # Add name to original data, and list of names
        data.append((Full_Name, []))
        Name_List.append(Full_Name)
        name_num = -1  # pass index number
        data, don_sum = add_donations(name_num, data)  # call function to add donation info
    elif Full_Name in Name_List:  # Select name already on list
        name_num = Name_List.index(Full_Name)  # pass index number
        data, don_sum = add_donations(name_num, data)  # call function to add donation info
    print("\n\nHi {},\n\nThank you for your total donation of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".format(Full_Name, don_sum))


def Create_a_Report(data):
    Report_List = []  # create empty dataset for reporting
    for i in range(len(data)):  # start populating dataset in accordance with the original data
        num_don = len(data[i][1])  # number of donations
        Report_List.append([Name_List[i], num_don])
        sum_individual = 0
        for j in range(len(data[i][1])):
            sum_individual += data[i][1][j]  # build sum of donations per individual
        Report_List[i].append(sum_individual)
        if num_don != 0:
            Report_List[i].append(sum_individual / num_don)  # determine average donation
        else:
            Report_List[i].append(sum_individual)  # prevent division by zero

    def sort_total(val):  # define key for sorting
        return val[2]
    Report_List.sort(key=sort_total, reverse=True)  # sort by descending sum of donations
    print("\n\n {:^28}|{:^18s}|{:^7s}|{:^18s}".format('Donor Name', 'Total Given($)', '# Gifts', 'Average Gift($)'))
    print("-" * 75)
    for j in range(len(Report_List)):
        print(" {:28s}|{:17,.2f} |{:6d} |{:>18,.2f}".format(Report_List[j][0], Report_List[j][2], Report_List[j][1], Report_List[j][3]))


def Quit_Program():
    print('\n\ngoodbye\n\n')
    sys.exit()


def add_donations(A_name_num, A_data):  # function that adds donation info
    A_donation = ''
    A_don_sum = 0
    while A_donation != 'none':
        # query for amount, with option for no donation or exit parent function
        A_donation = input("Please provide the donation amount (enter 'none' for no donation \
                           'quit' to exit script): ")
        if A_donation == 'quit':
            Quit_Program()
        if A_donation != 'none':
            A_data[A_name_num][1].append(float(A_donation))  # add individual donation to original data
            A_don_sum += float(A_donation)  # keep sum of donations
    return A_data, A_don_sum  # return the updated original data and the sum of donations


if __name__ == "__main__":
    main()


