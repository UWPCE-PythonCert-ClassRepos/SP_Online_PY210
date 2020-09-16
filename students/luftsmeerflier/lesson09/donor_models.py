# NOTE! This is not comprehensive, just showing some methods and properties of the classes (full solution would expand on attributes/methods as needed)

class Donor:
    def __init__(self, name, donation, date):
        self.name = name
        self.donations = [(donation, date)]

    def add_donation(self, donation, date):
        self.donations.append((donation, date))

    @property
    def num_donations(self):
        all_donations = [d[0] for d in self.donations]
        return len(all_donations)

    @property
    def sum_donations(self):
        total = sum([d[0] for d in self.donations])
        return total

    def get_thank_you_letter(self):
        template = "Dear {},\n\n    Thank you for your donation in the amount of ${} on {}. Please keep this letter for your records.\n\n"
        index = len(self.donations) - 1
        completed_letter = template.format(self.name, self.donations[index][0], self.donations[index][1])
        file_name = "{}.txt".format(self.name).replace(" ", "_")
        thank_you_letter = open("{}".format(file_name), "w+")
        thank_you_letter.write(completed_letter)
        thank_you_letter.close()
        print("\nThank you letter has been created for {}\n".format(self.name))


class DonorCollection:
    def __init__(self, *args):
        self.donors = {d.name: d for d in args}

    def send_thank_you(self, name):
        if self.donors.get(name):
            self.donors[name].get_thank_you_letter()
        else:
            print("Donor not found")

    def send_letters(self):
        for donor_obj in self.donors.values():
            donor_obj.get_thank_you_letter()

    def add_donation(self, name, donation, date):
        if self.donors.get(name):
            self.donors[name].add_donation(donation, date)
        else:
            self.donors[name] = Donor(name, donation, date)
        #self.donors[name].get_thank_you_letter()
    def get_report(self):
        heading = "Donor Name".ljust(28) + '|'.ljust(2) + "Total Given" + '|'.rjust(2) + "Num Gifts".rjust(10) + "|".ljust(2) + "Average Gift"

        print(heading)

        for donor_obj in self.donors.values():
            total = donor_obj.sum_donations
            count_donations = donor_obj.num_donations
            average = int(total / count_donations)

            print((donor_obj.name).ljust(30) + '$'.ljust(2) + str(total).ljust(15) + str(count_donations).ljust(10) + '$'.ljust(2) + str(round(average, 2)))



