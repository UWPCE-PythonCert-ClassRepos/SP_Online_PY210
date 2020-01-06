import sys

#Functions

#Show list of names
def show_list(dict):
    #print names of donors
    names = list(dict)
    name_string = "\n".join(names)
    print(f"{name_string}")

#Add a new name to the list
def search_name(name,dict):
    Donation = input("Please enter an amount to donate >")
    dict.setdefault(name,[]).append(float(Donation))
    return

#make the program quit
def quit_prog():
    print("Thank you. Goodbye!")
    sys.exit()

#generate an email1
def email(name,dict):
    Email = f"\n\nDear {name},\n\n\tWe appreciate your generous donations totalling ${sum(dict[name]):.2f}.\n\nThank you,\nAndrew\n\n" 
    with open(f"Thank_You_to_{name}.txt", 'w+') as f:
        f.write(Email)
    return


def nothing():
    print("Invalid response. Please use an appropriate response.")
    return
   
    
def send_thank_you():
    name = input("Who would you like to thank?>")
    quit_request = ('q', 'quit')
    #call quit_prog function to end program
    if name.lower() in quit_request:
        quit_prog()
    
    #show the list of names using show_list function
    while name.title() == 'List':
        show_list(Donor_dict)
        name = input("Who whould you like to thank?>")
        if name.lower() in quit_request:
            quit_prog()
    
    #Call the search_name function
    search_name(name,Donor_dict)
    
    #call the email function
    Email = email(name,Donor_dict)
    return

def Thank_you_All():
    for name in Donor_dict:
        email(name,Donor_dict)

#sum up the total donations for each person    
def tot_don(dict):
    tots = []
    for name in dict:
        tots.append(sum(dict[name]))
    return tots

#average the donations for each person
def ave_don(dict):
    aves = []
    for name in dict:
        aves.append(sum(dict[name])/len(dict[name]))
    return aves

#return the total number of donations for each person
def num_don(dict):
    nums = []
    for name in dict:
        nums.append(len(dict[name]))
    return nums

#Create a report
def write_report():
    tot = tot_don(Donor_dict)
    num = num_don(Donor_dict)
    ave = ave_don(Donor_dict)
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
    
#Mailroom part2 
#update initial code to include dictionaries


if __name__ ==  '__main__':
    #Create a database
    Jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
    Ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
    Che = ['Cher', [0.01, 0.01]]
    Aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
    Wan = ['Wan Do Nation', [1.00]]   
    #Combine donors into a database
    Database = [Jen, Ste, Che, Aba, Wan]
    #create a dictionary of donor information
    Donor_dict = {}
    for name in Database:
        Donor_dict[name[0]] = name[1]
    print(Donor_dict)    
    #Create a dictionary to switch between input options
    switch_dict = {
        '1': send_thank_you,
        '2': write_report,
        '3': Thank_you_All,
        '4': quit_prog,
        'quit': quit_prog
        }
    
    while True:
        Prompt = input("Choose:\n"
                       "1) Send a Thank you\n"
                       "2) Create a Report\n"
                       "3) Send letters to all donors\n"
                       "4) Quit \n"
                       "Respond with 1, 2, 3 or 'quit'>")                       
        switch_dict.get(Prompt,"nothing")()
       
