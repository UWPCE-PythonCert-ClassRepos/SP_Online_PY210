#Mailroom.py


def send_thank_you_note():
    #-----User Options-----
    # (list): show list of donors and re-prompt for name
    # (Name not in database): add to list and use it
    # (Name in database): use it

    #Prompt for donation amount
        #convert amount to number
        #add donation to user history

    #Compose an email: thank the user, print email to terminal
        # and re-prompt user for an action
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

def quit():
    #Exit the main() function
    return False

def main():
    while True:
        #Prompt the user for one of the following actions:
            #1 Send thank you: Prompt for a full name
                #send_thank_you_note()

            #2 Create a report
                #create_report()

            #3 quit
                #quit()

    return None

# Main Interaction
if __name__ == '__main__':
    main()