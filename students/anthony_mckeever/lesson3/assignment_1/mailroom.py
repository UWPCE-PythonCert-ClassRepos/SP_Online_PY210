"""
Programming In Python - Lesson 3 Assignment 1: Mailroom Part 1
Code Poet: Anthony McKeever
Start Date: 07/30/2019
End Date: 08/01/2019
"""

menu_opts = ["main", "return", "stop"]
quit_opts = ["exit", "end", "quit"]
list_opts = ["list", "l", "ls"]
help_opts = ["help", "h", "?"]

donors_list = [("Cresenta Starchelle", [99.99, 6000.00, 10345.23, 29.99]),
               ("Delilah Matsuka", [199.99, 299.99, 2100.00]),
               ("Astra Matsume", [599.99]),
               ("Kima Metoyo", [3600.00, 1200.00]),
               ("Kayomi Matsuka", [0.01]),
               ("Katie Starchelle", [600.00])]

stay_on = True


def main():
    """
    The main loop of the script.  Prompts user with a main menu.
    """
    print("\nStudio Starchelle Donor Appreciation System\n")
    while stay_on:
        print_menu()
        user_choice = input("What do you want to do? > ")
        handle_main_choice(user_choice.lower())


def set_stay_on(val):
    """
    Set the value of the stay_on global variable.

    :val:   The Boolean value to set the stay_on variable to.
    """
    global stay_on
    stay_on = val


def print_menu():
    """
    Print the main menu.
    """
    help_cmds = ", ".join(help_opts)
    quit_cmds = ", ".join(quit_opts)
    print("--- Main Menu ---\n"
          "\nAvailable Options:\n"
          "\t\"Send A Thank You\"\tGet prepopulated email template to thank a donor.\n"
          "\t\"Create a Report\"\tView a list of all donors and their cumulative donations.\n"
          f"\t\"{quit_cmds}\"\tQuit the script.  Can be used at any input prompt.\n"
          f"\t\"{help_cmds}\"\t\tView the script's help text and additional commands.\n"
         )


def handle_main_choice(user_choice):
    """
    Handle the user choice from the main menu input promt.

    :user_choice:   The str().lower value of the user's input selection.
    """
    if user_choice in help_opts:
        print_help()
    elif user_choice == "create a report":
        create_report()
    elif user_choice == "send a thank you":
        send_thanks()
    elif user_choice in quit_opts:
        set_stay_on(False)
    else:
        print("\nUnknown command.\n"
              "Type \"help\" to get all options.\n")


def print_help(from_main=True):
    """
    Print the help text for the handle_main_choice or send_thanks functions.

    :from_main: A boolean value that determins whether or not this function was called from handle_main_choice. (Default = True)
    """
    help_cmds = ", ".join(help_opts)
    quit_cmds = ", ".join(quit_opts)
    menu_cmds = ", ".join(menu_opts)
    list_cmds = ", ".join(list_opts)

    if from_main:
        print("\nStudio Starchelle Donor Appreciation System\n"
              "\nA basic system for thanking donors for thier generous contributions.\n"
              "\nCommand List:\n"
              f"\t{help_cmds}\t\tPrints this help text.\n"
              f"\t{menu_cmds}\tReturn to the main menu.\n"
              f"\t{quit_cmds}\t\tExit the entire script.\n"
             )
        input("\n--- Press the Enter/Return Key to return to Main ---\n")
    else:
        print( "\nCommand List:\n"
              f"\t{help_cmds}\t\tPrint this help text.\n"
              f"\t{list_cmds}\t\tList all of the known donors\n"
               "\tDonor Name\t\tSelects a donor to thank for their contributions.\n"
               "\t\t\t\tSelecting an unknown donor will prompt to add them.\n"
              f"\t{menu_cmds}\tReturn to the main menu.\n"
              f"\t{quit_cmds}\t\tExit the entire script."
             )
    

def send_thanks():
    """
    Function for acepting donations and thanking donors.
    """
    print("\nLets send thanks!")
    thanking = True
    while thanking:
        user_choice = input("\nWho do you want to thank? > ")
        thanking = thank_handle_choice(user_choice)


def thank_handle_choice(user_choice):
    """
    Handle the user's choice from the send_thanks input prompt.
    Parameter, user_choice, should be passed to the function as is to preserve the user's capitolization.
    This function will handle the str.lower()    
    :user_choice:   The as-is instance of the user's choice.
    """
    if user_choice.lower() in list_opts:
        print("\nList of Donors:")
        for donor in donors_list:
            print("\t" + donor[0])
        return True

    elif user_choice.lower() in menu_opts:
        return False

    elif user_choice.lower() in quit_opts:
        set_stay_on(False)
        return False

    elif user_choice.lower() in help_opts:
        print_help(from_main=False)
        return True

    else:
        donor = get_donor(user_choice)
        
        donation_float = 0.0
        while donation_float <= 0.0:
            donation = input("How much did they donate? > ")

            if donation in menu_opts:
                return False
            elif donation in quit_opts:
                set_stay_on(False)
                return False

            donation_float = float(donation)
            if donation_float <= 0.0:
                print("Invalid amount.  Try again.")

        donor[1].append(donation_float)
        print_email(donor[0], donation_float)
        return False


