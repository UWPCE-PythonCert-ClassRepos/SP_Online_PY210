#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# CLI and Main program
# Created 1/17/2021 - csimmons

text_dict = {
    'header1': '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name',  '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift '),
    'header2': ('_ ' * 32) + '\n',
    'info_row': '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format,
    'letter': (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands, perhaps\n'
        'even millions, enjoy the wonders of the Emerald city!\n\n'
        'Sincerely,\n\n'
        'H.P. Lovecraft \n')),
    'gift_prompt': '\n'.join(('Please enter the donation amount: ',
                '>>>  ')),
    'donor_prompt': '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '>>>  ')),
    'donation_err': '\nError: Please enter a number or decimal ("$" and commas not needed).',
    'letter_err': '\nError: The letter for {} not generated. Please       check the destination folder',
    'donor_prompt': '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '\n>>>  ')),
    'menu_prompt': '\n'.join(('Please choose from the options below:\n',
          '1 - Add a new donor',
          '2 - Update existing donor',
          '3 - List current donors',
          '4 - Print donor database',
          '5 - Send thank you letters to all donors',
          '6 - Quit',
          '>>> '))
    }

    