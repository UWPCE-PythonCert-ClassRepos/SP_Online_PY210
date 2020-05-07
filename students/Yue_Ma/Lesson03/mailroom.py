#!/usr/bin/env python3

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
            break
        elif user_main == '2':
            create_a_report()
            break
        elif user_main == '3':
            print('Thank you for using Mailroom! See you next time!')
            break
        else:
            print("Not a valid option!!!")


def send_a_thank_you_note():
    send_a_thank_you_note_prompt = "\n".join(("Please choose from below options:",
                                              "Enter: 'list' - Print a list of donors",
                                              "Enter: '1' - Print the donation history of individual donors",
                                              "Enter: '2' - Back to the main menu or Quit"))
    while True:
        user_send_a_thank_you_note = input(send_a_thank_you_note_prompt)
        if user_send_a_thank_you_note == 'list':
            print(' ')
            print(list(donor_list.keys()))
            print(' ')
            back_to_main()
            break
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
                back_to_main()
            else:
                print('')
                print('This name is NOT in our database!')
                donor_list[user_name] = [float(user_amount)]
                print('Added the name to our database.')
                print(email(user_name))
                back_to_main()
            break
        elif user_send_a_thank_you_note == '2':
            back_to_main()
            break
        else:
            print("Not a valid option!!!")


def create_a_report():
    title = {'Donor Name': ['Total Given', 'Num Gifts', 'Average Gift']}
    value_title = list(title.values())
    key_title = list(title.keys())

    # calculate total donation
    donation_matrix = []
    for j in range(0, len(donor_list)):
        donation_matrix.append([list(donor_list.keys())[j], sum(list(donor_list.values())[j]),
                                len(list(donor_list.values())[j])])

    line_title = f'| {key_title[0]:<20}| {value_title[0][0]:<15} | {value_title[0][1]:<10} | {value_title[0][2]:<15}|'
    line_x = '|' + '-' * 69 + '|'
    line_1 = ' ' + '-' * 69 + ' '

    # Print the report
    print(line_1)
    print(line_title)
    print(line_x)
    for i in range(0, len(donor_list)):
        main_lines = f'| {donation_matrix[i][0]:<20}| {donation_matrix[i][1]:<15.2f} | {donation_matrix[i][2]:<10} ' \
                     f'| {donation_matrix[i][1] / donation_matrix[i][2]:<15.2f}|'
        print(main_lines)
    print(line_1)
    back_to_main()


def back_to_main():
    back_to_main_prompt = "\n".join(("Please choose from below options:",
                                     "Enter: '1' - Back to the main menu",
                                     "Enter: '2' - Quit"))
    while True:
        user_back_to_mean = input(back_to_main_prompt)
        if user_back_to_mean == '1':
            main()
            break
        elif user_back_to_mean == '2':
            print('Thank you for using Mailroom! See you next time!')
            break
        else:
            print("Not a valid option!!!")


def email(x):
    email_prompt = '\n' + 'Dear ' + x + ',' + '\n\nThank you for your donation! We will make sure that ' \
                                              'the money is in good use!!! \n\nSincerely, \nThe Donation Team \n'
    return email_prompt


if __name__ == "__main__":
    main()
