donors = list()

donors = [('William Gates, III', [100, 200]),
('Nathan Evoldi', [1000, 2, 120]),
          ('Aaron Judge', [10000]) ]
    # ['Gary Sheffield', [4, 6, 12345]],
    # ['Gary Sanchez', [23]]]

# donors = globals()
# def choose_option():
option = input('Choose an options: \n (1) Send a Thank You \n (2) Create a Report \n (3) Quit \n')
# choose_option()

if option == '1':
    name = input('Full Name: \n---\n')
    if name == 'list':
        for i in donors:
            print(i[0])


    if name.lower() != 'list' and name.lower() not in donors:
        donors.append(name)
        donation_amount = int(input('Enter a Donation Amount: '))
        donors.append(donation_amount)

    def thank_you_email(x, y):
        print(f'Thank you, {name}, for your generous donation of ${donation_amount}.')

    thank_you_email(name, donation_amount)


if option == '2':

    def sort_key(donors):
        print(donors[1])
        return donors[1]

    def report(z):
        donor_summary = []
        header = "{:<25s}| {:<10s} | {:<5s} | {:<5s}".format('Donor Name', 'Total Given', 'Num Gifts', "Average Gifts")
        print('\n')
        print(header)
        print('-'*len(header))

        for i in donors:
            name = i[0]
            total = sum(i[1])
            num = len(i[1])
            avg = total/num
            donor_summary.append([name, total, num, avg])

        donor_summary.sort(key=lambda x: x[1], reverse=True)
        for donor in donor_summary:
            print(f"{donor[0]:<29s}${donor[1]:<15}{donor[2]:<11}{donor[3]:<5}")
        print('\n')
    report(donors)




















