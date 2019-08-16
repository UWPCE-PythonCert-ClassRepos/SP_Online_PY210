#!/usr/bin/env python3

"""
Programming In Python - Lesson 5 Assignment 1: Mailroom Part 3
Code Poet: Anthony McKeever
Start Date: 08/13/2019
End Date: 08/15/2019
"""
import os
import sys
import tempfile


def main():
    """
    The main loop of the script.  Prompts user with a main menu.
    """
    print("\nStudio Starchelle Donor Appreciation System\n")
    while True:
        menu_system(main_menu_dict, "\nMain Menu:", "\nWhat do you want to do? > ")


def safe_input(msg):
    """
    Return the input from the user or exit upon KeyboardInterupt or EOFError

    :msg:   The message for the input prompt
    """
    output = None
    try:
        output = input(msg)
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
        sys.exit()
    else:
        return output


def menu_system(opts_dict, menu_text, prompt_text, include_main=False, include_donors=False, invalid_opt=None):
    """
    The menu system that handles most user multiple choice inputs.

    :opts_dict:         The initial options dictionary.
    :menu_text:         The flavor text of the menu.
    :prompt_text:       What to prompt the user when accepting input.
    :include_main:      Whether or not to include options for returning to the main menu (Default = False)
    :include_donors:    Whether or not to include the donors with the options. (Default = False)
                        Note: Donors will not print when menu options are printed.
    :invalid_opt:       Override the action if the user provides an invalid selection. (Default = None)
                        Note: Using None will prompt user to reattemt their choice until a correct choice is made.
    """
    show_opts = opts_dict.copy()
    
    if include_main:
        show_opts.update(main_dict)

    show_opts.update(quit_dict)

    print(menu_text)
    print_options(show_opts)
    
    # Don't include the list of donors in the help text so the user has to request them.
    if include_donors:
        show_opts.update(donor_dict)

    while True:
        user_choice = safe_input(prompt_text)
        choice_key = key_from_lower(user_choice, show_opts.keys())

        if choice_key is not None:
            selection = show_opts[choice_key]

            if selection[1]:
                if selection[1] == accept_donation:
                    selection[1](choice_key)
                else:
                    selection[1]()
            
            if selection[1] != print_donors:
                break

        else:
            if invalid_opt is None:
                print("Invalid choice.  Please select from available options.")
            else:
                invalid_opt(user_choice)
                break


def print_options(show_opts):
    """
    Print the options from a menu.

    :show_opts:     The complete dictionary of the current menu's options.
    """
    skip = set([])
    for key, value in show_opts.items():
        if key not in skip:
            opts_string, skippable = get_opts_string(key, show_opts)
            print("\t" + opts_string + value[0])
            skip.update(skippable)
            

def key_from_lower(user_choice, keys):
    """
    Return the user's lower case input to a properly cased dictionary key.

    :user_choice:   The choice the user made at a menu.
    :keys:          The keys from the dictionary the user is choosing from.
    """
    lower_keys = {k.lower(): k for k in keys}
    return lower_keys[user_choice] if user_choice in lower_keys.keys() else None


def get_opts_string(key, dictionary):
    """
    Return a string for multiple keys where the value the key represents is duplicated in the dictionary and the keys
    that were combined in a list.
    
    :key:   The key in the dictionary to find duplicate values of.
    """
    keys = [k for k, v in dictionary.items() if v == dictionary[key]]
    return ", ".join(keys), keys


def print_donors():
    """
    Print a list of donors.
    """
    print("\nList of Donors:")
    for donor in donor_dict.keys():
        print("\t" + donor)

        
def send_thanks():
    """
    Initializes the menu system to prompt the acceptance of a donation and creation of a thank you letter.
    """
    menu_system(list_dict, "\n\nLets send thanks!", "\nWho do you want to thank? > ", include_main=True,
                include_donors=True, invalid_opt=accept_donation)


def accept_donation(donor_name):
    """
    Accept a new donation from a donor.

    :donor_name:    The donor who donated.
    """
    donor = get_donor(donor_name)

    donation_float = 0.0
    while donation_float <= 0.0:
        donation = safe_input("How much did they donate? > ")

        if main_or_exit(donation):
            return
        
        try:
            donation_float = float(donation)
        except ValueError:
            donation_float = 0.0
        finally:            
            if donation_float <= 0.0:
                print("Invalid amount.  Try again.")

    donor[0].append(donation_float)
    email = get_email(donor_name, donation_float)

    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")
    print(email)
    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")


def send__to_all():
    """
    Write text files with thank you letters for every donor.
    """
    default_dir = tempfile.gettempdir()
    print("\n\nLets thank everybody!")
    print("\nThis will prepare a letter to send to everyone has donated to Studio Starchelle in the past.")
    print("All letters will be saved as text (.txt) files in the default directory a different directory is specified.")
    print(f"\nDefault Directory: {default_dir}")
    
    user_dir = get_user_output_path()
    
    if main_or_exit(user_dir):
        return
    
    write_dir = user_dir if user_dir is not None else default_dir

    for k, v in donor_dict.items():
        file_path = os.path.join(write_dir, f"{k}.txt")
        email = get_email(k, v[0][-1])
        write_file = open(file_path, "w")
        write_file.write(email)
        write_file.close()
    
    print(f"Donor letters have been written to: {write_dir}")

    
