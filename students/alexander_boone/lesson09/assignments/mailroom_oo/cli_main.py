#!/usr/bin/env python



if __name__ == '__main__':
    '''Main Code'''
    response_dict = {1: thank_you, 2: display_report,
                     3: quit_program}
    response = 0
    while True:
        response = 0

        # display main menu with options
        options = ["1. Send a Thank You to a single donor", "2. Create a"
                   + " Report", "3. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}"
              + f"\n{options[2]}")

        # ask for and run user response
        while int(response) not in response_dict:
            try:
                response = int(safe_input("Enter a number: "))
            except ValueError:
                print('Input must be a number. Enter 1, 2, or 3.')
            else:
                if response not in response_dict:
                    print('Invalid Response. Enter 1, 2, or 3.')
        response_dict.get(response)()