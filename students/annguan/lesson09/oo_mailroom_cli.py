###Incomplete - ran out of time.

def thanks_one():
    while True:
        name = input("Enter a donar's name or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(list_donors())
        elif name == "menu":
            return
        else:
            break
    while True:
        



def quit():
    sys.exit(0)

if __name__ == "__main__":
    option_select = ['1', '2', '3']
    while True:
        user_prompt = input('Menu Selection\n'
              'Please make a selection:\n'
              '1 - Send a Thank You\n'
              '2 - Create a Report\n'
              '3 - Quit\n'
              'Enter your selection: ')
        if user_prompt not in option_select:
            quit()
        elif user_prompt == '1':
            thanks_one()
        elif user_prompt == '2':
            create_a_report()
        elif user_prompt == '3':
            quit()
