import sys
import tempfile

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),]

def get_name_list():
    name_list = []
    #for i in donor_db:
    #    name_list.append(i[0])
    [name_list.append(i[0]) for i in donor_db]
    return name_list


def sort_key(donor_db):
    return donor_db[0].split(" ")[1]


prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - exit_program",
          ">>> "))

def add_donation_amount(full_name, donation_amount):
    for i in donor_db:

        if full_name == i[0]:
            #donation_amount = int(input("Enter donation amount >> "))
            i[1].append(donation_amount)






def send_a_thank_you():
    while True:
        name_list = get_name_list()
        full_name = input("Pleass enter Full Name >> ")
        if full_name == "list":
            print("\n".join(name_list))
        else:
            break
    try:
        donation_amount= int(input("Enter donation amount >> "))
    except:
        print("please enter integer only")
        exit_program()


    if full_name not in name_list:
        new_donor = []
        #donation_amount=int(input("Enter donation amount >> "))
        new_donor = (full_name,[donation_amount],)
        donor_db.append(new_donor)

    else:
        add_donation_amount(full_name, donation_amount)


    print(f"Thank Mr/Ms {full_name.upper()} for donation $ {donation_amount}")

    print(donor_db)
    l1 = full_name.split()
    try:
        first_name = l1[0].upper()
    except:
        first_name = ""
    try:
        last_name = l1[1].upper()
    except:
        last_name = ""

    template = """Dear {first_name} {last_name},
    Thank you for your very kind donation of ${donation_amount}
    It will be put to very good use.
        Sincerely,
            -The Team"""

    letter_data ={"first_name": first_name, "last_name": last_name, "donation_amount": donation_amount}
    filename = f"{first_name}_{last_name}.txt"
    with open(filename, "w") as fp:
        fp.write(template.format(**letter_data))

def get_first_last_name():
    name_list = get_name_list()
    first_last_name_list= []
    for i in range(len(name_list)):
        l = name_list[i].split()
        if len(l)>2:
            l[1:] = [" ".join(l[1:])]
        first_last_name_list.append(l)
    return first_last_name_list

def thank_you_letter_template(first_name, last_name, donation_amount):
    first_name = first_name
    last_name = last_name
    donation_amount = donation_amount

    template = """Dear {first_name} {last_name},
    Thank you for your very kind donation of ${donation_amount}
    It will be put to very good use.
        Sincerely,
            -The Team"""

    letter_data ={"first_name": first_name, "last_name": last_name, "donation_amount": donation_amount}

    filename = f"{first_name}_{last_name}.txt"
    with open(filename, "w") as fp:
        fp.write(template.format(**letter_data))



def send_all_thank_you():
    first_last_name_list= get_first_last_name()
    full_name_list = get_name_list()
    for i in range(len(first_last_name_list)):
        first_name = first_last_name_list[i][0]
        last_name = first_last_name_list[i][1]
        thank_you_letter_template(first_name, last_name, 10)

def sort_total_given(l1):
    #return donor_db[0].split(" ")[1]
    return l1[1]

def create_a_report():
    l = (["Donor Name", "Total Given", "Num Gifts", "Average Gift"])
    temp_list = []
    l1 = []

    total_given =0
    for x in donor_db:
        temp_list.append(x[0])
        tg = sum(list((x[1])))
        total_given = str(tg)
        temp_list.append(total_given)
        ng = len(x[1])
        num_gift = str(ng)
        temp_list.append(num_gift)
        #ave_gift = str(round(total_given/num_gift,2))
        aG = round(tg/ng,2)
        ave_gift = str(aG)
        temp_list.append(ave_gift)
        #report_table.append(x[0], total_given, num_gift, ave_gift)
    m = 0
    while m< len(temp_list):
        l1.append(temp_list[m:m+4])
        m = m+4

    #l1 =sorted(l1, key = sort_key)
    l1 =sorted(l1, key = sort_total_given)
    l1.insert(0,l)

    new_list = []
    #for i in l1:
    #    for j in i:
    #        new_list.append(len(j))
    #        l = max(new_list)

    [new_list.append(len(j)) for i in l1 for j in i]
    l = max(new_list)
    space = " "*10
    width = l
    #print(l1)
    for a,b,c,d in l1:
        print(f'{a:<{width}}{space}{b:>{width}}{space}{c:>{width}}{space}{d:>{width}}')

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

response_dict ={"1": send_a_thank_you, "2": create_a_report, "3": send_all_thank_you, "4": exit_program}
def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response in response_dict:
            response_dict.get(response)()
        else:
            print("Not a valid option!")

        #try:
        #    response_dict.get(response)()
        #except:
        #    print("Not a valide option!")




if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
