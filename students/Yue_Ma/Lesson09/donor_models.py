### Yue Ma


class Donor(object):
    def __init__(self, donor_name, new_donation=None):
        self.name = donor_name

        if new_donation is None:
            self.donation = []
        else:
            self.donation = list(new_donation)

    def add_donation(self, new_donation):
        updated_donation = self.donation.append(new_donation)
        return updated_donation

    @property
    def count_donation(self):
        number_of_donation = len(self.donation)
        return number_of_donation

    @property
    def total_donation(self):
        total_donation = sum(self.donation)
        return total_donation

    @property
    def average_donation(self):
        average_donation = self.total_donation / self.count_donation
        return average_donation

    def __lt__(self, other):
        return self.total_donation < other.total_donation

    def __eq__(self, other):
        return self.name == other.name


class DonorCollection:
    def __init__(self):
        self.donor_list = [Donor('Yue Ma', [100000, 1561132]),
                           Donor('Yanan Ma', [1000, 5645, 6161, 27]),
                           Donor('Jianqiang Ma', [200000, 854821, 1202]),
                           Donor('Chunhong Liu', [100.51, 1000.1]),
                           Donor('Robert Rowe', [20000000])]

    def try_donor(self, donor_name):
        for item in self.donor_list:
            if item.name == donor_name:
                return donor_name
        else:
            return None

    def add_a_donor(self, donor_name, new_donation):
        new_donor_list = Donor(donor_name, [new_donation])
        self.donor_list.append(new_donor_list)
        return new_donor_list

    def add_new_donation(self, donor_name, new_donation):
        for donor in self.donor_list:
            if donor_name == donor.name:
                donor.add_donation(new_donation)

    def create_report(self):
        title = {'Donor Name': ['Total Given', 'Num Gifts', 'Average Gift']}
        value_title = list(title.values())
        key_title = list(title.keys())

        # sort
        self.donor_list.sort(reverse=True)

        # Print the report
        line_title = f'| {key_title[0]:<20}| {value_title[0][0]:<15} | {value_title[0][1]:<10} | {value_title[0][2]:<15}|'
        line_x = '|' + '-' * 69 + '|'
        line_1 = ' ' + '-' * 69 + ' '

        report = [line_1, line_title, line_x]
        for item in self.donor_list:
            main_lines = f'| {item.name:<20}| {item.total_donation:<15.2f} | {item.count_donation:<10} ' \
                         f'| {item.average_donation:<15.2f}|'
            report.append(main_lines)
        report.append(line_1)
        return report

    def send_letters_to_all_donor(self):
        for item in self.donor_list:
            file_name = '{}.txt'.format(item.name.replace(' ', '_'))
            file = open(file_name, 'w')
            file.write(f'\n' + f'Dear {item.name},\n\nThank you for your donation{item.total_donation}! '
                               f'It will be put to very good use!!!\n\nSincerely, \nThe Donation Team \n')
        print('file saved')

    def get_donor_list(self):
        show_donor_list = []
        for item in self.donor_list:
            show_donor_list.append(item.name)
        return show_donor_list

