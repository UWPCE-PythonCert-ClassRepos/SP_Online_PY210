# send a thank you
def thanks(donors):
    repeat = True
    while repeat:
        # name of donors
        names = []
        for i in range(len(donors)):
            names.append(donors[i][0])
        name = input('Enter full name: ')
        if name == 'list':
            print(' '.join(names))
        elif name in names:
            amt = int(input('Enter a amount to donate: '))
            donors[names.index(name)].append(amt)
            # email
            print('''
                    Dear {0},
                    Thank you for your donation.
                    '''.format(name))
            repeat = False
        else:
            repeat = False
            donors.append([name])
    return donors

# report
def report(donors):
    # using list comprehension
    report_listing = [[donors[i][0], len(donors[i][1:]), sum(donors[i][1:]), (sum(donors[i][1:])/len(donors[i][1:]))] for i in range(len(donors))]
    print(report_listing)
    # sorting the array based on average donation
    sorted_report = sorted(report_listing[:], key=lambda x: x[3], reverse=True)
    # printing report
    print('Donor Name'.ljust(15, " "), 'Total Given'.ljust(15, " "), 'Num Gifts'.ljust(10, " "),
          "Average Gift".ljust(10, " "))
    j = 0
    while j < len(sorted_report):
        total_given = str('{:.2f}'.format(sorted_report[j][2]))
        num_gifts = str(sorted_report[j][1])
        avg_gift = str('{:.2f}'.format(sorted_report[j][3]))
        print(sorted_report[j][0].ljust(15, " "), total_given.ljust(15, " "), num_gifts.ljust(10, " "),
              avg_gift.ljust(5, " "))
        j += 1


if __name__ == '__main__':
    # initial set of donors
    donors = [
        ['Adam A', 100, 200],
        ['Betty B', 100, 200, 200],
        ['Carl C', 100],
        ['Ed E', 50,100,25],
        ['Frank F', 50]
    ]
    request_flag = True
    # using try and except
    while request_flag:
        try:
            request = int(input('Choose from following three items: \n'
                    'Enter 1 for sending a Thank You \n'
                    'Enter 2 for creating a report \n'
                    'Enter 3 for quit \n'
                    ''))
        # when user enter non-int entries
        except ValueError:
            print('Enter numbers 1, 2 or 3 only.')
        else:
            if request == 3:
                request_flag = False
            elif request == 2:
                report(donors)
            elif request == 1:
                thanks(donors)
                request_flag = False
            else:
                print('Enter from given options only.')
