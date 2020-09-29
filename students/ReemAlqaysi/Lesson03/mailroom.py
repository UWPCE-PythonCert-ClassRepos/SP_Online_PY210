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
donor_list = [
    ["Jan Balard", (600.00,250.00)],
    ["Joe McHennry", (1500.00,1500.00)],
    ["Jeff Hansen", (450.00,150.00)],
    ["Scott Newman", (100.00,5000.00)],
    ["Rabi Das", (500.00,950.00)]
    ]
# main menue prompt
prompt ="\n".join(("Welcome to the MailRoom!",
          "Please choose from below options:",
          "1 - Send a Thank You Email",
          "2 - Create a Rrport",
          "3 - Exit",
          ">>> ")) 

#get the donation amounts
def get_amount():
    amount = input("please enter donation amounts : ")
    amount = int(amount)
    return amount

#get the name and check if it exist, add the ammount, otherwise add the name and the amount to the donors list
def add_name():
    fullname = input("please enter full name : ")
    if fullname == 'list':
        for doner in donor_list:
            print(doner[0])
        add_name()
    else:
        amount = get_amount()
        for doner in donor_list:
            if doner[0].lower() == fullname.lower():
                amountlist = list(doner[1])
                amountlist.append(amount)
                doner[1] = amountlist
                break # to make sure it will not check ans add the name manytimes
        else:
            donor_list.append((fullname,[amount])) # add new name and donations
        thank_you_email(fullname,amount)

#thank you Email formating
def thank_you_email(fullname, amount):
    print ("\n\nDear {}:\n Thank you for your donation of ${:2d}, we appriciate your support to our service. \n MailRoom Team\n".format(fullname,amount))
    main()

#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def create_report():
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)

    for donor in sorted(donor_list, key=itemgetter(1)):
        print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(donor[0], '$', round(sum(donor[1]),2), len(donor[1]), '$',round(sum(donor[1])/len(donor[1]),1))))


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
   
    while True:
        response = input(prompt)  # continuously collect user selection
        
        ## now redirect to feature functions based on the user selection
        if response == "1":
            add_name()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
   	        print('That is not a valid answer!')



if __name__ == "__main__":
   main()