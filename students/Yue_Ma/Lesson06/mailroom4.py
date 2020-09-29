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


def send_a_thank_you_note():
    send_a_thank_you_note_prompt = "\n".join(("Please choose from below options:",
                                              "Enter: 'list' - Print a list of donors",
                                              "Enter: '1' - Print the donation history of individual donors",
                                              "Enter: '2' - Back to the main menu"))
    while True:
        user_send_a_thank_you_note = input(send_a_thank_you_note_prompt)
        if user_send_a_thank_you_note == 'list':
            print(list_user(donor_list))
        elif user_send_a_thank_you_note == '1':
            user_name = input("Please enter the full name that you want to search with a space in between"
                              "(Ex. 'Tom James'):")
            user_amount = float(input("Please enter the amount of the donation:"))

            if user_name in donor_list.keys():
                add_amount(donor_list, user_name, user_amount)
            else:
                add_user(donor_list, user_name, user_amount)

            print(email(user_name))
        elif user_send_a_thank_you_note == '2':
            break
        else:
            print("Not a valid option!!!")


def add_amount(x, y, z):
    x[y].append(z)
    return x


def add_user(x, y, z):
    x[y] = [float(z)]
    return x


def list_user(x):
    return list(x.keys())


def total(data):
    return sum(data[1])


def create_a_report():
    title = {'Donor Name': ['Total Given', 'Num Gifts', 'Average Gift']}
    value_title = list(title.values())
    key_title = list(title.keys())

    # sort
    donation_matrix_sorted = sorted(donor_list.items(), reverse=True, key=total)

    # Print the report
    line_title = f'| {key_title[0]:<20}| {value_title[0][0]:<15} | {value_title[0][1]:<10} | {value_title[0][2]:<15}|'
    line_x = '|' + '-' * 69 + '|'
    line_1 = ' ' + '-' * 69 + ' '

    report = [line_1, line_title, line_x]
    for item in donation_matrix_sorted:
        main_lines = f'| {item[0]:<20}| {sum(item[1]):<15.2f} | {len(item[1]):<10} ' \
                     f'| {sum(item[1]) / len(item[1]):<15.2f}|'
        report.append(main_lines)
    report.append(line_1)

    for item in report:
        print(item)

    return report


def send_letters_to_all_donors():
    for item in donor_list.keys():
        file_name = '{}.txt'.format(item.replace(' ', '_'))
        file = open(file_name, 'w')
        amount = " " + str(sum(donor_list[item]))
        file.write(email(item, y=amount))
    print('file saved')


def exit_program():
    print('Thank you for using Mailroom! See you next time!')
    sys.exit()


def email(x, y=''):
    if y == '':
        print('Updated the info to our database.')
    email_prompt = '\n' + 'Dear {},\n\nThank you for your donation{}! It will be put to very good use!!! ' \
                          '\n\nSincerely, \nThe Donation Team \n'.format(x, y)
    return email_prompt


if __name__ == "__main__":
    main()
