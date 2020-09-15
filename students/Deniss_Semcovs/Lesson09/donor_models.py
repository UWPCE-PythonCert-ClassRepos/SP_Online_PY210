#!/usr/bin/env python3

# This is section with all donor related data
from cli_main import *

class Donor(object):

    def __init__(self, var):
        self.var = var


    def ty_note(self):
        c_data = donor_db
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
            data = donor_db
            if self.var == "list":
                DonorCollection.list()
            elif self.var == "q":
                return
            else:
                for i in data:
                    if self.var == i["name"]:
                        nd = n_don()
                        i["don"].append(nd)
                        print()
                        print("Donation has been submitted! You can see new donation total in the report.")
                        return
                else:
                    add = new_donor()
                    donor_db.append({"name":self.var, "don":[add]})
                    print()
                    print("New donor has been added to the data base, please see report for more information.")
                    print()
        except ValueError:
            valueerror()
        except KeyboardInterrupt:
            keyboardinterrupt()

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
        sort_donor = sorted(donor_db, key = lambda d: sum(d["don"]), reverse = True)
        return sort_donor

donor_db = [{'name': 'Natalie Portman', 'don': [5000]},
           {'name': 'Jennifer Aniston', 'don': [2000, 2000, 2000]},
           {'name': 'Scarlett Johansson', 'don': [1500, 1000]},
           {'name': 'Tom Hanks', 'don': [1000, 500]}, 
           {'name': 'Harrison Ford', 'don': [500, 2000, 100]},
           {'name': 'Leonardo DiCaprio', 'don': [300, 1200, 500]}
           ]

