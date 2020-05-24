# mailroom.py
# opcode6502: SP_Online_PY210


    # The Program: Part 1
    # Write a small command-line script called mailroom.py.
    # This script should be executable.
    # The script should accomplish the following goals:
    #
    # It should have a data structure that holds:
    #   a list of your donors and
    #   a history of the amounts they have donated.
    #
    # This structure should be populated at first with
    #   at least five donors,
    #   with between 1 and 3 donations each.
    #
    # You can store that data structure in the global namespace.


def create_report():
    if debug_flag: print("[ DEBUG ]: create_report(): called!")
    # Create a Report
    #
    # If the user (you) selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
    # Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor’s donations, just the summary info.
    # Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below).
    # After printing this report, return to the original prompt.
    # At any point, the user should be able to quit their current task and return to the original prompt.
    # From the original prompt, the user should be able to quit the script cleanly.
    # Your report should look something like this:

    # Donor Name                | Total Given | Num Gifts | Average Gift
    # ------------------------------------------------------------------
    # William Gates, III         $  653784.49           2  $   326892.24
    # Mark Zuckerberg            $   16396.10           3  $     5465.37
    # Jeff Bezos                 $     877.33           1  $      877.33
    # Paul Allen                 $     708.42           3  $      236.14
    if debug_flag: print("[ DEBUG ]: create_report(): exiting!")


# Send a Thank You
def send_thank_you():
    if debug_flag: print("[ DEBUG ]: send_thank_you(): called!")
    # If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
    # If the user types list show them a list of the donor names and re-prompt.
    # If the user types a name not in the list, add that name to the data structure and use it.
    # If the user types a name in the list, use it.
    # Once a name has been selected, prompt for a donation amount.
    # Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
    # Add that amount to the donation history of the selected user.
    # Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
    # It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.
    if debug_flag: print("[ DEBUG ]: send_thank_you(): exiting!")


def display_user_prompt():
    # The script should prompt the user (you) to choose from a menu of 3 actions:
    #   “Send a Thank You”,
    #   “Create a Report” or
    #   “Quit”.

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: display_user_prompt(): called!")

    # Display user prompt.
    user_response = None
    while user_response != '3':
        user_response = input(
                    '[  MENU ]: Select an option:\n'
                    '[    01 ]: Send a Thank You\n'
                    '[    02 ]: Create a Report\n'
                    '[    03 ]: Quit\n'
                    '[ INPUT ]: ')
        if user_response == '1':
            send_thank_you()
        elif user_response == '2':
            create_report()
        elif user_response == '3':
            if debug_flag: print("[ DEBUG ]: display_user_prompt(): exiting!")
            break
        else:
            print("[ ERROR ]: Select item: 1, 2, or 3.")


debug_flag = 1


if __name__=='__main__':
    display_user_prompt()
