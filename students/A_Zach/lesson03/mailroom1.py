import sys

#Functions
#Add a donation to a person on the list
def new_donation(inp,n,d):
    response_donation = input("Please enter an amount to donate >")
    quit_prog(response_donation)
    
    i = 0
    
    #iterate through the database until the requested name is found
    while i < len(n):
        #Add the donation to the name provided
        if n[i] == inp.title():
            d[i].append(float(response_donation))        
            break
        #Increase iteration if name has not been reached
        i += 1
    return

#Show list of names
def show_list(inp,n):
    #print names of donors
    for i in n:
        print(i)
    return
    
#Add a new name to the list
def search_name(inp,n,d):
    for i in n:
        #if the name is in the list add a new donation. If not add the name and a new donation.
        if inp.title() == i:
            new_donation(inp,n,d)
            #leave loop if name has been found and donation added
            return
    n.append(inp.title())
    d.append([])
    new_donation(inp,n,d)
    return

#make the program quit
def quit_prog(p):
    if p.lower() == 'quit':
        print("Thank you. Goodbye!")
        sys.exit()

#generate an email1
def email(inp,n,d):
    #find the index of n in the database
    i = n.index(inp.title())
    #format email. n is name. format the donation amount (d[i])
    #into a floating point with 2 decimal places.
    print(f"\n\nDear {inp},\n\n\tWe appreciate your generous donations totalling ${sum(d[i]):.2f}.\n\nThank you,\nAndrew\n\n")
    
   
    
def send_thank_you(n,d):
    inp = input("Who whould you like to thank?>")
    
    #call quit_prog function to end program
    quit_prog(inp)
    
    #show the list of names using show_list function
    while inp.title() == 'List':
        show_list(inp,n)
        inp = input("Who whould you like to thank?>")
        quit_prog(inp)
    
    #Call the search_name function
    search_name(inp,n,d)
    
    #call the email function
    email(inp,n,d)
    return

#sum up the total donations for each person    
def tot_don(d):
    tots = []
    i = 0
    while i < len(d):        
        tots.append(sum(d[i]))
        i += 1
    return tots

#average the donations for each person
def ave_don(d):
    aves = []
    i = 0
    while i < len(d):        
        aves.append(sum(d[i])/len(d[i]))
        i += 1
    return aves

#return the total number of donations for each person
def num_don(d):
    nums = []
    i = 0
    while i < len(d):        
        nums.append(len(d[i]))
        i += 1
    return nums

#Create a report
def write_report(n,d):
    tot = tot_don(d)
    num = num_don(d)
    ave = ave_don(d)
    #sort by the totaled values
    sort_by_tot = sorted(tot, reverse=True)
    print(tot)
    print(sort_by_tot)
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
        print(f"{n[ind]:<{ln}} ${tot[ind]:>{l-1}}{num[ind]:>{l+1}} ${ave[ind]:>{l-3}.2f}")
    print(f"\n")
    
#Mailroom part 1
#Generate a database of donors


def main():
    #Create a database
    Jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
    Ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
    Che = ['Cher', [0.01, 0.01]]
    Aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
    Wan = ['Wan Do Nation', [1.00]]   
    #Combine donors into a database
    Database = [Jen, Ste, Che, Aba, Wan]
    #Initialize a new list for just names and just donations
    Names = []
    Donations = []
    #Fill the names and donations lists
    for i,j in Database:
       Names.append(i)
       Donations.append(j)
    #iterate until 1, 2, or quit is chosen. then call the appropriate function
    while True:
        Prompt = input("Choose:\n1) Send a Thank you\n2) Create a "
                       "Report\n3) Quit \nRespond with 1, 2 or 'quit'>")    
        if Prompt is '1':
            send_thank_you(Names,Donations)
        elif Prompt is '2':
            write_report(Names,Donations)
        elif Prompt.lower() == 'quit':
            quit_prog(Prompt)
        else:
            print(f"'{Prompt}' is an invalid entry")
            
        
main()