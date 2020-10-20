### Lesson_3 - Mailroom Part 1

from textwrap import dedent

donor_db = [("Jimmy Hendrix", [23.23, 24.48]),
            ("Jack White", [32.84, 48]),
            ("Keith Richards", [68]),
            ("Jimmy Page", [34,89]),
            ("Albert Hamond", [34,64,49]),
            ]

def main():
    prompt = "\n".join(("Please select from the following options",
         "1 - Send a Thank You",
         "2 - Create a Report",
         "3 - Quit",
         ">>> "))
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            report()
        elif response == "3":
            break
        else:
            print("Please select a number between 1 and 3")

def thank_you():

    while True:
        name = input("Please input donors full name or type 'list' to display existing registry: ")
        if name.lower() == 'list':
            print_donors()
            continue
        else:
            amount = float(input("Please donation amount: "))
            existing_donor = False
            for donor in donor_db:
                if name.strip().lower() == donor[0].lower():
                    li = donor_db.index(donor)
                    existing_donor = True

            if existing_donor:
                donor_db[li][1].append(amount)
            else:
                donor = (name,[amount])
                donor_db.append(donor)
            break

    print(thank_you_letter(name))

def thank_you_letter(name):
    return dedent('''
                Dear {},
                    Thank for your generous donation!!  Your
                    contribution is greatly appreciated.

                    Truly yours,

                    Guitar Greats.
                '''.format(name))

def print_donors():
    print("Donor list:\n")
    for donor in donor_db:
        print(donor)

def sort_key(item):
    return item[1]

def report():
    donate_name = []
    for name,donation in donor_db:
        donate_sum = sum(donation)
        donate_num = len(donation)
        donate_avg = donate_sum/donate_num
        donate_name.append((name,donate_sum,donate_num,donate_avg))

    donate_name.sort(key=sort_key, reverse=True)

    print("{:25s} |$ {:11s} | {:9s} |$ {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in donate_name:
        print("{:25s}   {:8.2f}   {:9d}   {:10.2f}".format(*row))
print(f'\n\n')



if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
