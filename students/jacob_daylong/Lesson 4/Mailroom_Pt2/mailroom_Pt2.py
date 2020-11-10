import tempfile

FullName = ''
TableHeader = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
DonorTable = {}

def menu():
    dict_menu = {'\n1.': 'Send a Thank You', '2.' : 'Create a Report', '3.' : 'Send Thank You - All Donors', '4.' : 'Quit'}
    for x, y in dict_menu.items():
        print(x, y)

def thankyou_note(entry):
    note =(f'\nDear {entry}, \nThank you for your donation of ' 
          f'${sum(DonorTable.get(entry)):.2f}. \nSincerely, Jake\n')
    return note

def send_thankyou(FullName):
    FullName = input("\nPlease enter donor's Full Name: ")
    while FullName == 'List':
        for entry in DonorTable:
            print(entry)
        FullName = input("\nPlease enter donor's Full Name: ")

    DonorAmt = float(input("Please enter the amount given: "))

    if FullName not in DonorTable:
         DonorTable[FullName] = [DonorAmt]
    else:
         DonorTable[FullName] += [DonorAmt]

    print(thankyou_note(FullName))

def thankyou_print():
    for entry in DonorTable:
        dir = tempfile.gettempdir()
        filename = entry + '.txt'
        f = open(dir + filename, 'w')
        f.write(thankyou_note(entry))
        f.close
    print(dir)

def create_report(TableHeader, DonorTable):
    print('\n|{:<{width}s}|{:<{width}s}|{:<{width}s}|{:<{width}s}|'.format(*TableHeader, width = 20))
    print('-------------------------------------------------------------------------------------')
    SortedDonors = sorted(DonorTable, key=DonorSortKey, reverse=True)
    for entry in SortedDonors:
        DonationTotal = sum(DonorTable.get(entry))
        DonationQty = len(DonorTable.get(entry))
        DonationAvg = DonationTotal/DonationQty
        print('|{:<{width}s}|${:<19.2f}|{:<{width}d}|${:<19.2f}|\n'.format(entry, DonationTotal, DonationQty, DonationAvg, width = 20))

def dict_init():
    DonorTable['Jane Doe'] = [10000, 4000, 2000]
    DonorTable['John Doe'] = [10000, 2000, 5000, 3000]
    DonorTable['Bobby Newport'] = [2000, 100]
    DonorTable['Johnny Mnemonic'] = [900, 800, 1000]
    DonorTable['Phillip Dick'] = [2220]

def DonorSortKey(entry):
    return sum(DonorTable.get(entry))

def main():
    while True:
        menu()
        UserInput = input("\nChoice Selected: \n")
        if UserInput == '1':
            send_thankyou(FullName)
        elif UserInput == '2':
            create_report(TableHeader, DonorTable)
        elif UserInput == '3':
            thankyou_print()
        elif UserInput == '4':
            break

if __name__ == "__main__":
    dict_init()
    main()
