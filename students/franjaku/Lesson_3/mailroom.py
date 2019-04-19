import sys
#Mailroom.py

def prompt_user():
    prompt = "\n".join(('1: Send thank you note',
             '2: Create report',
             '3: Quit',
             '>>> '))

    UserAction = input(prompt)
    return UserAction

def send_thank_you_note():
    #-----User Options-----
    # (list): show list of donors and re-prompt for name
    # (Name not in database): add to list and use it
    # (Name in database): use it

    #Prompt for donation amount
        #convert amount to number
        #add donation to user history

    #Compose an email: thank the user, print email to terminal
    return None

def create_report():
    #Print the list of donors sorted by historical donation amount
    #Include
        #Donor name
        #Total donated
        #Number of donations
        #Average donation amount
    #End result should be nice and tabular
    #Re-prompt for an action
    return None

def main():
    welcome_message = "\n".join(('',
                      '------------Welcome to the Mailroom :)------------',
                      'What would you like to do?'))
    while True:
        #Prompt the user for one of the following actions:
        #print('Pick and action\n 1: Send thank you note\n 2: Create report\n 3: quit')
        #UserAction = input()

        UserAction = prompt_user()

        if UserAction == '1':
            #1 Send thank you: Prompt for a full name
            print('User option 1')
                #send_thank_you_note()
        elif UserAction == '2':
            #2 Create a report
            print('User option 2')
                #create_report()
        elif UserAction == '3':
            #3 quit
            print('Goodbye!')
            return False
        else:
            print('Not a valid option...\n')
            UserAction = prompt_user()

    return None

# Main Interaction
if __name__ == '__main__':
    main()