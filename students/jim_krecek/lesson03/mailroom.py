data = [["Nate Secinaro",12,44,9],["Jess Reid",3],["Pat Carrier",65,41],["Zac Fisher",13,4,4],["Jim Krecek",3,33,57]]

prompt = "\nWhat do you want to do?\n -1 Send a Thank You\n -2 Create a Report\n -3 Quit\n>>> "

def send_ty():
    askname = input("\nEnter the full name of the donor or type 'list' to see the list of donors:\n>>> ")
    if askname.lower() == "list":
        print("\nHere is a list of all of the donors:")
        for d in data:
            print(d[0])
    
    for d in data:
        if askname.lower() == d[0].lower():
            usename = askname
            askmoney = input("\nHow much did this person donate?\n>>> ")
            d.append(int(askmoney))
            emailtext = "\nDear {},\n\nThank you for your generous donation of ${}.\n\nSincerely, Jim".format(d[0],askmoney)
            print(emailtext)
            break
    
    if askname not in d[0] and askname.lower() != "list":
        data.append([askname])

def create_report():
    firstline = "{:<25}| {:<12}| {:<10}| {:>12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(firstline)
    print("-"*len(firstline))
    for d in data:
        total = sum(d[1:])
        average = total/(len(d)-1)
        print("{:<25} ${:>11.2f}  {:>10}  ${:>12.2f}".format(d[0],total,len(d)-1,average))
        
    
def main():
    while True:
        response = input(prompt)
        if response == "1" or response.lower() == "send a thank you":
            send_ty()
        if response == '2' or response.lower() == "create a report":
            create_report()
        if response == '3' or response.lower() == "quit":
            break

            
if __name__ == "__main__":
    main()