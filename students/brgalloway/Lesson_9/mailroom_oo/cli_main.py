import sys
from mailroom_oo import methods as m
from mailroom_oo import donor_models as d

class CliMenu(object):
    '''
    cli menu class includes a prompt, dispatch dictionary, and exit method
    '''
    def __init__(self):
        # menu prompt and options to select from
        self.prompt = "Choose one of the following options. \n\n" \
            "1 - Send a Thank You to a single donor \n" \
            "2 - Create a Report \n" \
            "3 - Send letters to all donors \n" \
            "4 - Quit \n" \
            ">> "

        # value returned from choice keys
        # TODO configure options 1-3 as classes
        self.main_dispatch = {
            "1": d.find_donor,
            "2": m.generate_report,
            "3": m.bulk_thankyou,
            "4": self.quit_app
        }
    
    def quit_app(self):
        return "quit"

class MenuSelection(CliMenu):
    '''
    Menu selection class, asks user for options until user selects or chooses from the prompt
    '''
    def selector(self):
        
        while True:
            response = input(self.prompt)
            response = response.lower()
            response = response.strip()
            try:
                if self.main_dispatch[response]() == "quit":
                    sys.exit()
            except KeyError:
                print("\n\ninvalid response\n")
