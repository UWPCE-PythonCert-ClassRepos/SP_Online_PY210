#Mailroom part2 
#update initial code to include dictionaries

import sys

#Functions

#Show list of names
def show_list():
    #print names of donors
    names = list(donor_dict)
    name_string = "\n".join(names)
    print(f"{name_string}")

#Add a new name to the list
def search_name(name):
    donation = input("Please enter an amount to donate >")
    donor_dict.setdefault(name.title,[]).append(float(donation))
    return

#make the program quit
def quit_prog():
    print("Thank you. Goodbye!")
    sys.exit()

#generate an email1
def email(name):
    email = f"\n\nDear {name},\n\n\tWe appreciate your generous donations totalling ${sum(donor_dict[name]):.2f}.\n\nThank you,\nAndrew\n\n" 
    with open(f"Thank_You_to_{name}.txt", 'w+') as f:
        f.write(email)
    return


def nothing():
    print("Invalid response. Please use an appropriate response.")
    return
   
    
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
    
    #Call the search_name function
    search_name(name)
    
    #call the email function
    email = email(name)

def Thank_you_All():
    for name in donor_dict:
        email(name)

#create report inputs   
def report_results():
    tots = []
    aves = []
    nums = []
    for donation_list in donations:        
        tots.append(sum(donation_list))
        aves.append(sum(donation_list)/len(donation_list))
        nums.append(len(donation_list))
    return (tots, aves, nums)

#Create a report
def write_report():
    results = report_results()
    tots = results[0]
    aves = results[1]
    nums = results[2]
    #sort by the totaled values
    sort_by_tot = sorted(tot, reverse=True)
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
    for i in sort_by_tot:
        ind = tot.index(i)
        print(f"{list(Donor_dict.keys())[ind]:<{ln}} ${tot[ind]:>{l-1}}{num[ind]:>{l+1}} ${ave[ind]:>{l-3}.2f}")
    print(f"\n")
    
if __name__ ==  '__main__':
    #Create a database
    Jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
    Ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
    Che = ['Cher', [0.01, 0.01]]
    Aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
    Wan = ['Wan Do Nation', [1.00]]   
    #Combine donors into a database
    database = [Jen, Ste, Che, Aba, Wan]
    #create a dictionary of donor information
    donor_dict = {}
    for name in database:
        donor_dict[name[0]] = name[1]    
    #Create a dictionary to switch between input options
    switch_dict = {
        '1': send_thank_you,
        '2': write_report,
        '3': thank_you_all,
        '4': quit_prog,
        'quit': quit_prog
        }
    
    while True:
        prompt = input("Choose:\n"
                       "1) Send a Thank you\n"
                       "2) Create a Report\n"
                       "3) Send letters to all donors\n"
                       "4) Quit \n"
                       "Respond with 1, 2, 3 or 'quit'>")                       
        switch_dict.get(prompt,"nothing")()