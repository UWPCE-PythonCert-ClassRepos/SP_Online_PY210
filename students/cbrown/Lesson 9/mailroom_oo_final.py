import sys


class Donor_Collection():

    donor_dict = {"Bill Gates": [539000, 235642],
          "Jeff Bezos": [108356, 204295, 897345],
          "Satya Nadella": [236000, 305352],
          "Mark Zuckerberg": [153956.35],
          "Mark Cuban":[459035, 369.50, 570.89]}

    def __init__(self, donor=None):
        self.donor = donor

    def update_donor(self):
        self.donor_dict.get(self.donor.name).append(self.donor.amount)

    def add_donor(self):
        self.donor_dict[self.donor.name] = [self.donor.amount]

    # method for sorting key
    def sum_value(self, donations):
        item = donations[1]
        return sum(item)

    def sort_donors(self):
        return sorted(self.donor_dict.items(), key=self.sum_value, reverse=True)


class Donor():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def sum_amount(self):
        total_donated = sum(self.amount)
        return total_donated


prompt = "\n".join(("Please Select from Items Below:",
                    "1 - Send A Thank You",
                    "2 - Create A Report",
                    "3 - Send Letters to All Donors",
                    "4 - Quit",
                    " "))


def exit_from():
    '''quits the program for the user'''

    print('Work Completed. Good Bye!')
    sys.exit()


def donor_verify(donor):
    '''
    Checks to see if the requested donor is in the donor_collection dict. Updates new
    donation if name not found
    '''
    #instantiates donor_collection class
    donor_collection = Donor_Collection(donor)

    #adds donation amount if donor_name is in database already
    if donor.name in donor_collection.donor_dict:
        donor_collection.update_donor()

    #creates new donor entry if not found
    else:
        donor_collection.add_donor()


def thank_you_note(donor):
    '''
    Creates thank you message for an individual donor
    '''
    thanks_dict = {'donor_name': donor.name, 'amount': donor.amount}

    # Formatted Thank You Note
    message = ('Dear {donor_name}, \n\nThank you for your show of support and generosity. '
      'Your Donation of ${amount} will contribute to saving Olympic Marmots '
      'in Washington State. These Marmota are special and a unique gift to the Olympic '
      'National Park ecosystem. As a way of saying thank you. '
      'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
      'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n').format(**thanks_dict)

    return message


def send_thanks():
    '''
    Adds new donations and new donors. Prints out message to individual donors.
    '''
    print('\n', "For A Complete Donor List Type 'List'\n ")

    #Displays the list of current donors for the user if requested
    while True:
        donor_name = input("What donor(s) are you looking for?\n ").title()
        if donor_name == 'List':
            print('\n', "Here is A Complete List of Donor Names\n ")
            donor_list = [donor for donor in Donor_Collection.donor_dict.keys()]
            print(donor_list)
        else:
            break

    # prompt for donation amount
    try:
        amount = float(input("How Much Did This Person Donate?\n "))

    except ValueError:  #start prompt over again if exception occurs
        print('Please input a numeric amount & try again.')
        send_thanks()

    #Creates new instance of donor
    donor = Donor(donor_name, amount)

    # updates donor database & adds new ones if a name does not exist
    donor_verify(donor)

    # formats message thanking the individual donor
    message = thank_you_note(donor)

    print(message)


def create_message(donor):
    '''
    Creates a personalized & formatted message for each donor
    '''
    tmt_amount = donor.sum_amount()

    message = ('Dear {}, \n\nThank you for your show of support and generosity. '
        'Your donations totaling ${:,.1f} will contribute to saving Olympic Marmots '
        'in Washington State. These Marmota are special and a unique gift to the Olympic '
        'National Park ecosystem. As a way of saying thank you. '
        'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
        'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n').format(donor.name, tmt_amount)

    return message


def write_file(name, message):
    '''
    Creates a text file of each thank you message for each donor
    '''
    fname = name + '.txt'
    with open(fname, 'w') as f:
        f.write(message)


def send_letters():
    '''
    creates and writes a letter to each donor in the donor database
    '''
    for name, amount in Donor_Collection.donor_dict.items():
        donor = Donor(name, amount)

        message = create_message(donor)

        write_file(donor.name, message)


def report_rows(name, amounts):
    '''
    Creates formatted row for every donor. For use in create_report
    '''
    total_given = sum(amounts)
    num_gift = len(amounts)
    avg_gift = total_given/num_gift

    total_given = '{:,.0f}'.format(total_given)
    avg_gift = '{:,.0f}'.format(avg_gift)
    row = '{:<25}${:^15}{:^15}${:^15}'.format(name, total_given, num_gift, avg_gift)

    return row


def print_report(report_lines):
    '''
    Prints the output of the donor report using data generated from report_rows function & report_lines list
    '''
    # prints the header of the report
    print('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    str_len = len('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    print('-' * str_len)

    # prints name, total, num of gifts, and avg gift
    for row in report_lines:
        print(row)


def create_report():
    '''
    Creates the data used in donor reports
    '''
    donor_collection = Donor_Collection()

    # create a sorted donations dict by total amount
    sorted_donations = donor_collection.sort_donors()

    report_lines = []

    for k, v in sorted_donations:
        report_lines.append(report_rows(k, v))

    print_report(report_lines)


response_dict = {"1": send_thanks,"2": create_report, "3": send_letters, "4": exit_from}


def main():
    while True:
        try:
            response = input(prompt)
            response_dict.get(response)()

        except TypeError:
            print('The choice you have selected is not an option. Please select from the menu.')
            continue


if __name__ == "__main__":
    main()
