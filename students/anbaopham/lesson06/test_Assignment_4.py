import sys
import pandas as pandas
import os

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),]

def get_name_list():
    name_list = []
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

def user_input_full_name():
    while True:
        full_name = input("Pleass enter full name >> ")
        full_name = full_name.strip()

        if len(full_name) == 0:
            print("please try again")
        elif (' ' in full_name) == False:
            print("first name or last name can't be blank, please try again")
        elif listing_donor(full_name) is True:
            continue
        else:
            break
    return full_name

def listing_donor(full_name):
    name_list = get_name_list()
    if full_name == "list":
        print("\n".join(name_list))
        return True
    else:
        return False

def test_listing_donor():

    assert(listing_donor("list")) is True
    assert(listing_donor("afsd")) is False

def add_donor(full_name, donation_amount):
    new_donor = []
    new_donor = (full_name,[donation_amount],)
    donor_db.append(new_donor)
def test_add_donor():
    add_donor("a p", 100)
    assert(donor_db[-1]==('a p', [100]))


def add_donation_amount(full_name, donation_amount):
    for i in donor_db:

        if full_name == i[0]:
            i[1].append(donation_amount)

def test_add_donation_amount():
    full_name ="a b"
    donation_amount=100
    for i in donor_db:
        if full_name == i[0]:
            assert i[1] == [100]

def get_donation_amount():
    while True:
        try:
            donation_amount= int(input("Enter donation amount >> "))
        except:
            print("please enter integer only")
        else:
            break

    return donation_amount


def thank_you_letter_template(first_name, last_name, donation_amount):
    first_name = first_name.upper()
    last_name = last_name.upper()
    donation_amount = donation_amount

    template = """Dear {first_name} {last_name},
    Thank you for your very kind donation of ${donation_amount}
    It will be put to very good use.
        Sincerely,
            -The Team"""

    letter_data ={"first_name": first_name, "last_name": last_name, "donation_amount": donation_amount}

    file_name = f"{first_name}_{last_name}.txt"
    with open(file_name, "w") as fp:
        fp.write(template.format(**letter_data))



def test_thank_you_letter_template():
    template = """Dear AN PHAM,
    Thank you for your very kind donation of $100
    It will be put to very good use.
        Sincerely,
            -The Team"""
    thank_you_letter_template("an", "pham", 100)
    with open("AN_PHAM.txt", "r") as fp:
        f = fp.read()
        assert(f) == template


def send_a_thank_you():
    full_name = user_input_full_name()
    donation_amount = get_donation_amount()
    name_list = get_name_list()

    if full_name not in name_list:
        add_donor(full_name, donation_amount)
    else:
        add_donation_amount(full_name, donation_amount)

    print(f"Thank Mr/Ms {full_name.upper()} for donation $ {donation_amount}")

    l1 = full_name.split()
    try:
        first_name = l1[0]
    except:
        first_name = ""
    try:
        last_name = l1[1]
    except:
        last_name = ""

    thank_you_letter_template(first_name, last_name, donation_amount)

def get_first_last_name():
    name_list = get_name_list()
    first_last_name_list= []
    for i in range(len(name_list)):
        l = name_list[i].split()
        if len(l)>2:
            l[1:] = [" ".join(l[1:])]
        first_last_name_list.append(l)
    return first_last_name_list

def send_all_thank_you():
    first_last_name_list= get_first_last_name()

    for i in range(len(first_last_name_list)):
        first_name = first_last_name_list[i][0]
        last_name = first_last_name_list[i][1]
        thank_you_letter_template(first_name, last_name, 10)

def test_send_all_thank_you():
    send_all_thank_you()
    first_last_name_list= get_first_last_name()
    path = os.getcwd()
    for i in range(len(first_last_name_list)):
        first_name = first_last_name_list[i][0]
        last_name = first_last_name_list[i][1]
        file_name = f"{first_name}_{last_name}.txt"
    for i in os.listdir(path):
        if i.startswith(file_name) and i.endswith(".txt"):
            with open("file_name", "r") as fp:
                f = fp.read()
                assert(f) == template

def sort_total_given(l1):
    #return donor_db[0].split(" ")[1]
    return l1[1]


def get_report_data():
    temp_list = []
    for x in donor_db:
        temp_list.append(x[0])
        tg = round(sum(list((x[1]))),2)
        total_given = str(tg)
        temp_list.append(total_given)
        ng = len(x[1])
        num_gift = str(ng)
        temp_list.append(num_gift)
        aG = round(tg/ng,2)
        ave_gift = str(aG)
        temp_list.append(ave_gift)

    return temp_list

def test_get_report_data():
    add_donor("an pham", 1234567)
    donor_list = get_report_data()
    assert(donor_list[-4]) == "an pham"
    assert(donor_list[-3]) == '1234567'
    assert(donor_list[-2]) == '1'
    assert(donor_list[-1]) == '1234567.0'

def create_a_report():
    l = (["Donor Name", "Total Given", "Num Gifts", "Average Gift"])
    temp_list = get_report_data()
    l1 = []

    m = 0
    while m< len(temp_list):
        l1.append(temp_list[m:m+4])
        m = m+4

    l1 =sorted(l1, key = sort_total_given)
    l1.insert(0,l)

    new_list = []

    [new_list.append(len(j)) for i in l1 for j in i]
    l = max(new_list)
    space = " "*10
    width = l
    print(l1)

    for a, b, c, d in l1:
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
