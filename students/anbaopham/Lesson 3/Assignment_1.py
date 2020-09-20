import sys
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),]

def get_name_list():
    name_list = []
    for i in donor_db:
        name_list.append(i[0])
    return name_list


def sort_key(donor_db):
    return donor_db[0].split(" ")[1]


prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

def add_donation_amount(full_name, donation_amount):
    for i in donor_db:

        if full_name == i[0]:
            #donation_amount = int(input("Enter donation amount >> "))
            i[1].append(donation_amount)






def send_a_Thank_You():
    while True:
        name_list = get_name_list()
        full_name = input("Pleass enter Full Name >> ")
        if full_name == "list":
            print("\n".join(name_list))
        else:
            break
    donation_amount=int(input("Enter donation amount >> "))

    if full_name not in name_list:
        new_donor = []
        #donation_amount=int(input("Enter donation amount >> "))
        new_donor = (full_name,[donation_amount],)
        donor_db.append(new_donor)

    else:
        add_donation_amount(full_name, donation_amount)


    print(f"Thank Mr/Ms {full_name.upper()} for donation $ {donation_amount}")
    print(donor_db)

def create_a_Report():
    l = (["Donor Name", "Total Given", "Num Gifts", "Average Gift"])
    temp_list = []
    l1 = []

    totalGiven = 0
    for x in donor_db:
        temp_list.append(x[0])
        tg = sum(list((x[1])))
        totalGiven = str(tg)
        temp_list.append(totalGiven)
        ng = len(x[1])
        numGift = str(ng)
        temp_list.append(numGift)
        #aveGift = str(round(totalGiven/numGift,2))
        aG = round(tg/ng,2)
        aveGift = str(aG)
        temp_list.append(aveGift)
        #report_table.append(x[0], totalGiven, numGift, aveGift)
    m = 0
    while m < len(temp_list):
        l1.append(temp_list[m:m+4])
        m = m+4

    l1 =sorted(l1, key = sort_key)

    l1.insert(0,l)

    newL = []
    for i in l1:
        for j in i:
            newL.append(len(j))
            l = max(newL)
    space = " "*10
    width = l
    #print(l1)
    for a,b,c,d in l1:
        print(f'{a:<{width}}{space}{b:>{width}}{space}{c:>{width}}{space}{d:>{width}}')

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_a_Thank_You()

        elif response == "2":
            create_a_Report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")






if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
