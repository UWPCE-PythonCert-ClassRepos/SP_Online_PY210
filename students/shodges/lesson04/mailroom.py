#!/usr/bin/env python3
import tempfile
from pathlib import Path

donors = {'William Henry Harrison' : [806.25, 423.10],
          'James K. Polk' : [37.67, 127.65, 1004.29],
          'Martin van Buren' : [126.47],
          'Millard Fillmore' : [476.21, 2376.21],
          'Chester A. Arthur' : [10236.91]}

letter_template = """Dear {name},
On behalf of all of us at Save the Marmots, thank you for your generous gift of ${amount:.2f}.  When it comes to ensuring marmots have loving homes, every dollar goes a long way.

Your gift will help us provide food and shelter for all of the rescued marmots, and ensure our staff have the resources to train them for placement.

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

            letter_values = {'name': donor, 'amount': float(amount)}
            print(("""



{}


""".format(letter_template)).format(**letter_values)) # I'm doing this because I like the extra whitespace when the letter is in-line, otherwise it gets smooshed with the prompts
            break

def generate_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    report_output = []
    for donor in donors.keys():
        total = 0
        for amount in donors[donor]:
            total += amount
        report_output.append([donor, len(donors[donor]), total])
    report_output.sort(key = lambda x: x[2], reverse = True)
    for item in report_output:
        print('{:24}  ${:10.2f}   {:10d}   ${:12.2f}'.format(item[0], item[2], item[1], item[2]/item[1]))
    print('')

def save_all_letters():
    letter_dir = Path(input('Please specify a directory to save letters in (or leave blank to use temp directory): '))
    if not letter_dir.is_dir():
        print('{} is an invalid directory; using {}'.format(letter_dir, tempfile.gettempdir()))
        letter_dir = Path(tempfile.gettempdir())
    for donor in donors.keys():
        letter_values = {'name': donor, 'amount': donors[donor][-1]}
        print(letter_values)
        letter = letter_dir / (donor + '.txt')
        print(letter)
        with letter.open("w") as fileio: fileio.write(letter_template.format(**letter_values))
        fileio.close()

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
        try:
            if menu_dispatch.get(int(option))() == 1: break # breaking out of the loop /appears/ to be the cleanest way to do this, if I dispatch to quit() the loop is still repeating
        except:
            continue
