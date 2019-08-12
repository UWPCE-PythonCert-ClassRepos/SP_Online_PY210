#!/usr/bin/env python3
import tempfile
from pathlib import Path
from datetime import datetime

donors = {'William Henry Harrison' : [806.25, 423.10],
          'James K. Polk' : [37.67, 127.65, 1004.29],
          'Martin van Buren' : [126.47],
          'Millard Fillmore' : [476.21, 2376.21],
          'Chester A. Arthur' : [10236.91]}

letter_template = """Dear {name},
On behalf of all of us at Save the Marmots, thank you for your recent gift of ${amount:.2f}.  When it comes to ensuring marmots have loving homes, every dollar goes a long way.

Your very generous gifts of ${total:.2f} will help us provide food and shelter for all of the rescued marmots, and ensure our staff have the resources to train them for placement.

Warmest regards,

Sean Hodges
"""

def send_thank_you():
    while True:
        donor = input('Please enter a donor name: ')
        if donor == 'quit':
            break
        elif donor == 'list':
            for item in donors.keys():
                print(item)
        else:
            if not donor in donors.keys(): donors[donor] = []
            amount = input('Please enter a donation amount: ')
            try:
                donors[donor].append(float(amount))
            except ValueError:
                break
            total = 0
            for gift in donors[donor]: total += gift
            letter_values = {'name': donor, 'amount': float(amount), 'total': total}
            print(("""



{}


""".format(letter_template)).format(**letter_values)) # I'm doing this because I like the extra whitespace when the letter is in-line, otherwise it gets smooshed with the prompts
            break

def generate_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    donor_report = [] # not a ton of value in converting this to a list.  it made things a bit more complicated...
    for donor in donors.keys():
        total = 0
        for amount in donors[donor]:
            total += amount
        donor_report.append([donor, len(donors[donor]), total])
    donor_report.sort(key = lambda x: x[2], reverse = True) # ...for instance here, where sorting the dict with a lambda function in sorted() was still possible, but then I'd have to cast the resultant list back to a dict
    for item in donor_report:
        report_output = {'name': item[0], 'total': item[2], 'gifts': item[1], 'average': (item[2] / item[1])}
        print('{name:24}  ${total:10.2f}   {gifts:10d}   ${average:12.2f}'.format(**report_output))
    print('')

def save_all_letters():
    letter_dir = Path(input('Please specify a directory to save letters in: '))
    if not letter_dir.is_dir():
        print('{} is an invalid directory; using {}'.format(letter_dir, tempfile.gettempdir()))
        letter_dir = Path(tempfile.gettempdir())
    letter_dir = letter_dir / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
    try:
        letter_dir.mkdir(exist_ok=True)
    except:
        print('Error creating {}'.format(letter_dir.absolute()))
        return

    for donor in donors.keys():
        total = 0
        for amount in donors[donor]: total += amount
        letter_values = {'name': donor, 'amount': donors[donor][-1], 'total': total}
        letter = letter_dir / (donor.replace(' ', '_') + '.txt')
        with letter.open("w") as fileio: fileio.write(letter_template.format(**letter_values))
        fileio.close()
    print('Saved letters in {}'.format(letter_dir.absolute()))

def exit_mailroom():
    return 1

if __name__ == '__main__':
    menu_dispatch = {1: send_thank_you, 2: generate_report, 3:save_all_letters, 4: exit_mailroom}
    while True:
        print("""Mailroom -- Main Menu

Options:
  1 Send a Thank You
  2 Generate a Report
  3 Send letters to all donors
  4 Quit
""")
        option = input('Please select an option (1, 2, 3, 4): ')
        if option.isnumeric():
            if int(option) in menu_dispatch.keys():
                if menu_dispatch.get(int(option))() == 1: break # breaking out of the loop /appears/ to be the cleanest way to do this, if I dispatch to quit() the loop is still repeating
