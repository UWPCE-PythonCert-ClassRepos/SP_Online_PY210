import sys


donors  =[('James Smith',[21000.25, 500, 27.50]),
        ('Dorothy Parker',[3175, 475.45, 92.30]),
        ('Dohgyu Hwang',[10670, 350.19,175]),
        ('Sally Yu', [100, 925]),
        ('Jenny Ramos',[25.14])]

prompt = "\n".join(("Functions:",
          "Please choose from below options:",
          "1 - Send a Thank You to donors",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))


def add_donors():
    print("If you want a list of donors please type 'list' ")
    while True:
        response = input("Please enter the full name of the donor or select list? ")
        if response == "list":
            list_donors()
            break
        else:
            amount = int(input("Please enter the amount of donation: "))
            for donor in donors:
                if donor[0] == response:
                    donor.append((response, [amount]))
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
        print("{:<20s}".format(donors[i][0]))


def view_donors(donors):
    print("{:20s}{:20s}{:20s}{:20s}".format("DONOR ", "| TOTAL GIVEN ", "| NUMBER OF GIFTS ", "| AVERAGE GIFTS "))
    print("-----------------------------------------------------------------------------")

    summary_data = []

    for donor in donors:
        donations = donor[1]
        summary_data.append([((len(donations))),sum(donations)])
        sorted_data = sorted(summary_data, reverse=True)

    for i in range(len(donors)):
        tot_ave = (sum(donors[i][1]) / int(len(donors[i][1])))
        print("{:20s}{:^20.2f}{:^19d}{:^18.2f}".format(donors[i][0], (sorted_data[i][1]), len(donors[i][1]), tot_ave))



def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            add_donors()
        elif response == "2":
            view_donors(donors)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
   main()