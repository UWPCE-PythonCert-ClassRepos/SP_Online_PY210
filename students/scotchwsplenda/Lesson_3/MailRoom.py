import sys  # need to do this if you want to use sys.exit()


donators = [
("Gordian",[30.0,45.0]),
("Tiberius",[60]),
("Maximus",[65.00, 12.00]),
("Tacitus",[33.00,22.00]),
("Commodus",[43,11])]

prompt = "\n".join(("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
        "Welcome to the MAILROOM main menu",
          "Please choose from below options:",
          "1 - Initiate Groveling",
          "2 - Data Metrics 3000",
          "3 - Quit",
          "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
          "Indicate your choice:  "))

extant_don=[i[0] for i in donators]



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
            print(names)
        if respondy=="2":
            donor_inp=input("Input donor: ")
            if donor_inp in extant_don :
                # they've entered a donor we already know
                don_amount = input("That's a known donor, input donation amount: ")
                # return the index for the known donoor
                don_indx = [item[0] for item in donators].index(donor_inp)
                # indicate to python the column titles in the tuple at the specified index in the list
                name, donations = donators[don_indx]
                # apppend donation amount to donators
                # I DON'T KNOW IF THIS IS WORKING BECAUSE THE CODE DOESN'T CHANGE ON MY END
                donations.append(float(don_amount))
            else:
                # they've entered a donor we don't have a record of
                new_don = input("That's an unknown donor, do you wish to add them y/n?")
                if new_don=="y":
                    asd00
                    # request donation donation amount
                    # append to donators
                else:
                    return main()
        elif respondy=="3":
            return main()







# def add_fruit():
#     new_fruit = input("Name of the fruit to add?").title()
#     fruits.append(new_fruit)

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
            print_don()
        elif response == "3":
            exit_program()
        elif response  =="4":
            print(donators)
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