def get_user_output_path():
    """
    Return the user's desired path for emails or None if the user leaves the choice blank.
    Will prompt to create a directory if it does not exist.
    """
    user_dir = safe_input("\nPlease enter a directory (Empty for Default) > ")

    if main_or_exit(user_dir):
        return

    if user_dir != "":
        if not os.path.exists(user_dir):
            while True:
                choice = safe_input(f"The directory \"{user_dir}\" does not exist.  Do you want to create it? ([Y]es / [N]o) > ")
                if choice.lower() in ["yes", "y"]:
                    os.makedirs(user_dir)
                    break
                elif choice.lower() in ["no", "n"]:
                    print("Using default directory instead.")
                    user_dir = None
                    break
                print("Invalid choice.  Please enter \"Yes\" or \"No\"")
    else:
        return None

    return user_dir


def main_or_exit(selection):
    """
    Return if the user wants to return to the main menu or exit the app.

    Return Values:
        True = Return to main menu
        False = Continue with current operation
    """
    if selection in main_dict.keys():
        return True
    elif selection in quit_dict.keys():
        quit_dict[selection][1]()

    return False


def get_email(name, donation):
    """
    Print the thank you email to the console.

    :name:      The name of the donor.
    :donation:  The donation amount that was recieved from the donor.
    """
    return str("Studio Starchelle - A Fizzworks Studios Company\n"
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


def get_donor(user_choice):
    """
    Return the donor entry for the selected.  Creates a donor and appends them to donor_list if they do not exist.

    :user_choice:   The user's donor selection.
    """
    for donor in donor_dict.keys():
        if user_choice.lower() == donor.lower():
            return donor_dict[donor]
    
    donor_dict.update({user_choice: ([], accept_donation)})
    return donor_dict[user_choice]


def create_report():
    """
    Display a table of donors, the total amount they've donated, the count of their donations, and the average donation.
    """
    donor_summary = get_donor_summary()
    header = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    lengths = [get_length([x[0] for x in donor_summary], header[0]),
               get_length([x[1] for x in donor_summary], header[1]),
               get_length([x[2] for x in donor_summary], header[2]),
               get_length([x[3] for x in donor_summary], header[3])]

    sep_strings = ["-" * (x + 2) for x in lengths]
    sep_line = "|" + "+".join(sep_strings) + "|"
    
    table = get_report_header(sep_line, header, lengths)
    table.extend([format_line(d, lengths) + f"\n{sep_line}" for d in sorted(donor_summary, key=sort_key, reverse=True)])

    print("\n".join(table) + "\n")


def get_report_header(sep_line, header, lengths, report_name="Donor Report"):
    """
    Return the header of a deisred report.

    :sep_line:      The seperator line between rows.
    :header:        The header for the report.
    :lengths:       The lenght of each field in the report.
    :report_name:   The name of the report.  (Default = "Donor Report")
    """
    return ["\n|" + "-" * (len(sep_line) - 2) + "|",
            f"|{report_name:^{len(sep_line) - 2}}|",
            sep_line,
            format_line(header, lengths, is_donor=False),
            sep_line]


def sort_key(item):
    """
    The key to sort donors by.
    """
    return float(item[1].replace("$", ""))


def get_donor_summary():
    """
    Return a summary of all donors including their name, total donation sum, count of donations, and average donation.
    """
    return [(k, f"${sum(v[0]):.02f}", len(v[0]),  f"${sum(v[0]) / len(v[0]):.02f}") for k, v in donor_dict.items()]


def format_line(item, lengths, is_donor=True):
    """
    Return a formatted string that will fit in the donor summary table.

    :item:      The sequence of data to format.
    :lengths:   The lengths for each field of the table.
    :is_donor:  A boolean value determining whether or not the :item: is a donor.  (Default = True)
    """
    return f"| {item[0]:<{lengths[0]}} | {item[1]:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {item[3]:>{lengths[3]}} |"


def get_length(seq, name):
    """
    Return the max length between the longest item in a sequence or the name of the field.

    :seq:   The sequence to evaluate
    :name:  The name of the field to evaluate
    """
    longest = sorted(seq, key=length_key, reverse=True)[0]
    return max(len(name), len(str(longest)))


def length_key(item):
    """
    The sort key for the length of items in a sequence
    """
    return len(str(item))


main_menu_dict = {"Send A Thank You":    ("\tGet prepopulated email template to thank a donor.", send_thanks),
                  "Create a Report":     ("\t\tView a list of all donors and their cumulative donations.", create_report),
                  "Send Letters to All": ("\tGenerate a letter for every donor.", send__to_all)
                  }


main_dict = {"main":   ("\tReturn to the main menu.  Can be used at any input prompt.", None),
             "return": ("\tReturn to the main menu.  Can be used at any input prompt.", None),
             "stop":   ("\tReturn to the main menu.  Can be used at any input prompt.", None)
             }


quit_dict = {"exit": ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
             "end":  ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
             "quit": ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
             }

            
list_dict = {"list": ("\t\tPrint a list of available donors.", print_donors),
             "l":    ("\t\tPrint a list of available donors.", print_donors),
             "ls":   ("\t\tPrint a list of available donors.", print_donors)
             }

            
donor_dict = {"Cresenta Starchelle": ([99.99, 6000.00, 10345.23, 29.99], get_donor),
              "Delilah Matsuka":     ([199.99, 299.99, 2100.00],         get_donor),
              "Astra Matsume":       ([599.99],                          get_donor),
              "Kima Metoyo":         ([3600.00, 1200.00],                get_donor),
              "Kayomi Matsuka":      ([0.01],                            get_donor),
              "Katie Starchelle":    ([600.00],                          get_donor)
              }


if __name__ == "__main__":
    main()
