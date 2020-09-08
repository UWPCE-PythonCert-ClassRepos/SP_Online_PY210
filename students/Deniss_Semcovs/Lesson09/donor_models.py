#!/usr/bin/env python3

# This is section with all donor related data
from cli_main import *

class Donor(object):

    def __init__(self, var, **kwargs):
        self.var = (var)
        self.kwargs = (kwargs)


    # adding donations method
    def adding_donation(self):
        (self.var).append(kwargs)
        print()
        print("Donation has been submitted! You can see new donation total in the report.")

    def ty_note(self):
        c_data = DonorCollection.donor_db
        for i in c_data:
            if self.var == i["name"]:
                print()
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(i['name'], (sum(i["don"]))))
                return
        else:
            print()
            print("Entered >> "+(self.var))
            print()
            print("The name you entered is not on the list!")
            return

    def new_donation(self):
        try:
            data = DonorCollection.donor_db
            if self.var == "list":
                DonorCollection.list()
            elif self.var == "q":
                return
            else:
                for i in data:
                    if self.var == i["name"]:
                        n_don()
#                        nd = return(n_don())
                        nd = n_don
                        print(nd)

#                        Donor.up_donor(self.var, nd)
                        DonorCollection.donor_db.append({"name":self.var, "don":[nd]})
#                        n_don = int(input("Please enter the donation amount: "))
#                        Donor.adding_donation(i[0])
#                        i.append(int(input("Please enter the donation amount: ")))            
                        print("Donation has been submitted! You can see new donation total in the report.")
                        return
                else:
                    new_donor(self.var)

        except ValueError:
            valueerror()
        except KeyboardInterrupt:
            keyboardinterrupt()

    def up_donor(self, nd):
#        n = self.var[0]
#        d = self.var[1]
        DonorCollection.donor_db.append({"name":self.var, "don":[nd]})

    def add_n_don(self, var, kwargs):
        n_data = DonorCollection.donor_db
        if new_don == "q":
            print()
            print("Exiting!")
            return
#        else:
#            Donor.adding_donor(full_name, new_don)
#    def adding_donor(self, var, kwargs):
#            n_data = DonorCollection.donor_db
        elif self.var is None:
                pass
        else:
            n_data.append({"name":self.var, "don":[self.kwargs]})
            print()
            print("Letter for the donor: ")
            print()
            print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(self.var, self.kwargs))
#        return



class DonorCollection(Donor):

    def list():
        new_data = DonorCollection.sorted_db()
        print()
        [print(i["name"]) for i in new_data]

    def report():
        tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
        print(("-")*61)
        DonorCollection.report_data()

    def report_data():
        new_data = DonorCollection.sorted_db()
        for i in new_data:
            data2 = (i["name"], sum(i["don"]), len(i["don"]), (sum(i["don"]))/(len(i["don"])))
            print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

    def sorted_db():
        sort_donor = sorted(DonorCollection.donor_db, key = lambda d: sum(d["don"]), reverse = True)
        return sort_donor

    donor_db = [{'name': 'Natalie Portman', 'don': [5000]},
             {'name': 'Jennifer Aniston', 'don': [2000, 2000, 2000]},
             {'name': 'Scarlett Johansson', 'don': [1500, 1000]},
             {'name': 'Tom Hanks', 'don': [1000, 500]}, 
             {'name': 'Harrison Ford', 'don': [500, 2000, 100]},
             {'name': 'Leonardo DiCaprio', 'don': [300, 1200, 500]}
             ]


"""

# Creating dict list from list "data"
    def dict_donor():
        donor = [{"name" : i[0], "don" : sum(i[1:]), "count" : len(i[1:]), "average" : ((sum(i[1:]))/(len(i[1:])))} for i in data]
        sort_donor = sorted(donor, key = lambda d: d["don"], reverse = True)
        return sort_donor

data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]

"""




















