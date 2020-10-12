
person1 = {"Name": 'William Gates', "Total": 653784.49, "Qty": 2, "Avg": 326892.24}
person2 = {"Name": 'Mark Zuckerberg', "Total": 16396.10, "Qty": 3, "Avg": 5465.37}
person3 = {"Name": 'Jeff Bezos', "Total": 877.33, "Qty": 1, "Avg": 877.33}
person4 = {"Name": 'Paul Allen', "Total": 708.42, "Qty": 3, "Avg": 236.14}
person5 = {"Name": 'John Smith', "Total": 899.98, "Qty": 5, "Avg": 399.21}
donor_all = [person1, person2, person3, person4, person5]
user_input = ""

user_input = input(
    'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
existing = False
while user_input.title() == "List":
    for person in donor_all:
        print(person)
    user_input = input(
        'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
for person in donor_all:
    for pvalue in person.values():
        if user_input.title() == pvalue:
            donation_amt = float(input("Please enter the donation amount: "))
            person["Total"] = person["Total"] + donation_amt
            person["Qty"] = person["Qty"] + 1
            person["Avg"] = round(person["Total"] / person["Qty"], 2)
            existing = True
            person_to_thank = person
if existing != True:
    donation_amt = float(input("Please enter the donation amount: "))
    person_add = {"Name": user_input.title(), "Total": donation_amt, "Qty": 1, "Avg": donation_amt}
    donor_all.append(person_add)
    person_to_thank = person_add
print("The following thank you note will be emailed to the donor: ")
print(
    '"Dear {}, \n Thank you so much for your gracious donation of ${:.2f}. We are so thankful for your strong support!! \nCheers,\nRoslyn Melookaran"'.format(
        person_to_thank["Name"], donation_amt))
for person in donor_all:
    print(person)