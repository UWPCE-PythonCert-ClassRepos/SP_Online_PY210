#!/usr/bin/env python3
from sys import exit


def create_report():
    print("{:<22}{:<5}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)
    for val, i in enumerate(main_list[0]):
        print ("{:<20} {:>9} {:>9} {:>26}{:>11}{:>12}".format(*(i, '$', sum(main_list[val+1]), len(main_list[val+1]), '$',round(sum(main_list[val+1])/len(main_list[val+1]),1))))
        
def use_it(full_name):
    amount = int(input("Please enter in the amount you want to donate: "))
    if amount == 'c':
        get_option()
    main_list[main_list[0].index(full_name)+1].append(amount)
    print ('Thank you {} for your generous donation of {}'.format(full_name, amount))
    main()
def send_thanks():
    full_name = input("\n\nPlease enter a name for a Thank You to go out: ")
    while full_name == 'list':
        print (main_list[0])
        full_name = input("\n\nPlease enter a name for a Thank You to go out: ")
    if full_name == 'c':
        get_option()
    if full_name in main_list[0]:
        use_it(full_name)
    elif full_name not in main_list[0]:
        main_list[0].append(full_name)
        main_list.append([])
        use_it(full_name)

def get_option():
    print ("You have 3 options: \n a: Send a Thank you\n b: Create a Report\n c: quit")
    num = 'd'
    while num!='a' and num!='b' and num!='c':
        num = input("Please enter a valid option: ")
        if num == 'c':
            exit()
    return num
def main():
    while True:
        num = get_option()
        if num =='a':
            send_thanks()
        if num == 'b':
            create_report()

main_list = [['Dan C','Erika K','Mindy P','Mike H','Lovey G'], [1,200,20],[34000],[40,50,60],
                        [13,60,42],[22]]

main()