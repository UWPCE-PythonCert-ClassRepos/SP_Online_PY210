import sys
import mailroom_OO


def create_report(donor_list_variable):
    listy = mailroom_OO.DonorCollection(donor_list_variable).sorting_function()
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0, len(listy)):
        print(f"{listy[i][1]:<21} ${listy[i][0]:>12.2f}{listy[i][2]:>11}  ${listy[i][3]:>12.2f}")


def send_thanks(donor_list_variable, query="empty_1", new_donate="empty_2"):
    while True:
        if query == "empty_1":
            query = input("Please enter a Full Name, enter 'list' to see a list of current donors, or quit to exit: ")
        if query == "list":
            print(mailroom_OO.DonorCollection(donor_list_variable).list_donors())
            break
        elif query.lower() == "quit":
            break
        else:
            if new_donate == "empty_2":
                while True:
                    try:
                        new_donate = float(input("\nHow much would you like to donate: \n"))
                        break
                    except ValueError:
                        print("\nPlease enter a number in numerical form\n")
            else:
                if query in donor_list:
                    mailroom_OO.DonorCollection(donor_list_variable).update_donor(query, new_donate)
                else:
                    mailroom_OO.DonorCollection(donor_list_variable).add_donor(query, new_donate)
                return print(mailroom_OO.Donor(donor_list[query], query))


def save_file_prompt(chosen_dict):
    chosen_file = input("Saving file as: \n")
    mailroom_OO.FileHandling(chosen_file).save_file(chosen_dict)


def mass_send_thanks(dictionary):
    mailroom_OO.DonorCollection(dictionary).mass_send_thanks()


def quit_now(arg):
    sys.exit()

# Menu dict
menu = {
    "A": send_thanks,
    "B": create_report,
    "C": mass_send_thanks,
    "D": save_file_prompt,
    "E": quit_now
}

# Script
if __name__ == '__main__':
    donor_list={}
    answer = input("Would you like to import a donor file? \n").upper()
    if answer == "YES":
        while True:
            file_name = input("What is the filename?\n")
            if file_name.upper() == "QUIT":
                break
            data = mailroom_OO.FileHandling(file_name).open_file()
            if data == "file not found":
                print(data,", please try again")
            else:
                donor_list.update(eval(data))
                break
    while True:
        prompt = input(
            "What would you like to do?:\n"
            "A - Send a thank you\n"
            "B - Create a report\n"
            "C - Send a thank you to all donors\n"
            "D - Save the new donor list\n"
            "E - Quit\n")
        try:
            menu[prompt.upper()](donor_list)
        except KeyError:
            print("\nPlease enter A, B, C or D\n")