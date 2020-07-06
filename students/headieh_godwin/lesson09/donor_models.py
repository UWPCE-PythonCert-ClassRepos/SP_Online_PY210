import os
import time

class Donor:
    """
    Class responsible for donor data encapsulation
    """

    def __init__(self, name):
        self.name = name
        self.donations = []

    @property
    def d_num(self):
        """number of donations"""
        return len(self.donations)

    @property
    def d_tot(self):
        """sum of donations"""
        return sum(self.donations)

    @property
    def d_avg(self):
        """average donation"""

        if self.d_num == 0:
            return 0
        else:
            return (self.d_tot/self.d_num)

    def add_donation(self, *args):
        """add donation amount to a donor object"""
        for i in args:
            self.donations.append(i)

    def send_thank_you(self, money_amount):
        """Sends a thank you when donation is made"""
        return f"""
Dear {self.name},

Thank you for your very kind donation of ${money_amount:.2f}

It will be put to very good use.

Sincerely,
-The Team"""

    def __lt__(self, other):
        """sorts order"""
        return self.total_donation < other.total_donation

    def __repr__(self):
        return self.name


class DonorCollection:

    """
    Class responsible for donor collection data encapsulation
    """

    def __init__(self, donors=[]):
        """Create a collection of donors"""
        self.donor_obs_list = donors

    @property
    def list_donors(self):
        """Return a list of all donors"""
        return self.donor_obs_list

    @list_donors.setter
    def list_donors(self, donors = []):
        self.donor_obs_list.extend(donors)

    def add_donors(self, *args):
        """Add a donor to the collection."""
        self.list_donors.extend(args)
        return self.list_donors

    def __repr__(self):
        names = [donor.name for donor in self.list_donors]
        return ', '.join(names)


    def thanks_all(self):
        parent = os.getcwd()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.mkdir(timestr)
        for k in self.list_donors:
            filename = os.path.join(parent, timestr + "/" + k.name + '.txt')
            with open(filename, 'w') as file:
                file.write(self.write_thanks_all(k.name, k.d_tot, k.d_num))
        print("Letters have been outputted for all donors")

    def write_thanks_all(self, name, total,numb):
        mass_text_1 = f"""
        Dear {name},

        Thank you for your very kind donation of ${total:.2f}

        It will be put to very good use.

                               Sincerely,
                                  -The Team"""

        mass_text_2 = f"""
        Dear {name},

        Thank you for your very kind donations totaling ${total:.2f}

        It will be put to very good use.

                               Sincerely,
                                  -The Team"""

        if numb == 1:
            return mass_text_1
        else:
            return mass_text_2


    def report(self):

        raw =[]
        raw_temp=[]
        """ prints a report of donors - revisit and recode this (sort data)"""
        col_labels = ["Donor Name",
                      "Total Given",
                      "Num Gifts",
                      "Average Gift"]
        header =f"{col_labels[0]:<30}{col_labels[1]:<15}{col_labels[2]:<15}{col_labels[3]:<5}"
        raw.append(header)
        raw.append('\n')
        raw.append('-'*len(header))
        raw.append('\n')

        for this_ob in self.list_donors:
            name = this_ob.name
            num = this_ob.d_num
            total= this_ob.d_tot
            aveg = this_ob.d_avg
            raw_temp.append({'name': name,
                        'total': total,
                        'number': num,
                        'average': aveg})

        sort_data = (sorted(raw_temp, key = lambda i: i['total'], reverse=True))

        for i in sort_data:
            raw.append(f"{i['name']:<30}${i['total']:>10.2f}{i['number']:>12}   ${i['average']:>15.2f}")
            raw.append('\n')
        return "".join(raw)
