import sys

donors = [
['William Gizzard', [1.00, 123234.12, 80000000]], ['Mark Zhophone', [120000.00]],
['Jeff Binsue', [800.00, 500.00, 50.00]], ['Prince luis', [1.50, 666]],
['Paul Alad', [56743, 300000, 10000000, 88743]],
['mike mixer', [309000, 10000000]]]


menu = '\n'.join(('Please select what you want to do.',
'type 1 to Send a Thank You',
'type 2 to Create a Report',
'type 3 to quit','>>> '))

def thank():
    namelst = [donor[0].lower() for donor in donors]
    name = input("Please enter the donors full name. To check the list of previous donors type list: ")
    print('\n')
    while name.lower() == 'list':
        print('Past Donors:')
        for donor in donors:
            print(donor[0])
        print('\n')
        name = input('Please enter the full name of the donor. If it is a new donor enter their name: ')
        print('\n')

    if name.lower() not in namelst:
        donors.append([name])
        donation = input('How much did {} donate? '.format(name))
        if donation.isnumeric():
            donors[-1].append([int(donation)])

    elif name.lower() in namelst:
        nameposition = namelst.index(name)
        donation = input('How much did {} donate? '.format(name))
        if donation.isnumeric():
            donors[nameposition][1].append(int(donation))
    print('\n')

    email = '''Dear {},

Thank you for your donation of ${}.'''.format(name,donation)
    return print(email)

def report():
    donor_record = [[i[0],sum(i[1]),len(i[1]), sum(i[1])/len(i[1])] for i in donors]
    sorted_donor_record = sorted(donor_record, key=lambda x:-x[1])

    print(f"\n\n{'Name':<16}{'Total Given':<12} {'Num Gifts':<10} {'Average Gift':<14}")
    print("-" * 15 + " " + "-" * 11 + "  " + "-" * 9 + "  " + "-" *13)
    for i in sorted_donor_record:
        print(f"{i[0]:<16}{i[1]:<12.2f} {i[2]:<10} {i[3]:<14.2f}")
    print('\n')

def quit():
    print('Quitting...')
    sys.exit()

if __name__ == '__main__':

    while True:
        response  = input(menu)
        print('\n')

        if response == '1':
            thank()
            print('\n')
        elif response == '2':
            report()
        elif response == '3':
            quit()
        else:
            print('Not a valid option')
            print('\n')
