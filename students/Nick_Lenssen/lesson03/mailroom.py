from sys import exit

from operator import itemgetter

def use_it():
    while True:
        amount = input("\nPlease enter in the amount you want to donate or c to go to original prompt: ")
        if amount == 'c':
            main()
            #donor_db.pop()
        else:
            amount = int(amount)
        return amount

def create_report():
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)
    #donor_db_c = sorted(donor_db, key=itemgetter(1))
    for i in sorted(donor_db, key=itemgetter(1)):
        print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(i[0], '$', round(sum(i[1]),2), len(i[1]), '$',round(sum(i[1])/len(i[1]),1))))

def send_thanks():
    while True:
        full_name = input("\n\nPlease enter a name for a Thank You to go out or c to go to orginal prompt: ")
        if full_name == 'list':
            for i in donor_db:
            	print (i[0])
        elif full_name == 'c':
            main()
        else:
            for i in donor_db:
                if i[0] == full_name:
                    i[1].append(use_it())
                    break
            else:
                donor_db.append((full_name, [use_it()]))
            main()

def exit_program():
	print ('Goodbye')
	exit()

def main():
    while True:
        num = input(prompt)
        if num =='a':
            send_thanks()
        elif num == 'b':
            create_report()
        elif num == 'c':
        	exit_program()
        else:
        	print ('Not a valid option')

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

prompt = "\n".join(("Please choose from below options:",
          "a - Send a Thank you",
          "b - Create a report",
          "c - Exit",
          ">>> "))

if __name__ == "__main__":
    main()