#!/usr/bin/env python3

donors = [("Bill Gates", [653772.32, 12.17]),
          ("Jeff Bezos", [877.33]),
          ("Paul Allen", [663.23, 43.87, 1.32]),
          ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
          ("Tim Cook", [1563.32, 8976.54])]

prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          ">>> "))


def donor_list():
    donor_names = [i[0] for i in donors]
    return donor_names
    

def add_donation(name):
    donation = float(input("Please enter in a donation: "))
    for i in donors:
        if name in i:
            place = donors.index(i)
            thankyou_email(name, donation)
            return donors[place][1].append(donation)

def thankyou_email(name, donation):
    #donation = [(donor, donations) for name, donations in donors if donor==name][0][1][:1]
    print("""Dear {},
            Thank you very much for the generous donation of {}.
            It is very much appreciated. 
            Respectfully,
        
            Eric""".format(name, donation))


def thank_you():
    complete = False
    
    while not complete:
        thanks = input("Please enter full name, or type 'list' to see all names: ").title()
        if thanks == 'List':
            print(donor_list())
            continue
        if thanks not in [x[0] for x in donors]:
            donors.append((thanks,list()))
        
        add_donation(thanks)
        complete = True

    print("out of the loop", donors)
    
    

def create_report():
    pass



def main():
    response = input(prompt)
    if response == '1':
        thank_you()





if __name__ == "__main__":
    main()

