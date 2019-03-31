
data = {"Nate Secinaro":[12,44,9],"Jess Reid":[3],"Pat Carrier":[65,41],"Zac Fisher":[13,4,4],"Jim Krecek":[3,33,57]}

prompt = "\nWhat do you want to do?\n -1 Send a Thank You\n -2 Create a Report\n -3 Send letters to all donors\n -4 Quit\n>>> "

def send_ty():
    askname = input("\nEnter the full name of the donor or type 'list' to see the list of donors:\n>>> ")
    if askname.lower() == "list":
        print("\nHere is a list of all of the donors:")
        for d in data.keys():
            print(d)
    else:
        for d in data.keys():
            if askname.lower() == d.lower():
                askmoney = input("\nHow much did this person donate?\n>>> ")
                data[d].append(int(askmoney))
                emailtext = "\nDear {},\n\nThank you for your generous donation of ${}.\n\nSincerely, Jim".format(d,askmoney)
                print(emailtext)
                break
    
        if askname != d:
            askmoney = input("\nHow much did this person donate?\n>>> ")
            data[askname] = []
            data[askname].append(int(askmoney))
            emailtext = "\nDear {},\n\nThank you for your generous donation of ${}.\n\nSincerely, Jim".format(askname,askmoney)
            print(emailtext)
            

def create_report():
    firstline = "{:<25}| {:<12}| {:<10}| {:>12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(firstline)
    print("-"*len(firstline))
    sorted_data = sorted(((sum(value),len(value),key) for (key,value) in data.items()), reverse=True)
    for tot,num,name in sorted_data:
        average = tot/num
    
        print("{:<25s} ${:>11.2f}  {:>10d}  ${:>12.2f}".format(name,tot,num,average))
        
def send_all():
    for k,v in data.items():
        lettertext = "Dear {},\n\n\tThank you for your very kind donation of ${}\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t\t-Jim & The Team".format(k,sum(v))
        with open('{}.txt'.format(k.replace(' ','_')),'w+') as output:
            output.write(lettertext)
    print("\nLetters have been printed and are saved in the current directory")
    
def main():
    while True:
        response = input(prompt)
        if response == "1" or response.lower() == "send a thank you":
            send_ty()
        elif response == '2' or response.lower() == "create a report":
            create_report()
        elif response == '3' or response.lower() == "send letters to all donors":
            send_all()
        elif response == '4' or response.lower() == "quit":
            break

            
if __name__ == "__main__":
    main()