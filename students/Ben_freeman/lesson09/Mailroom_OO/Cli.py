import sys
import mailroom_OO
import ast


def create_report(donors_variable):
    listy = donors_variable.sorting_function()
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0, len(listy)):
        print(f"{listy[i][1]:<21} ${listy[i][0]:>12.2f}{listy[i][2]:>11}  ${listy[i][3]:>12.2f}")


def send_thanks(donors_variable, query="empty_1", new_donate="empty_2"):
    while True:
        if query == "empty_1":
            query = input("Please enter a Full Name, enter 'list' to see a list of current donors, or quit to exit: ")
        if query == "list":
            print(donors_variable.list_donors())
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
                if query in donors_variable.donors:
                    donors_variable.update_donor(query, new_donate)
                else:
                    donors_variable.add_donor(query, new_donate)
                for items in donors_variable.donors:
                    if donors_variable.donors[items].name == query:
                        return print(donors_variable.donors[items].message())


def data_handler(dictionary):
    return [mailroom_OO.Donor(v,k) for k,v in dictionary.items()]


def save_file_prompt(donors_variable):
    chosen_file = input("Saving file as: \n")
    mailroom_OO.FileHandling(chosen_file).save_file(donors_variable)


def mass_send_thanks(donors_variable):
    donors_variable.mass_send_thanks()


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
    donor_dict={}
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
                donor_dict.update(ast.literal_eval(data))
                break
    donors = mailroom_OO.DonorCollection(data_handler(donor_dict))
    while True:
        prompt = input(
            "What would you like to do?:\n"
            "A - Send a thank you\n"
            "B - Create a report\n"
            "C - Send a thank you to all donors\n"
            "D - Save the new donor list\n"
            "E - Quit\n")
        try:
            menu[prompt.upper()](donors)
        except KeyError:
            print("\nPlease enter A, B, C or D\n")