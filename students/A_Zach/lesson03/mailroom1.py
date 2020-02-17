import sys
from operator import itemgetter

#Functions
#Show list of names
def show_list():
    #print names of donors
    for donor in database:
        print(donor[0])

def send_thank_you():
    inp = input("Who whould you like to thank?>")
    if inp.lower() == 'quit':
        return
    #show the list of names using show_list function
    while inp.title() == 'List':
        show_list()
        inp = input("Who whould you like to thank?>")
        if inp.lower() == 'quit':
            return
    donation = input("Please enter an amount to donate >")
    if donation.lower() == 'quit':
        return
    for donor in database:
        if donor[0] == inp.title():
            donor.append(float(donation))
            break
    else:
        database.append([inp.title(), float(donation)])
    
    print(f"\n\nDear {inp.title()},\n\n\tWe appreciate your generous donations.\n\nThank you,\nAndrew\n\n")

#creat report   
def write_report():
    report = []
    for j,donor in enumerate(database):
        names = database[j][0]
        tots = sum(database[j][1:])
        nums = len(database[j]) - 1
        aves = tots/nums
        report.append((names, tots, nums, aves))
    
    sort_by_tot = sorted(report, key = itemgetter(1), reverse=True)
    #create a variable as the length of each column other than  names. For ease of updating
    l = 15
    #same but for name column
    ln = 25
    #Create a header names
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    #Print header line
    print(f"\n{headers[0]:<{ln}}|{headers[1]:^{l}}|{headers[2]:^{l}}|{headers[3]:^{l}}")
    print("- "*int((l*3+3+ln)/2))
    #index each entry of sort_by_tot in tot and use that index to generate report
    for entry in sort_by_tot:
        print(f"{entry[0]:<{ln}} ${entry[1]:>{l-1}}{entry[2]:>{l+1}} ${entry[3]:>{l-3}.2f}")
    print(f"\n")
    
#Mailroom part 1
#Generate a database of donors


if __name__ == '__main__':
    #Create a database
    jen = ['Jenny Jones', 272.00, 8700.11, 4.22]
    ste = ['Steve Martin', 85000.00, 12345.67, 54321.99]
    che = ['Cher', 0.01, 0.01]
    aba = ['Aba Ababa', 101.01, 10101.01, 1100.10]
    juan = ['Juan Doe Nation', 1.00]   
    #Combine donors into a database
    database = [jen, ste, che, aba, juan]

    #iterate until 1, 2, or quit is chosen. then call the appropriate function
    while True:
        prompt = input("Choose:\n1) Send a Thank you\n2) Create a "
                       "Report\n3) Quit \nRespond with 1, 2 or 'quit'>")    
        if prompt == '1':
            send_thank_you()
        elif prompt == '2':
            write_report()
        elif prompt == '3' or prompt.lower() == 'quit':
            print("Thank you. Goodbye!")
            sys.exit()
        else:
            print(f"'{prompt}' is an invalid entry")
            
        

