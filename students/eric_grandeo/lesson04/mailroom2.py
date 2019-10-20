#!/usr/bin/env python3


#switch between users selections
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


def thank_you():
    pass

def create_report():
    pass

def quit_program():
    return "exit menu"

def display_donors():
    return donors.keys()


#donors as a dict
donors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54]}

main_prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          ">>> "))

main_dispatch = {"1" : thank_you,
                "2" : create_report,
                "3" : quit_program,}

sub_prompt = "\n".join(("Please enter one of the following",
            "A full name",
            "Type list to see all name",
            "Enter 'q' to quit",
            ">>> "))

sub_dispatch = {"List" : display_donors,
                "Q" : quit_program}

#may need to change this to menu selection
if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)

