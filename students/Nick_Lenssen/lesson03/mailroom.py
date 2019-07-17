#!/usr/bin/env python3
from sys import exit


def create_report():
    print("\n{:<22}{:<5}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)
    for val, i in enumerate(main_list[0]):
        print ("{:<20} {:>9} {:>9} {:>26}{:>11}{:>12}".format(*(i, '$', sum(main_list[val+1]), len(main_list[val+1]), '$',round(sum(main_list[val+1])/len(main_list[val+1]),1))))
        
def use_it(full_name):
    while True:
        amount = input("\nPlease enter in the amount you want to donate: ")
        if amount == 'c':
            main_list[0].pop()
            main_list.pop()
            print (main_list)
            main()
        else:
            amount = int(amount)
            main_list[main_list[0].index(full_name)+1].append(amount)
            print ('Thank you {} for your generous donation of {}'.format(full_name, amount))
            main()
def send_thanks():
    full_name = input("\n\nPlease enter a name for a Thank You to go out: ")
    while True:
        while full_name == 'list':
            print (main_list[0])
            full_name = input("\n\nPlease enter a name for a Thank You to go out: ")
        if full_name == 'c':
            main()
        if full_name in main_list[0]:
            print ('in')
            use_it(full_name)
        elif full_name not in main_list[0]:
            print ('not in')
            main_list[0].append(full_name)
            main_list.append([])
            use_it(full_name)

def get_option():
    while True:
        print ("\nYou have 3 options: \n a: Send a Thank you\n b: Create a Report\n c: quit")
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
            print ('send')
            send_thanks()
        if num == 'b':
            print ('create')
            create_report()

main_list = [['Dan C','Erika K','Mindy P','Mike H','Lovey G'], [1,200,20],[34000],[40,50,60],
                        [13,60,42],[22]]


if __name__ == "__main__":
    main()




