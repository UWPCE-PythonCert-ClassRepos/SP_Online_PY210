import sys
# Donor dict
donar_list = [
    ("Mike", [200, 150, 50]),
    ("Tony", [150, 50, 250]),
    ("Sarah", [150, 150, 150]),
]


# send thanks funct
def send_thanks():
    while True:
        selection = input(
            "Please enter a Full Name, enter 'list' to see a list of current donors, or quit to exit: ")

        if selection == "list":
            print('\n'.join(donar_list))
        elif selection.lower() == "quit":
            return
        else:
            new_donate = float(
                input("\nHow much would you like to donate: \n"))
            if selection in donar_list:
                donar_list[selection].append(new_donate)
            else:
                donar_list[selection] = [new_donate]
            print(f"\nThank you {selection} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                  "Sincearly,\n\n"
                  "A low paid intern\n")
            break

# making a sortable list


def sorting_function(dictionary):
    temp_list = []
    for keys, values in dictionary.items():
        temp_list.append([sum(values), keys, len(
            values), sum(values)/len(values)])
    return sorted(temp_list, reverse=True)
# creating a report


def create_report():
    temp_donar_list = sorting_function(donar_list)
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0, len(temp_donar_list)):
        print(
            f"{temp_donar_list[i][1]:<21} ${temp_donar_list[i][0]:>12.2f}{temp_donar_list[i][2]:>11}  ${temp_donar_list[i][3]:>12.2f}")

# writing thank you to all donors function


def mass_send_thanks():
    for donor in donar_list:
        with open(f"{donor}.txt", "w+") as letter:
            letter.write(f"\nThank you {donor} for your donation of ${sum(donar_list[donor]):.2f}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                         "Sincearly,\n\n"
                         "A low paid intern\n")
    print("\nSending out thank you letters\n")


# Menu dict
menu = {
    "s": send_thanks,
    "c": create_report,
    "sa": mass_send_thanks,
    "q": sys.exit
}

# Script
if __name__ == '__main__':
    while True:
        prompt = input(
            "What would you like to do?:\n"
            "s - Send a thank you\n"
            "c - Create a report\n"
            "sa - Send a thank you to all donors\n"
            "q - Quit\n")
        if prompt.lower() in ["s", "c", "sa", "q"]:
            menu[prompt.lower()]()
        else:
            print("\nPlease enter s, c, sa or q\n")
