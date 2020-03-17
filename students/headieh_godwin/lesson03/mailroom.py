#!/usr/bin/env python3
import inquirer

donors = [['Karen', (20,20,100)],
    ['Susan', (20)],
    ['Larry', (40,50)],
    ['Curly', (20.99,20,100)],
    ['Mo', (2)]]
#print(donors) FOR TESTING

def menu():
    """ Main function """
    while True:
        resp = original_prompt()
        if resp == 'Send a Thank You':
            thanks()
        elif resp == 'quit':
            print('bye')
            break
        elif resp == 'Create a Report':
            report()
        else:
            print('Something went wrong')
            break

def original_prompt():
    """ Prompt for a user selection """
    questions = [
        inquirer.List('action',
                      message="What would you like to do? ",
                      choices=['Send a Thank You', 'Create a Report', 'quit'])]
    answers = inquirer.prompt(questions)
    return(answers['action'])

def email(x,y):
    print( f"""
Dear {x},

Thank you for your generous donation of ${y:.2f}
     
Kind Regards""")

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
        #response2 = int(response2)
        if (response2 == "") or (float(response2) < 0.01):
            print("Please enter a value greater than 0")
        elif float(response2) > 100000:
            print('Please enter a smaller value')
        else:
            new_donor = [response1, float(response2)]
            donors.append(new_donor)
            email(new_donor[0],new_donor[1])

    elif response1 in names:
        response2 = input("Please enter a donation amount ")
        #response2 = int(response2)
        if (response2 == "") or (float(response2) < 0.01):
            print("Please enter a value greater than 0")
        elif float(response2) > 100000:
            print('Please enter a smaller value')
        else:
            filters = [response1 in names for names in donors]
            filters = [i for i, x in enumerate(filters) if x][0]
            wo_d = donors[filters][1]
            response2= float(response2)
            if(type(wo_d) is tuple):
                w_d = (wo_d)+(response2,)
            else:
                w_d = (wo_d,)+(response2,)
            donors[filters][1]=w_d
            email(response1, response2)

#Report
def report():
    """ prints a report of donors """
    #print(donors) FOR TESTING
    col_labels=["Donor Name","Total Given","Num Gifts", "Average Gift"]
    print(f"{col_labels[0]:<30}{col_labels[1]:<15}{col_labels[2]:<15}{col_labels[3]:<5}")
    print("-"*72)
    for i in donors:
        if(type(i[1]) is tuple):
            tot = sum(i[1])
            n = len(i[1])
        else:
            tot = i[1]
            n = 1
        avg = round(tot/n,2)
        print(f"{i[0]:<30}${tot:>10.2f}{n:>12}   ${avg:>15.2f}")      



if __name__ == '__main__':
    menu()