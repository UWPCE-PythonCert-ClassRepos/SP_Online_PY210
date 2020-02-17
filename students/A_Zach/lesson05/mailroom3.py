import sys
from operator import itemgetter
#Functions

#Show list of names
def show_list():
    #print names of donors
    names = list(donor_dict)
    name_string = "\n".join(names)
    print(f"{name_string}")


#make the program quit
def quit_prog():
    print("Thank you. Goodbye!")
    sys.exit()

#generate an email1
def write_email(name):
    email = f"\n\nDear {name.title()},\n\n\tWe appreciate your generous donations totalling ${sum(donor_dict[name.title()]):.2f}.\n\nThank you,\nAndrew\n\n" 
    with open(f"Thank_You_to_{name.title()}.txt", 'w+') as f:
        f.write(email)

    
def send_thank_you():
    name = input("Who would you like to thank?>")
    if name.lower() == 'quit':
        return
    
    #show the list of names using show_list function
    while name.title() == 'List':
        show_list()
        name = input("Who whould you like to thank?>")
        if name.lower() == 'quit':
            return
    
    donation = input("Please enter an amount to donate >")
    while True:
        #call quit_prog function to end program
        if donation.lower() == 'quit':
            return
        try:
            donor_dict.setdefault(name.title(),[]).append(float(donation))
        except ValueError:
            donation = input(f"\nInvalid response.\n\nEnter a number.\n\nPlease enter an amount to donate >")
        else:
            break
    #call the email function
    write_email(name)
    return

def thank_you_all():
    [write_email(name) for name in donor_dict]


def report_data(name):
    """function generates the number of donations, total amount, and average amount of each donor"""
    names = name
    tots = sum(donor_dict[name])
    nums = len(donor_dict[name])
    aves = tots/nums
    return (name,tots,nums,aves)
 
#Create a report
def write_report():
    report = []
    [report.append(report_data(name)) for name in donor_dict.keys()]
    #sort by the totaled values
    sort_by_tot = sorted(report, key = itemgetter(1), reverse=True)
    #create a variable as the length of each column other than  names. For ease of updating
    l = 15
    #same but for name column
    ln = 25
    #Create a header names
    Headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    #Print header line
    print(f"\n{Headers[0]:<{ln}}|{Headers[1]:^{l}}|{Headers[2]:^{l}}|{Headers[3]:^{l}}")
    print("- "*int((l*3+3+ln)/2))
    #index each entry of sort_by_tot in tot and use that index to generate report
    for entry in sort_by_tot:
        print(f"{entry[0]:<{ln}} ${entry[1]:>{l-1}.2f}{entry[2]:>{l+1}} ${entry[3]:>{l-3}.2f}")
    print(f"\n")
    
#Mailroom part3 
#update mailroom part 2 to include comprehensions and handle exceptions


if __name__ ==  '__main__':
    #Create a database
    jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
    ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
    che = ['Cher', [0.01, 0.01]]
    aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
    juan = ['Juan Doe Nation', [1.00]]   
    #Combine donors into a database
    database = [jen, ste, che, aba, juan]
    #create a dictionary of donor information
    donor_dict = {name[0]: name[1] for name in database}    
    #Create a dictionary to switch between input options
    switch_dict = {
        '1': send_thank_you,
        '2': write_report,
        '3': thank_you_all,
        '4': quit_prog,
        'quit': quit_prog
        }
    
    while True:
        try:
            prompt = input("Choose:\n"
                           "1) Send a Thank you\n"
                           "2) Create a Report\n"
                           "3) Send letters to all donors\n"
                           "4) Quit \n"
                           "Respond with 1, 2, 3 or 'quit'>")                       
            switch_dict.get(prompt)()
        except TypeError:
            print(f"\nInvalid response.\n\n")
