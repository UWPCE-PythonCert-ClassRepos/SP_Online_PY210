import sys
from operator import itemgetter

#Functions

#Show list of names
def show_list():
    """print names of donors"""
    names = list(dict)
    name_string = "\n".join(names)
    name_list = f"{name_string}"
    print(name_list)
    return name_list

def send_thank_you():
    """Finds name of who should be thanked, calls donation and email functions"""
    name = input("Who would you like to thank?>")
    if name.lower() == 'quit':
        return
    
    #show the list of names using show_list function
    while name.title() == 'List':
        show_list(donor_dict)
        name = input("Who whould you like to thank?>")
        if name.lower() == 'quit':
            return
    donation = input("Please enter an amount to donate >")
    #call add_donation function
    donation = add_donation(name, donor_dict, donation)
    if donation.lower() == 'quit':
        return
    #call the email function
    write_email(name, donor_dict)


def add_donation(name, dict, donation):
    """adds new donation to existing name, or adds name and donation if name isn't existing"""
    while True:
        #call quit_prog function to end program
        if donation.lower() == 'quit':
            return donation
        try:
            dict.setdefault(name.title(),[]).append(float(donation))
        except ValueError:
            donation = input(f"\nInvalid response.\n\nEnter a number.\n\nPlease enter an amount to donate >")
        else:
            break
    return dict

# make the program quit


def quit_prog():
    """quits program"""
    print("Thank you. Goodbye!")
    sys.exit()

# generate an email1


def write_email(name, dict):
    """writes email to a text file thanking a given donor"""
    email = f"\n\nDear {name},\n\n\tWe appreciate your generous donations totaling ${sum(dict[name]):.2f}.\n\nThank you,\nAndrew\n\n" 
    with open(f"Thank_You_to_{name}.txt", 'w+') as f:
        f.write(email)
    return email


def thank_you_all(dict):
    """writes a thank you email for all donors"""
    [email(name) for name in dict]


# Create a report

def report_data(name, dict):
    """function generates the number of donations, total amount, and average amount of each donor"""
    names = name
    tots = sum(dict[name])
    nums = len(dict[name])
    aves = tots/nums
    return name, tots, nums, aves


def build_report(dict):
    report = []
    [report.append(report_data(name, dict)) for name in dict.keys()]
    # sort by the totaled values
    sort_by_tot = sorted(report, key = itemgetter(1), reverse=True)
    return sort_by_tot


def write_report():
    # create a variable as the length of each column other than  names. For ease of updating
    l = 15
    # same but for name column
    ln = 25
    #Create header names
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    #Print header line
    print(f"\n{headers[0]:<{ln}}|{headers[1]:^{l}}|{headers[2]:^{l}}|{headers[3]:^{l}}")
    print("- "*int((l*3+3+ln)/2))
    report = build_report(donor_dict)
    for name,total,donations,average in report:
        print(f"{name:<{ln}} ${total:>{l-1}.2f}{donations:>{l+1}} ${average:>{l-3}.2f}")


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
            switch_dict.get(prompt,"nothing")()
        except TypeError:
            print(f"\nInvalid response.\n\n")
