import sys  # need to do this if you want to use sys.exit()


donators = [
("Gordian",[30.0,45.0]),
("Tiberius",[60]),
("Maximus",[65.00, 12.00]),
("Tacitus",[33.00,22.00]),
("Commodus",[43,11])]

# Opening menu
prompt = "\n".join(("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
        "Welcome to the MAILROOM main menu",
          "Please choose from below options:",
          "1 - Initiate Groveling",
          "2 - Data Metrics 3000",
          "3 - Quit",
          "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
          "Indicate your choice:  "))

# Names of donors
extant_don=[i[0] for i in donators]

# Option 1: Content of Thank you note
def send_thanks(a,b):
    print(f'Wow {a}, only ${b}?'
    "\n"+'Give til it hurts you capitalist swine')

#Option 1: logic of thank you note
def Send_Note():
    done=False
    while not done:
        respondy= input(
        "\n"+"Please select from the below Thank You Note options:"
        "\n"+"1 - Print list of extant donors"
        "\n"+"2 - Enter donor name and donation"
        "\n"+"3 - Return to the MAILROOM main menu"
        "\n"+"Indicate your choice:  ")
        if respondy=="1":
            print(extant_don)
        if respondy=="2":
            donor_inp=input("Input donor: ")
            if donor_inp in extant_don :
                # they've entered a donor we already know
                don_amount = input("That's a known donor, input donation amount: ")
                # return the index for the known donoor
                # DO I HAVE TO LOOP THROUGH THE LIST? DO I HAVE TO SPECIFY IT'S THE FIRST 'ITEM' IN THE TUPLE?
                don_indx = [item[0] for item in donators].index(donor_inp)
                # indicate to python the column titles in the tuple at the specified index in the list
                name, donations = donators[don_indx]
                # apppend donation amount to donators
                # WHY DOESN'T THIS 'SAVE' INTO MY ACTUAL CODE? IT WORKS DURING THE 'SESSION' BUT DOESN'T SAVE
                donations.append(float(don_amount))
                send_thanks(donor_inp,don_amount)
            else:
                # they've entered a donor we don't have a record of
                new_don = input("That's an unknown donor, do you wish to add them y/n?")
                if new_don=="y":
                    NEW_don_amount = input("Input new donor donation amount: ")
                    donators.append((donor_inp, float(NEW_don_amount)))
                    send_thanks(donor_inp,NEW_don_amount)
                else:
                    return main()
        elif respondy=="3":
            return main()

# Option 2: create report
def data_metrics():
    new_fruit = input("Name of the fruit to add?").title()
    fruits.append(new_fruit)

#Option 3: get out of this program
def exit_program():
    print("Bye!")
    sys.exit()  # THIS IS INCREDIBLY IMPORTANT


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            Send_Note()
        elif response == "2":
            data_metrics()
        elif response == "3":
            exit_program()
        elif response  =="4":
            print(donators)
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
