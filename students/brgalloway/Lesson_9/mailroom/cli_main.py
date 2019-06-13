import mailroom_oo.donor_collection as db 
import mailroom.donor_models as d

menu_selection = cli.MenuSelection()
menu_selection = menu_selection.selector()

oop_donors_list = []

d1 = d("Jeff Bezos")
d2 = d("Paul Allen")
d3 = d("William Gates, III")
d4 = d("Bill Ackman")
d5 = d("Mark Zuckerberg")

oop_donors_list = [d1, d2, d3, d4, d5]

donor_db = db(d1)

import sys
from mailroom_oo import methods as m
from mailroom_oo import donor_models as d


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


def menu_selection(self):
    
    while True:
        response = input(self.prompt)
        response = response.lower()
        response = response.strip()
        try:
            if self.main_dispatch[response]() == "quit":
                sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

if __name__ == '__main__':
    menu_selection()