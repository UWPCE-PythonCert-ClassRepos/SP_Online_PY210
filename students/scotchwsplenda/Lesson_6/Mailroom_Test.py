import Mailroom_4 as mail
import os

# ----- TEST FUNCTIONS -----


def get_updated_donors_list():
    '''Generate updated donors variables for testing purposes.'''
    return mail.donors.keys()


def get_text(filepath):
    '''Get text from the specified written letter for testing.'''

    with open(filepath, "r") as readfile:
        contents = readfile.read()
        return contents
