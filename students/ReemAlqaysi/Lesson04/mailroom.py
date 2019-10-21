"""
MAIL ROOM PART 1
this script has a data structure that holds a list of  donors and a history of the amounts they have donated. 
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
 data structure stored in the global namespace.
The script prompts the user (you) to choose from a menu of 3 actions: 
“Send a Thank You”, “Create a Report” or “quit”.
"""

from operator import itemgetter
import sys  # imports go at the top of the file

#initial donations ammount and givers names.
donor_list = {
    "Jan Balard": [600.00,250.00],
    "Joe McHennry": [1500.00,1500.00],
    "Jeff Hansen": [450.00,150.00],
    "Scott Newman": [100.00,5000.00],
    "Rabi Das": [500.00,950.00]
    }
# main menue prompt
def main_menu():
    print("\n".join(("Welcome to the MailRoom!",
          "Please Choose an action:",
          "1 - Send a Thank You to a single donor.",
          "2 - Create a Report.",
          "3 - Send letters to all donors.",
          "4 - Quit",
          ">>> ")))
    return input()


#get the donation amounts
def get_amount():
    amount = input("please enter donation amounts : ")
    amount = int(amount)
    return amount

#get the name and check if it exist, add the ammount, otherwise add the name and the amount to the donors list
def add_name():
    fullname = input("please enter full name : ")
    if fullname == 'list':
        for key in donor_list:
            print(key)
        add_name()
    else:
        amount = get_amount()
        if donor_list.get(fullname):
            donor_list[fullname].append(amount)
        else:
            donor_list.update({fullname:(amount)}) # add new name and donations
    thank_you_email(fullname,amount)



#thank you Email formating
def thank_you_email(fullname, amount):
    print ("\n\nDear {}:\n Thank you for your donation of ${:2d}, we appriciate your support to our service. \n MailRoom Team\n".format(fullname,amount))
    main()


#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def create_report():
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)

    for donor, value in sorted(donor_list.items(), key=itemgetter(1)):
        print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(donor, '$', round(sum(value),2), len(value), '$',round(sum(value)/len(value),1))))


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

#send letter to all givers, file name is snake style
def letter_to_all():
        for k,v in donor_list.items():
            amount = k[len(v) - 1]
            fileName = k.replace(' ', '_').replace(',', '') + ".txt"
            fileName = fileName.lower()
            filetext = "Dear {},\n\tThank you for your very kind donation of ${}\n\tIt will be put to very good use.\n\t\t\tSincerely,\n\t\t\t- The Team".format(k,amount)
            with open(fileName,'w+') as output:
                output.write(filetext)
                print("\nLetters {} have been printed and are saved in the current directory".format(fileName))




def main():
    #dict with the user options and the functions
    options = {
        '1': add_name,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    }
    while True:
        response = main_menu()
        menu_function = options.get(response)
        if response in options:
            menu_function()
        else:
            print("\n'{}'  is not a valid answer, please select option from 1-4 !. \n >> ".format(response))

if __name__ == "__main__":
   main()