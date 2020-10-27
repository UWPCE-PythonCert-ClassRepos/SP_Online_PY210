import sys

class DonorCollection(object):
    donor_db = [("William Gates, III", [653772.32, 12.17]),
                ("Jeff Bezos", [877.33]),
                ("Paul Allen", [663.23, 43.87, 1.32]),
                ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),]


    def __init__(self, full_name ="", donation_amount = 0, donor_db = donor_db):
        self.full_name = full_name
        self.donation_amount = donation_amount
        self.donor_db = donor_db

    def report_list(self):
        # l = (["Donor Name", "Total Given", "Num Gifts", "Average Gift"])
        r_list = []
        for i in self.donor_db:
            r_list.append(i[0])
            ng = 0
            tg = 0
            for j in i[1]:
                tg += j
                ng += 1
            r_list.append(str(tg))
            r_list.append(str(ng))
            ag = tg/ng
            r_list.append(str(ag))

        return r_list


    def update_donor_db(self, full_name, donation_amount):
        m = 0
        for i in self.donor_db:
            m += 1
            if full_name == i[0]:
                i[1].append(donation_amount)
                m = 0
                break
        if m > 0:
            new_donor = (full_name,[donation_amount],)
            return self.donor_db.append(new_donor)


    def name_list(self):
        name_list = []
        [name_list.append(i[0]) for i in self.donor_db]
        return sorted(name_list, key = lambda i: i[0])


    def __repr__(self):
        return "DonorCollection({})".format(self.donor_db)




class Donor(object):
    def __init__(self, full_name="", donation_amount =0):
        self.full_name = full_name
        self.donation_amount = donation_amount

    def __repr__(self):
        return "({}, [{}])".format(self.full_name, self.donation_amount)

    def generate_letter(self):
        l1 = self.full_name.split()
        try:
            first_name = l1[0].upper()
        except:
            first_name = ""
        try:
            last_name = l1[1].upper()
        except:
            last_name = ""

        template = """Dear {first_name} {last_name},
        Thank you for your very kind donation of ${donation_amount}
        It will be put to very good use.
            Sincerely,
                -The Team"""

        letter_data ={"first_name": first_name, "last_name": last_name, "donation_amount": self.donation_amount}
        file_name = f"{first_name}_{last_name}.txt"
        with open(file_name, "w") as fp:
            fp.write(template.format(**letter_data))
