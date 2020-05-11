#!/usr/bin/env python3
import inquirer
import os
import time

donor1 = {
    "name"        : "Karen",
    "donations"   :  (20,20,100)
}
donor2 = {
    "name"       : "Susan",
    "donations"  :  (20)
}
donor3 = {
    "name"        : "Larry",
    "donations"   :  (40,50)
}
donor4 = {
    "name"        : "Curly",
    "donations"   :  (20.99,20,100)
}
donor5 = {
    "name"        : "Mo",
    "donations"   :  (2)
}

donors = {
  "donor1" : donor1,
  "donor2" : donor2,
  "donor3" : donor3,
  "donor4" : donor4,
  "donor5" : donor5
}

#print(donors)# FOR TESTING

def menu():
    """ Main function """
    while True:
        resp = original_prompt2()
        if resp == '1':
            thanks()
        elif resp == '3':
            thanks_all()
        elif resp == '4':
            print('bye')
            break
        elif resp == '2':
            report()
        else:
            print('input is invalid')
            break

def original_prompt():
    """ Prompt for a user selection """
    questions = [
        inquirer.List('action',
                      message="What would you like to do? ",
                      choices=['Send a Thank You', 'Create a Report', 'quit'])]
    answers = inquirer.prompt(questions)
    return(answers['action'])
  
    
def original_prompt2():  
    answers = input(f"""
Choose an action:

1 - Send a Thank You to a single donor.
2 - Create a Report.
3 - Send letters to all donors.
4 - Quit
""")
    return(answers)

def email(x, y, z):
        
    if z == 0: # case for adding donor
        print ( f"""
Dear {x},

Thank you for your very kind donation of ${y:.2f}
     
It will be put to very good use.

                       Sincerely,
                          -The Team""") 
    if z == 1: #case for sending emails to all who have donated one time
        return ( f"""
Dear {x},

Thank you for your very kind donation of ${y:.2f}
     
It will be put to very good use.

                       Sincerely,
                          -The Team""") 
    
    else: #case for sending emails to all who have donated multiple times
       return(  f"""
Dear {x},

Thank you for your very kind donations totaling ${y:.2f}
     
It will be put to very good use.

                       Sincerely,
                          -The Team""") 


#Thanks!
def thanks():
    """ Prompt for a donor name and amount - then prints email"""
    names = [item[0] for item in donors]
    response1 = input("Please enter a full name ")
    
    if response1 == 'list':
        print(names)
    if response1 == '':
        print('No name entered')
    elif response1 not in names and response1 != 'list':
        response2 = input("Please enter a donation amount ")
        if (response2 == "") or (float(response2) < 0.01):
            print("Please enter a value greater than 0")
        elif float(response2) > 100000:
            print('Please enter a smaller value')
        else:
            new_donor = {"name"        : response1,
                         "donations"   :  float(response2)
                            }
            donors.update( {'donor' + str(len(donors)) : new_donor} )

            email(new_donor['name'], new_donor['donations'], z=0)      

    elif response1 in names:
        response2 = input("Please enter a donation amount ")
        if (response2 == "") or (float(response2) < 0.01):
            print("Please enter a value greater than 0")
        elif float(response2) > 100000:
            print('Please enter a smaller value')
        else:
            filters = [response1 in names for names in donors]
            filters = [i for i, x in enumerate(filters) if x][0]
            wo_d = donors[filters][1]
            response2 = float(response2)
            if(type(wo_d) is tuple):
                w_d = (wo_d) + (response2,)
            else:
                w_d = (wo_d,) + (response2,)
            donors[filters][1] = w_d
            email(response1, response2, z=0)

def thanks_all():
    parent = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #print(donors)
    os.mkdir(timestr)
    for k, v in donors.items():
        filename = os.path.join(parent, timestr + "/" + v['name'] + '.txt')
        #print(filename)
        #print(v)
        if(type(v['donations']) is tuple):
            z = len(v['donations']) # anything but 0 or 1
            tot = sum(v['donations'])
            letter = email(v['name'], tot, z)
            with open(filename, "w") as file:
                file.write(letter)
        else:
            tot = v['donations']
            z = 1
            letter= email(v['name'], tot, z)
            with open(filename, "w") as file:
                file.write(letter)      
    
#Report
def report():
    raw = []
    """ prints a report of donors """
    #print(donors)# FOR TESTING
    col_labels = ["Donor Name",
                  "Total Given",
                  "Num Gifts",
                  "Average Gift"]
    for k, v in donors.items():
        if(type(v['donations']) is tuple):
            tot = sum(v['donations'])
            n = len(v['donations'])
        else:
            tot = v['donations']
            n = 1
        avg = round(tot/n,2)
        raw.append({'name'      : v['name'],
                    'total'     : tot,
                    'number'    : n,
                    'average'   : avg})
    sort_data = (sorted(raw, key = lambda i: i['total']))
    print(f"{col_labels[0]:<30}{col_labels[1]:<15}{col_labels[2]:<15}{col_labels[3]:<5}")
    print("-"*72)
    for i in sort_data:
        print(f"{i['name']:<30}${i['total']:>10.2f}{i['number']:>12}   ${i['average']:>15.2f}")      



if __name__ == '__main__':
    menu()