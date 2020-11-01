
#Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

#It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
#This structure should be populated at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.
#The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

TotalGiven = 0.00
FullName = ''
NumGifts = 0
TableHeader = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
DonorTable = [['Jane Doe', 10000, 4000, 2000],
              ['John Doe', 10000, 2000, 5000, 3000],
              ['Bobby Newport', 2000, 100], ['Johnny Mnemonic', 900, 800, 1000], ['Phillip Dick', 2220]]

def menu():
    print()
    print("Please choose an option:")
    print("1. Send a Thank You")
    print("2. Create a Report")
    print("3. Quit")
    print()

def send_thankyou(FullName):
    print()
    while FullName == '':
        FullName = input("Please enter Donor's Full Name: ")
        if FullName == "list":
            print()
            print('|{:<{width}s}|'.format(*TableHeader, width=20))
            for row in DonorTable:
                print('|{:<{width}s}|'.format(*row, width=20))
        elif FullName == 'quit':
            break
        else:
            for row in DonorTable:
                if FullName.lower() == row[0].lower():
                    AmtGiven = input("Please enter Donor's gift amount: ")
                    row.append(int(AmtGiven))
                    MailText = "Dear {}, \nThank you for your donation of ${}. \nSincerely, Jake".format(row[0], AmtGiven)
                    print(MailText)
                    break
            
            if FullName != row[0] and FullName.lower() != "list":
                DonorTable.append([FullName])
                AmtGiven = input("Please enter Donor's gift amount: ")
                DonorTable[-1].append(int(AmtGiven))
                MailText = "Dear {}, \nThank you for your donation of ${}. \nSincerely, Jake".format(DonorTable[-1][0], AmtGiven)
                print(MailText)

    #return FullName, AmtGiven

def create_report(TableHeader, DonorTable):
    print()
    print('|{:<{width}s}|{:<{width}s}|{:<{width}s}|{:<{width}s}|'.format(*TableHeader, width = 20))
    print('-------------------------------------------------------------------------------------')
    for row in DonorTable:
        DonationTotal = sum(row[1:])
        DonationAvg = DonationTotal/(len(row)-1)
        DonationQty = len(row)-1

        print('|{:<{width}s}|${:<19.2f}|{:<{width}d}|${:<19.2f}|'.format(row[0], DonationTotal, DonationQty, DonationAvg, width = 20))

def main():
    while True:
        menu()
        UserInput = input("Choice Selected: ")
        if UserInput == '1':
            send_thankyou(FullName)
        elif UserInput == '2':
            create_report(TableHeader, DonorTable)
        elif UserInput == '3':
            break

if __name__ == "__main__":
    main()