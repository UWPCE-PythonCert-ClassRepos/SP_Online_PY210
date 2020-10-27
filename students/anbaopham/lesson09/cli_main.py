import sys
import donor_models as dm





dc = dm.DonorCollection()

def user_input_name():
    while True:
        full_name = input("Pleass enter Full Name >> ")
        if full_name == "list":
            print("\n".join(dc.name_list()))
        else:
            break
    return full_name.upper()

def user_input_amount():
    try:
        donation_amount= int(input("Enter donation amount >> "))
    except:
        print("please enter integer only")
        exit_program()

    return donation_amount



def send_a_thank_you():
    full_name = user_input_name()
    donation_amount = user_input_amount()
    dc = dm.DonorCollection()
    dc.update_donor_db(full_name.upper(), donation_amount)
    d = dm.Donor(full_name, donation_amount)
    d.generate_letter()


def create_a_report():
    dc = dm.DonorCollection()
    l = (["Donor Name", "Total Given", "Num Gifts", "Average Gift"])
    l1 = []
    a_list = dc.name_list()
    temp_list = dc.report_list()

    m = 0
    while m< len(temp_list):
        l1.append(temp_list[m:m+4])
        m = m+4

    l1 = sorted(l1, key = lambda i: i[0])
    l1.insert(0,l)

    new_list = []
    [new_list.append(len(j)) for i in l1 for j in i]
    l = max(new_list)
    space = " "*10
    width = l

    for a,b,c,d in l1:
        print(f'{a:<{width}}{space}{b:>{width}}{space}{c:>{width}}{space}{d:>{width}}')

def send_all_thank_you():
    dc = dm.DonorCollection()
    for i in dc.donor_db:
        full_name = i[0]
        last_donation = i[1][-1]
        d = dm.Donor(full_name,last_donation)
        d.generate_letter()

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script



def main():
    prompt = "\n".join(("Welcome to the mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a Report",
              "3 - Send letters to all donors",
              "4 - exit_program",
              ">>> "))

    response_dict ={"1": send_a_thank_you, "2": create_a_report,
                    "3": send_all_thank_you, "4": exit_program}
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response in response_dict:
            response_dict.get(response)()
        else:
            print("Not a valid option!")





if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