def print_email(name, donation):
    """
    Print the thank you email to the console.

    :name:      The name of the donor.
    :donation:  The donation amount that was recieved from the donor.
    """
    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")
    print("Studio Starchelle - A Fizzworks Studios Company\n"
          "123 Starshine Ln.\n"
          "Suite 200\n"
          "New Sophiesville, WA, 99999\n"
          "StudioStarchelle@fakeemail.com\n\n"
         f"Dear {name},\n"
         f"\tThank you for your generous donation of ${donation:.02f} to our organization, Studio Starchelle.\n"
          "This kind offering will help us grow and expand the creative operations at Fizzworks\n"
          "Studios as well as finance the creation of new and exciting stories.\n\n"
          "\tYour donation gives you access to exclusive content from the Starchelle*Project universe.\n"
          "To view this content, please visit https://www.*********.com/donors and create an account using\n"
          "the code STARCHELLE1234.\n\n"
          "\tThank you once again for your kind donation.  With your help, we'll be able to make our next\n"
          "graphic novel, Starchelle*Project: Shooting Star, a reality!\n\n"
          "Sincerely,\n\n"
          "Sophia McKeever")
    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")


def get_donor(user_choice):
    """
    Return the donor entry for the selected.  Creates a donor and appends them to donor_list if they do not exist.

    :user_choice:   The user's donor selection.
    """
    for donor in donors_list:
        if user_choice.lower() == donor[0].lower():
            return donor
    donor = (user_choice,[])
    donors_list.append(donor)
    return donor


def create_report():
    """
    Display a table of donors, the total amount they've donated, the count of their donations, and the average donation.
    """
    donor_summary = get_donor_summary()
    header = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    lengths = get_lengths(donor_summary, header)
    table = []

    sep_strings = [("-" * (lengths[0] + 2)), ("-" * (lengths[1] + 2)), ("-" * (lengths[2] + 2)), ("-" * (lengths[3] + 2))]
    sep_line = "|" + "+".join(sep_strings) + "|"
    for item in sorted(donor_summary, key=sort_key, reverse=True):
        table.append(format_line(item, lengths))
        table.append(sep_line)

    # Beautify report.
    report_name = "Donor Report"
    table.insert(0, "\n|" + "-" * (len(sep_line) - 2) + "|")
    table.insert(1, f"|{report_name:^{len(sep_line) -2}}|")
    table.insert(2, sep_line)
    table.insert(3, format_line(header, lengths, is_donor=False))
    table.insert(4, sep_line)

    print("\n".join(table) + "\n")


def sort_key(item):
    """
    The key to sort donors by.
    """
    return item[1]


def get_donor_summary():
    """
    Return a summary of all donors including their name, total donation sum, count of donations, and average donation.
    """
    donor_summary = []
    for donor in donors_list:
        name = donor[0]
        total_donations = sum(donor[1])
        count_donations = len(donor[1])
        average_donation = total_donations / count_donations
        donor_summary.append([name, total_donations, count_donations, average_donation])
    return donor_summary


def format_line(item, lengths, is_donor=True):
    """
    Return a formatted string that will fit in the donor summary table.

    :item:      The sequence of data to format.
    :lengths:   The lengths for each field of the table.
    :is_donor:  A boolean value determining whether or not the :item: is a donor.  (Default = True)
    """
    if is_donor:
        total = f"${item[1]:.02f}"
        avg = f"${item[3]:.02f}"
        return f"| {item[0]:<{lengths[0]}} | {total:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {avg:>{lengths[3]}} |"
    return f"| {item[0]:<{lengths[0]}} | {item[1]:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {item[3]:>{lengths[3]}} |"


def get_lengths(seq, header):
    """
    Return a list of the max lengths for all fields of the donor summary.
    
    :seq:       A list donor summary entries to get the lengths from.
    :header:    The header for the table to set the initial lengths to.
    """
    name_len = len(header[0])
    total_len = len(header[1])
    count_len = len(header[2])
    avg_len = len(header[3])
    
    for item in seq:
        total = f"${item[1]:.02f}"
        count = str(item[2])
        avg = f"${item[3]:.02f}"

        name_len = len(item[0]) if len(item[0]) > name_len else name_len
        total_len = len(total) if len(total) > total_len else total_len
        count_len = len(count) if len(count) > count_len else count_len
        avg_len = len(avg) if len(avg) > avg_len else avg_len

    return [name_len, total_len, count_len, avg_len]


if __name__ == "__main__":
    main()
