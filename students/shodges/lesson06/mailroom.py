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

letter_whitespace = """



{}


"""

###### BEGIN BLOCK OF BUSINESS FUNCTIONS (NOW WITH MORE UNIT TESTS!) ######

def format_letter(donor, extra_whitespace = False):
    try:
        letter_values = {'name': donor, 'amount': donors[donor][-1], 'total': sum(donors[donor])}
    except KeyError:
        return False

    if extra_whitespace == True: # I still like the extra whitespace in the user interactive mode :)
        return (letter_whitespace.format(letter_template)).format(**letter_values)
    else:
        return letter_template.format(**letter_values)


def add_donor_record(donor, amount):
    try:
        donors[donor].append(float(amount))
    except KeyError:
        pass
    except ValueError:
        return False
    else:
        return True

    try:
        donors[donor] = [float(amount)]
    except ValueError:
        return False
    else:
        return True


def generate_report():
    report_lines = ['{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')]
    report_lines.append('-'*68)
    donor_report = sorted([[x, len(donors[x]), sum(donors[x])] for x in donors], key = lambda x: x[2], reverse = True)
    for item in donor_report:
        try:
            report_output = {'name': item[0], 'total': item[2], 'gifts': item[1], 'average': (item[2] / item[1])}
            report_lines.append('{name:24}  ${total:10.2f}   {gifts:10d}   ${average:12.2f}'.format(**report_output))
        except ZeroDivisionError: # this occurs if an invalid donation amount is entered in send_thank_you for a new donor and the donor entry isn't removed
            continue
    return report_lines


def create_letter_dir(dirpath):
    letter_dir = Path(dirpath) / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
    try:
        letter_dir.mkdir(exist_ok=True)
    except (NotADirectoryError, FileNotFoundError, PermissionError):
        pass
    else:
        return letter_dir

    letter_dir = Path(tempfile.gettempdir()) / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
    try:
        letter_dir.mkdir(exist_ok=True)
    except (NotADirectoryError, FileNotFoundError, PermissionError):
        return False
    else:
        return letter_dir


def save_letter(dirpath, donor):
    letter = dirpath / (donor.replace(' ', '_') + '.txt')
    try:
        with letter.open("w") as fileio:
            fileio.write(format_letter(donor))
    except (FileNotFoundError, PermissionError):
        return False
    except TypeError:
        try:
            letter.unlink()
        except (PermissionError, OSError, FileNotFoundError):
            pass
        finally:
            return False
    else:
        return letter


###### BEGIN BLOCK OF USER INTERACTION FUNCTIONS ######
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
            if add_donor_record(donor, amount) == False:
                print('Invalid donation amount {}\n'.format(amount))
            else:
                print(format_letter(donor, True))
            break


def print_report():
    print('\n'.join(generate_report()))
    print()

def save_all_letters():
    letter_dir = create_letter_dir(input('Please specify a directory to save letters in: '))

    if letter_dir == False:
        print('Error creating letter directory.')
    else:
        for donor in donors.keys():
            letter = save_letter(letter_dir, donor)
            if letter != False:
                print('{} created successfully'.format(letter.absolute()))


if __name__ == '__main__':
    menu_dispatch = {1: send_thank_you, 2: print_report, 3:save_all_letters, 4: quit}
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
