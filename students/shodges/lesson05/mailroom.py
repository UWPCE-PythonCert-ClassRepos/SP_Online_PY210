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
            amount = input('Please enter a donation amount: ')
            try:
                donors[donor].append(float(amount))
            except KeyError:
                donors[donor] = [float(amount)]
            except ValueError:
                print('Invalid donation amount {}\n'.format(amount))
                if len(donors[donor]) == 0: # we caught the exceptions for this case but we'll remove the entry too
                    del(donors[donor])
                print(donors)
                break # this isn't necessary to get to the main menu but if we don't call it, it will raise a ValueError in the main try/except block
            total = sum(donors[donor])
            letter_values = {'name': donor, 'amount': float(amount), 'total': total}
            print(("""



{}


""".format(letter_template)).format(**letter_values)) # I'm doing this because I like the extra whitespace when the letter is in-line, otherwise it gets smooshed with the prompts
            break

def generate_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    donor_report = sorted([[x, len(donors[x]), sum(donors[x])] for x in donors], key = lambda x: x[2], reverse = True)
    for item in donor_report:
        try:
            report_output = {'name': item[0], 'total': item[2], 'gifts': item[1], 'average': (item[2] / item[1])}
            print('{name:24}  ${total:10.2f}   {gifts:10d}   ${average:12.2f}'.format(**report_output))
        except ZeroDivisionError: # this occurs if an invalid donation amount is entered in send_thank_you for a new donor and the donor entry isn't removed
            continue
    print('')

def save_all_letters():
    letter_dir = Path(input('Please specify a directory to save letters in: '))
    letter_dir = letter_dir / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
    try:
        letter_dir.mkdir(exist_ok=True)
    except NotADirectoryError:
        print('{} is not a directory; using {}'.format(letter_dir, tempfile.gettempdir()))
        letter_dir = Path(tempfile.gettempdir())
    except FileNotFoundError:
        print('{} was not found; using {}'.format(letter_dir, tempfile.gettempdir()))
        letter_dir = Path(tempfile.gettempdir())
    except PermissionError:
        print('Unable to create folder {}, using {}'.format(letter_dir, tempfile.gettempdir()))
        letter_dir = Path(tempfile.gettempdir())

    for donor in donors.keys():
        try:
            letter_values = {'name': donor, 'amount': donors[donor][-1], 'total': sum(donors[donor])}
        except IndexError: # this occurs if an invalid donation amount is entered in send_thank_you for a new donor and the donor entry isn't removed
            continue
        letter = letter_dir / (donor.replace(' ', '_') + '.txt')
        try:
            with letter.open("w") as fileio:
                fileio.write(letter_template.format(**letter_values))
        except (NotADirectoryError, FileNotFoundError, PermissionError):
            print('Error creating {}'.format(letter))
            continue
    else:
        print('Saved letters in {}\n'.format(letter_dir.absolute()))

if __name__ == '__main__':
    menu_dispatch = {1: send_thank_you, 2: generate_report, 3:save_all_letters, 4: quit}
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
            menu_dispatch.get(int(option))()
        except (TypeError, ValueError):
            print('Invalid option {}\n'.format(option))
