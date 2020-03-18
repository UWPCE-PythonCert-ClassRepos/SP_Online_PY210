#!/usr/bin/env python3

charity_name = "ABC Charity"

db_donors2 = {
            "Jane Smith" : [25, 50],
            "Tom Adams" : [100],
            "Helen Smalls" : [10, 20, 30],
            "Ming Chan" : [50],
            "Mary Jones" : [5, 10, 15] }


###################################


def main_menu2():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " R: Create report\n"
    msg += " P: Send letters to all\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    entry = input(msg)

    return entry


def done2():
    quit()


def mailroom2():
    print("mailroom begin")

    op_action_dict = {
                    'S': send_thankyou2,
                    'R': create_report_sorted2,
                    'W': write_letters_to_all2,
                    'Q': done2}

    while True:

        operation = main_menu2()
        op_action_dict.get(operation)()
        print(f"Invalid Entry, please retry: ==> ", operation)

    print("mailroom end")


###################################


# main, test funcs

if __name__ == "__main__":

    mailroom2()

