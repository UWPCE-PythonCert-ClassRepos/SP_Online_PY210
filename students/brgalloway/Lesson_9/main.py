import mailroom_oo.cli_main as cli
import mailroom_oo.database as db 
import mailroom_oo.donor_models as db

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

if __name__ == '__main__':
    menu_selection()
    