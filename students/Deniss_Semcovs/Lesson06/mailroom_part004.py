#!/usr/bin/env python3

import tempfile
import os.path

# KeyError exception added
def mailroom04(reply, action):
    while True:
        try:
            resp = input(reply)
            if action[resp]() is None or False:
                pass
            elif action[resp]() == "exit menu":
                break
        except KeyError:
            keyerror()
        except KeyboardInterrupt:
            keyboardinterrupt()

# Complerssed "list"
def print_list():
    sorted_donor = sorted_db()
    [print(i["name"]) for i in sorted_donor]

# add_donation() input function
def add_donation():
    print()
    full_name = str(input("Please enter 'list' to view donor names or 'q' to quit or full name of the donor: "))
    new_donation(full_name)
# add_donation() logic code + input
def new_donation(full_name):
    try:
        if full_name == "list":
            print_list()
        elif full_name == "q":
            return
        else:
            for i in donor_db:
                if full_name == i["name"]:
                    i["don"].append(int(input("Please enter the donation amount: ")))            
                    print()
                    print("Donation has been submitted! You can see new donation total in the report.")
                    return
            else:
                new_donar(full_name)
    except ValueError:
        valueerror()
    except KeyboardInterrupt:
        keyboardinterrupt()
# new_donar() input function
def new_donar(name):
    print()
    new_don = int(input("This is a new donor, please enter the donation amount or 'q' to exit: "))
    if new_don == "q":
        return
    else:
        adding_donor(name, new_don)

# new_donor() logic code
def adding_donor(full_name, new_don):
    if new_don is None or False:
        pass
    else:
        donor_db.append({"name":full_name, "don":[new_don]})
        print()
        print("Letter for the donor: ")
        print()
        print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(full_name, new_don))
        return

def create_report():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    report_data()

def report_data():
    sorted_donor = sorted_db()
    for i in sorted_donor:
        data2 = (i["name"], sum(i["don"]), len(i["don"]), (sum(i["don"]))/(len(i["don"])))
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

# create files
def send_ty_note_all():
    sort_donor = sorted_db()
    for i in sort_donor:
        letter_file = os.path.join(tempfile.gettempdir(), (i["name"]+".txt"))
        with open(letter_file, "w") as f:
            f.write("\nDear "+i["name"]+",")
            f.write("\n"*2)
            f.write(" "*8+"Thank you for your very kind donation of $"+str(sum(i["don"]))+".")
            f.write("\n"*2)
            f.write(" "*8+"It will be put to very good use.")
            f.write("\n"*2)
            f.write(30*" "+"Sincerely,")
            f.write(34*" "+"-The Team")
    print("<<< Letters have been created in the temp folder! >>>")


def quit():
    return "exit menu"

#send_ty_note() input function
def send_ty_note():
    try:
        don_name = input("Enter donor's name: ")
        ty_note(don_name)              
    except KeyboardInterrupt:
        keyboardinterrupt()
#send_ty_note() logic code
def ty_note(var):
#    sort_donor = sorted_db()
    for i in donor_db:
        if var == i["name"]:
            print()
            print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(i['name'], (sum(i["don"]))))
    else:
        print()
        print("The name you entered is not on the list!")
        return



def valueerror():
    print()
    print("The donation amount has been incorrect or not entered.")
    print()

def keyerror():
    print()
    print("Wrong entery, please try again!")
    
def keyboardinterrupt():
    print()
    print("Keyboard interrupt doesn't work here ;)")
    print("please use apropriate method to exit this program")
    print(">>>> Hint: 'q'")

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



"""
# Generating dictionary data from the list
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

main_reply = ("\nChoose an action: \n"
               "\n"
			   "1 - Send a Thank You note to a single donor.\n"
			   "2 - Add new donation.\n"
			   "3 - Create a Report.\n"
			   "4 - Send letters to all donors.\n"
			   "5 - To see the LIST of donor names.\n"
			   "q - Quit\n"			   
			   ">>>")

main_action = {"1" : send_ty_note,
               "2" : add_donation,
               "3" : create_report,
               "4" : send_ty_note_all,
               "5" : print_list,
               "q" : quit
               }

if __name__ == "__main__":
    mailroom04(main_reply, main_action)


