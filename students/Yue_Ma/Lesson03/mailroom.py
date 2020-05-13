#!/usr/bin/env python3
import sys

donor_list = {'Yue Ma': [100000, 1561132],
              'Yanan Ma': [1000, 5645, 6161, 27],
              'Jianqiang Ma': [200000, 854821, 1202],
              'Chunhong Liu': [100.51, 1000.1],
              'Robert Rowe': [20000000]}


def main():
    main_prompt = "\n".join(("Welcom to Mailroom!",
                             "Please choose from below options:",
                             "Enter: '1' - Send a Thank You note",
                             "Enter: '2' - Create a report",
                             "Enter: '3' - Quit the Mailroom"))
    while True:
        user_main = input(main_prompt)
        if user_main == '1':
            send_a_thank_you_note()
        elif user_main == '2':
            create_a_report()
        elif user_main == '3':
            exit()
        else:
            print("Not a valid option!!!")


def send_a_thank_you_note():
    send_a_thank_you_note_prompt = "\n".join(("Please choose from below options:",
                                              "Enter: 'list' - Print a list of donors",
                                              "Enter: '1' - Print the donation history of individual donors",
                                              "Enter: '2' - Back to the main menu"))
    while True:
        user_send_a_thank_you_note = input(send_a_thank_you_note_prompt)
        if user_send_a_thank_you_note == 'list':
            print(' ')
            print(list(donor_list.keys()))
            print(' ')
        elif user_send_a_thank_you_note == '1':
            user_name = input("Please enter the full name that you want to search with a space in between"
                              "(Ex. 'Tom James'):")
            user_amount = input("Please enter the amount of the donation:")

            if user_name in donor_list.keys():
                print('')
                print('This name is in our database!')
                list_history = list(donor_list[user_name])
                list_history.append(float(user_amount))
                donor_list[user_name] = list_history
                print('Updated the info to our database.')
                print(email(user_name))
            else:
                print('')
                print('This name is NOT in our database!')
                donor_list[user_name] = [float(user_amount)]
                print('Added the name to our database.')
                print(email(user_name))
        elif user_send_a_thank_you_note == '2':
            break
        else:
            print("Not a valid option!!!")
    return


def create_a_report():
    title = {'Donor Name': ['Total Given', 'Num Gifts', 'Average Gift']}
    value_title = list(title.values())
    key_title = list(title.keys())

    # calculate total donation
    donation_matrix = {}
    for item in donor_list.keys():
        donation_matrix[item] = sum(list(donor_list[item]))

    # sort
    donation_matrix_raw = sorted(donation_matrix.items(), reverse=True, key=lambda t: t[1])
    donation_matrix_sorted = {}
    for i in range(len(donation_matrix_raw)):
        donation_matrix_sorted[donation_matrix_raw[i][0]] = donation_matrix_raw[i][1]

    print(donation_matrix_sorted)
    # Print the report
    line_title = f'| {key_title[0]:<20}| {value_title[0][0]:<15} | {value_title[0][1]:<10} | {value_title[0][2]:<15}|'
    line_x = '|' + '-' * 69 + '|'
    line_1 = ' ' + '-' * 69 + ' '

    print(line_1)
    print(line_title)
    print(line_x)
    for item in donation_matrix_sorted.keys():
        main_lines = f'| {item:<20}| {donation_matrix_sorted[item]:<15.2f} | {len(donor_list[item]):<10} ' \
                     f'| {float(donation_matrix_sorted[item]) / len(donor_list[item]):<15.2f}|'
        print(main_lines)
    print(line_1)
    return


def exit():
    print('Thank you for using Mailroom! See you next time!')
    sys.exit()


def email(x):
    email_prompt = '\n' + 'Dear ' + x + ',' + '\n\nThank you for your donation! We will make sure that ' \
                                              'the money is in good use!!! \n\nSincerely, \nThe Donation Team \n'
    return email_prompt


if __name__ == "__main__":
    main()
