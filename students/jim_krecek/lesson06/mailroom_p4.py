import sys

data = {"Nate Secinaro":[12,44,9],"Jess Reid":[3],"Pat Carrier":[65,41],"Zac Fisher":[13,4,4],"Jim Krecek":[3,33,57]}

prompt = "\nWhat do you want to do?\n -1 Send a Thank You\n -2 Create a Report\n -3 Send letters to all donors\n -4 Quit\n>>> "

def send_ty():
    askname = input("\nEnter the full name of the donor or type 'list' to see the list of donors:\n>>> ")
    if askname.lower() == 'list':
        print(donor_list(data))
    else:
        askmoney = input("\nHow much did this person donate?\n>>> ")
        print(thanks(data, askname, askmoney))
            
def donor_list(donors):
    d_list = ''
    for donor in donors:
        d_list += '{}\n'.format(donor)
    return d_list
    
def thanks(donors, name, cash):
    try:
        donors[name].append(int(cash))
    except:
        donors[name] = []
        donors[name].append(int(cash))
    emailtext = "\nDear {},\n\nThank you for your generous donation of ${}.\n\nSincerely, Jim".format(name,cash)
    return emailtext

def create_report():
    firstline = "{:<25}| {:<12}| {:<10}| {:>12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    report = ""
    report = report + firstline + '\n' + ('-'*len(firstline))

    sorted_data = sorted(((sum(value),len(value),key) for (key,value) in data.items()), reverse=True)
    for tot,num,name in sorted_data:
        average = tot/num
        rep_line = "\n{:<25s} ${:>11.2f}  {:>10d}  ${:>12.2f}".format(name,tot,num,average)
        report = report + rep_line
    return report
        
def print_report():
    print(create_report())
        
        
def send_all():
    for k, v in data.items():
        write_letters(k,v)
    print("\nLetters have been printed and are saved in the current directory")

def write_letters(name, cash):
    lettertext = "Dear {},\n\n\tThank you for your very kind donation of ${}\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t\t-Jim & The Team".format(name,sum(cash))
    write_files(lettertext, name)
    return lettertext    
    
def write_files(text, name):
    with open('{}.txt'.format(name.replace(' ','_')),'w+') as output:
            output.write(text)

def quit():
    print('You are exiting the program. Come back again soon!')
    return SystemExit
 
def main():
    main_menu = {'1': send_ty,'2': print_report,'3':send_all,'4':quit}
    while True:
        response = input(prompt)
        menu_function = main_menu.get(response)
        try:
            menu_function()
        except TypeError:
            print("\n'{}' is not a valid entry. Please try again.".format(response))

            
if __name__ == "__main__":
    main()