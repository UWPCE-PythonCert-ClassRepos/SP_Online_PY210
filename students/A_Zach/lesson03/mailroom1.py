import sys

#Functions
#Show list of names
def show_list(inp):
    #print names of donors
    for name in names:
        print(name)
    return
    
#Add a new name to the list
def search_name(inp):
    response_donation = input("Please enter an amount to donate >")
    if response_donation.lower == 'quit':
        return
    i = 0
    #iterate through the database until the requested name is found
    while i < len(names):
        #Add the donation to the name provided
        if names[i] == inp.title():
            donations[i].append(float(response_donation))        
            return
        #Increase iteration if name has not been reached
        i += 1
    names.append(inp.title())
    donations.append([float(response_donation)])
    return response_donation

#make the program quit
def quit_prog(p):
    if p.lower() == 'quit':
        print("Thank you. Goodbye!")
        sys.exit()

#generate an email1
def email(inp):
    #find the index of n in the database
    i = names.index(inp.title())
    #format email. format the donation amount (d[i])
    #into a floating point with 2 decimal places.
    print(f"\n\nDear {inp},\n\n\tWe appreciate your generous donations totalling ${sum(donations[i]):.2f}.\n\nThank you,\nAndrew\n\n")
    
   
    
def send_thank_you():
    inp = input("Who whould you like to thank?>")
    if inp.lower == 'quit':
        return
    #show the list of names using show_list function
    while inp.title() == 'List':
        show_list(inp)
        inp = input("Who whould you like to thank?>")
        if inp.lower == 'quit':
            return
    
    #Call the search_name function
    donation = search_name(inp)
    
    #call the email function
    email(inp)

#creat report inputs    
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
    sort_by_tot = sorted(tots, reverse=True)
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
        ind = tots.index(entry)
        print(f"{names[ind]:<{ln}} ${tots[ind]:>{l-1}}{nums[ind]:>{l+1}} ${aves[ind]:>{l-3}.2f}")
    print(f"\n")
    
#Mailroom part 1
#Generate a database of donors


if __name__ == '__main__':
    #Create a database
    Jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
    Ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
    Che = ['Cher', [0.01, 0.01]]
    Aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
    Wan = ['Wan Do Nation', [1.00]]   
    #Combine donors into a database
    database = [Jen, Ste, Che, Aba, Wan]
    #Initialize a new list for just names and just donations
    names = []
    donations = []
    #Fill the names and donations lists
    for i,j in database:
       names.append(i)
       donations.append(j)
    #iterate until 1, 2, or quit is chosen. then call the appropriate function
    while True:
        Prompt = input("Choose:\n1) Send a Thank you\n2) Create a "
                       "Report\n3) Quit \nRespond with 1, 2 or 'quit'>")    
        if Prompt == '1':
            send_thank_you()
        elif Prompt == '2':
            write_report()
        else:
            quit_prog(Prompt)
            print(f"'{Prompt}' is an invalid entry")
            
        

