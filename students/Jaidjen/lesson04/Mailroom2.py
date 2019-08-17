import sys  # imports go at the top of the file


donors = [{'Name':'James Smith', 'Donation':[21000.25,500,27.50]},
          {'Name': 'Dorothy Parker','Donation':[3175,475.45,92.30]},
          {'Name':'Dohgyu Hwang','Donation':[10670,350.19,175]},
          {'Name': 'Sally Yu', 'Donation':[100,925]},
          {'Name':'Jenny Ramos','Donation':[25.14]}]


prompt = {
    1: "add_donors()",
    2: "view_donors(donors)",
    3: "thankyou_donors()",
    4: "exit_program()"
}


def view_donors(donors):
    print("{:20s}{:20s}{:20s}{:20s}".format("DONOR ", "| TOTAL GIVEN ", "| NUMBER OF GIFTS ", "| AVERAGE GIFTS "))
    print("-----------------------------------------------------------------------------")
    summary_data = []

    for donor in donors:
            donations = donor["Donation"]
            summary_data.append([len(donations),sum(donations)])
    sorted_data = sorted(summary_data, reverse=True)

    for i in range(len(sorted_data)):
        print("{:20s}{:^20.2f}{:^19d}{:^18.2f}".format((donors[i]["Name"]),(sorted_data[i][1]),(len(donors[i]["Donation"])),(sum(donors[i]["Donation"]))/(len(donors[i]["Donation"]))))


def add_donors():
    print("If you want a list of donors please type 'list' ")
    while True:
        response = input("Please enter the full name of the donor or select list? ")
        if response == "list":
            list_donors()
            break
        else:
            amount = (int(input("Please enter the amount of donation: ")))
            for donor in donors:
                if donor["Name"] == response:
                    donors.append((response, [amount]))
                    break
            else:
                donors.append((response, [amount]))
                print('Dear', response, ',')
                print('Thank you', response, 'for donating', '{:.2f}'.format(int(amount)))
                print('We appreciate your generosity.')
                print()
                print('Sincerely, Donation Team')
                print()
                break

def list_donors():
    for i in range(len(donors)):
        print("{:<20s}".format(donors[i]["Name"]))

def thankyou_donors():
    for donor in donors:
        donations = donor["Donation"]
        donated = sum(donations)
        donor_name = donor["Name"]
        print('Dear',(donor_name),',')
        print('Thank you for your very kind donation of','{:.2f}'.format(donated))
        print('It will be put to very good use.')
        print('Sincerely, Donation Team')
        print(  )



def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    prompt = 0
    while (prompt != 4):
        print("1. Send a Thank You to a single donor")
        print("2. Create a Report")
        print("3. Send letters to all donors")
        print("4. Quit")
        prompt = int(input("Select a menu option: "))

        if prompt == 1:
            add_donors()
        elif prompt == 2:
            view_donors(donors)
        elif prompt == 3:
            thankyou_donors()
        elif prompt == 4:
            exit_program
        else:
            print("Not a valid option")




if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
