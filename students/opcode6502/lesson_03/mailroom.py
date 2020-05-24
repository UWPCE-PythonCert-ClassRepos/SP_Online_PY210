# mailroom.py
# opcode6502: SP_Online_PY210

import sys

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

donors = [
    ("Donor 01", [100]),
    ("Donor 02", [150, 500]),
    ("Donor 03", [250, 250, 150]),
    ("Donor 04", [20, 3, 1578]),
    ("Donor 05", [360, 300, 4000])
]

def create_report():

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: create_report(): called!")

    # Print a list of your donors, sorted by total historical donation amount.
    #
    # Donor Name                | Total Given | Num Gifts | Average Gift
    # ------------------------------------------------------------------
    # William Gates, III         $  653784.49           2  $   326892.24
    # Mark Zuckerberg            $   16396.10           3  $     5465.37
    # Jeff Bezos                 $     877.33           1  $      877.33
    # Paul Allen                 $     708.42           3  $      236.14

    # Print the header row.
    if debug_flag: print("[ H ROW ]: ", end='')
    print('{:25} | {:1} | {:1} | {:1}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))

    # Print the spacer row.
    if debug_flag: print("[ ----- ]: ", end='')
    print('-'*66)

    # print(donors)
    def sort_key(d):
        return sum(d[1])

    donors_sorted = sorted(donors, key=sort_key, reverse=True)

    for donor in donors_sorted:
        donor_name = donor[0]
        donor_total = sum(donor[1])
        number_of_gifts = len(donor[1])
        average_gift = round(donor_total / number_of_gifts)
        if debug_flag: print("[  DATA ]: ", end='')
        print('{:26} ${:>11.2f} {:>11}  ${:>12.2f}'.format(
              donor_name,
              donor_total,
              number_of_gifts,
              average_gift))

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: create_report(): exiting!")


def display_user_prompt():

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: display_user_prompt(): called!")

    # The script should prompt the user (you) to choose from a menu of 3 actions:
    #   “Send a Thank You”,
    #   “Create a Report” or
    #   “Quit”.

    # Display user prompt.
    while True:
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
            # Debug statement.
            if debug_flag: print("[ DEBUG ]: display_user_prompt(): exiting!")
            exit_script()
        else:
            print("[ ERROR ]: Select item: 1, 2, or 3.")


def exit_script():

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: exit_script(): called! Script halting.")
    sys.exit()


# Send a Thank You
def send_thank_you():

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: send_thank_you(): called!")

    # If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
    #
    # If the user types list show them a list of the donor names and re-prompt.
    #
    # If the user types a name not in the list, add that name to the data structure and use it.
    #
    # If the user types a name in the list, use it.
    #
    # Once a name has been selected, prompt for a donation amount.
    #
    # Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
    #
    # Add that amount to the donation history of the selected user.
    #
    # Finally, use string formatting to compose an email thanking the donor for their generous donation.
    #
    # Print the email to the terminal and return to the original prompt.
    #
    # It is fine (for now) for the program not to store the names of the new donors that had been added
    # in other words, to forget new donors once the script quits running.

    # Debug statement.
    if debug_flag: print("[ DEBUG ]: send_thank_you(): exiting!")


# DEBUG: The debug_flag will turn on helpful testing statements.
# This creates a sort of 'black box' where you can read the exact steps
# that the code executed and debug where things went wrong (or right).
#
# NOTE: These debug messages are best viewed with a terminal width of at least
# 90 to 100 columns (depending on length of strings and tuples to be tested).
#
# Set to 1 = ENABLE debug messages.
# Set to 0 = DISABLE debug messages.
#
# DEBUG MESSAGES key:
# [ EXEC  ]: Informs which function is printing debug statements.
# [ DEBUG ]: A debug statement.
debug_flag = 0


if __name__=='__main__':
    display_user_prompt()
