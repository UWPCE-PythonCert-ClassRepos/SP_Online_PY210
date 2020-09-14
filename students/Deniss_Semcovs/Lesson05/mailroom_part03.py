#!/usr/bin/env python3

import tempfile
import os.path

# KeyError exception added
def mailroom02(reply, action):
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
#    new_data = dict_donor()
    [print(i["name"]) for i in sort_donor]

# KeyError and KeyboardInterrupt exceptions added
def add_donation():
    while True:
        full_name = str(input("Please enter 'list' to view donor names or 'q' to quit or full name of the donor: "))
        if full_name == "list":
            print_list()
        elif full_name == "q":
            break
        else:
            for i in sort_donor:
                if full_name == i["name"]:
                    i["don"].append(int(input("Please enter the donation amount: ")))            
                    print()
                    print("Donation has been submitted! You can see new donation total in the report.")
                    break          
            else:
                try:
                    new_donation = int(input("This is a new donor, please enter the donation amount: "))
                    if new_donation is None or False:
                        pass
                    else:
                        sort_donor.append({"name":full_name, "don":[new_donation]})
                        print("Letter for the donor: ")
                        print()
                        print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(full_name, new_donation))
                    break
                except (ValueError):
                    valueerror()
                except KeyboardInterrupt:
                    keyboardinterrupt()

def create_report():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    for i in sort_donor:
        data2 = (i["name"], sum(i["don"]), len(i["don"]), (sum(i["don"]))/(len(i["don"])))
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

def send_ty_note_all():
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

def send_ty_note():
    try:
        don_name = input("Enter donor's name: ")
        for i in sort_donor:
            if don_name == i["name"]:
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(i['name'], (sum(i["don"]))))
                break

        else:
            print()
            print("The donor's name is not on the list! Please add a new donor through 'Add new donation' option.")
                
    except KeyboardInterrupt:
        keyboardinterrupt()

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

donor_db = [{'name': 'Natalie Portman', 'don': [5000]},
         {'name': 'Jennifer Aniston', 'don': [2000, 2000, 2000]},
         {'name': 'Scarlett Johansson', 'don': [1500, 1000]},
         {'name': 'Tom Hanks', 'don': [1000, 500]}, 
         {'name': 'Harrison Ford', 'don': [500, 2000, 100]},
         {'name': 'Leonardo DiCaprio', 'don': [300, 1200, 500]}
         ]

sort_donor = sorted(donor_db, key = lambda d: sum(d["don"]), reverse = True)

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

if __name__=="__main__":
    mailroom02(main_reply, main_action)


