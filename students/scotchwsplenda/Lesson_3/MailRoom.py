import sys  # need to do this if you want to use sys.exit()
from operator import itemgetter


# donors
donators = [
("Gordian",[30.0,45.0]),
("Tiberius",[60.0]),
("Maximus",[65.0, 12.0]),
("Tacitus",[33.0,22.0,25.00]),
("Commodus",[43.0,11.0])]


# Opening menu
prompt = "\n".join(("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
        "Welcome to the MAILROOM main menu",
          "Please choose from below options:",
          "1 - Initiate Groveling",
          "2 - Data Metrics 3000",
          "3 - Quit",
          "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
          "Indicate your choice:  "))


# opening menu option responses
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

# Option 1: Content of Thank you note
def send_thanks(a,b):
    print("\n"f'Wow {a}, only ${b}?'
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
            print([i[0] for i in donators])
        if respondy=="2":
            donor_inp=input("Input donor: ")
            if donor_inp in ([i[0] for i in donators]) :
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
                    new_don_amount = input("Input new donor donation amount: ")
                    # unsure how to enforce entry of a float or integer
                    donators.append((donor_inp, new_don_amount))
                    send_thanks(donor_inp,new_don_amount)
                else:
                    return
        elif respondy=="3":
            return

# Option 2: create report
def data_metrics():
    report = []
    for name, donations in donators:
        total_Given = sum(donations)
        number_Gifts = len(donations)
        average_Gift = total_Given/number_Gifts
        report.append((name, total_Given, number_Gifts, round(average_Gift,1)))
    ranked_dons=sorted(report, key=itemgetter(1),reverse=True)
    # https://stackoverflow.com/questions/46490541/how-print-list-of-tuples-side-by-side/46490575
    # for x in ranked_dons:
    #     print(*x:, sep='|')
    print('Name'+'-'*30+'Sum'+'-'*28+'Count'+'-'*30+'Avg')
    for a,b,c,d in ranked_dons:
        print(f'{a:<33}{b:<33}{c:<33}{d:<33}')

#Option 3: get out of this program
def exit_program():
    print("Bye!")
    sys.exit()  # THIS IS TO EXIT THE PROGRAM AND START OVER


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
