import sys
from donor_models import *

donor_collection = DonorCollection()


def main():
    main_prompt = "\n".join(("Welcom to Mailroom!",
                             "Please choose from below options:",
                             "Enter: '1' - Send a Thank You note to a single donor",
                             "Enter: '2' - Create a report",
                             "Enter: '3' - Send letters to all donors",
                             "Enter: '4' - Quit"))
    while True:
        user_main = input(main_prompt)
        while True:
            try:
                int(user_main)
            except ValueError:
                user_main = input(main_prompt)
            else:
                if user_main == '4':
                    exit_program()
                else:
                    arg_dict = {1: send_a_thank_you_note, 2: create_a_report, 3: send_letters_to_all_donors}
                    arg_dict.get(int(user_main))()
                    main()


def exit_program():
    print('Thank you for using Mailroom! See you next time!')
    sys.exit()


def create_a_report():
    report = donor_collection.create_report()
    for item in report:
        print(item)
    return report


def send_letters_to_all_donors():
    donor_collection.send_letters_to_all_donor()


def send_a_thank_you_note():
    send_a_thank_you_note_prompt = "\n".join(("Please choose from below options:",
                                              "Enter: 'list' - Print a list of donors",
                                              "Enter: '1' - Print the donation history of individual donors",
                                              "Enter: '2' - Back to the main menu"))
    while True:
        user_send_a_thank_you_note = input(send_a_thank_you_note_prompt)
        if user_send_a_thank_you_note == 'list':
            print(donor_collection.get_donor_list())

        elif user_send_a_thank_you_note == '1':
            user_name = input("Please enter the full name that you want to search with a space in between"
                              "(Ex. 'Tom James'):")
            user_amount = float(input("Please enter the amount of the donation:"))
            if donor_collection.try_donor(user_name) is None:
                donor_collection.add_a_donor(user_name, user_amount)
            else:
                donor_collection.add_new_donation(user_name, user_amount)

        elif user_send_a_thank_you_note == '2':
            break
        else:
            print("Not a valid option!!!")


if __name__ == "__main__":
    main()

