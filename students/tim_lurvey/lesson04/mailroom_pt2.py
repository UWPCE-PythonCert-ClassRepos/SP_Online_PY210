#!/usr/bin/env python
__author__ = 'Tim Lurvey, ig408c'

import sys
import os
from lurvey_classes import bunch

my_data = {}
my_data.update({'Tom Hanks': bunch(total=24536.20, number=3)})
my_data.update({'Barry Larkin': bunch(total=4521., number=3)})
my_data.update({'Mo Sizlack': bunch(total=88.88, number=2)})
my_data.update({'Anonymous': bunch(total=100., number=1)})
my_data.update({'Donnald Trump': bunch(total=1., number=3)})


def add_new_name(name: str = ""):
    my_data.update({name: bunch(total=0., number=0)})
    return True


def compose_email(name: str = "", donation: float = 0., data: bunch = None):
    """return the string of the formatted email"""
    if data.number < 1:
        s = ""
        is_are = "is"
    else:
        s = "s"
        is_are = "are"
    #
    new_donation = ""
    if donation:
        new_donation += "Thank you for your generous donation of $ {donation:.2f}.\n".format(donation=donation,)
    #
    email_str = "\nHello {name},\n\n" \
                "{new_donation}" \
                "Your {count} donation{s}, totaling $ {total:.2f}, {is_are} greatly appreciated.\n\n" \
                "Thank you\n\n".format(name=name,
                                       new_donation=new_donation,
                                       count=data.number,
                                       s=s,
                                       total=data.total,
                                       is_are=is_are)
    return email_str


def add_donation(name: str = "", ammount: float = 0.):
    data = my_data.get(name)
    data.total += float(ammount)
    data.number += 1
    my_data.update({name: data})
    return True


def print_name_list():
    print_list = "The following names are available:\n"
    for i, item in enumerate(my_data.items()):
        print_list += "{i:>3} : {name}\n".format(i=i, name=item[0])
    return print_list[:-1]


def send_thank_you(request: str = "", skip_donation: bool = False):
    """This method will send a thank you notice to a user in the database
    who has made a new donation."""
    if not request:
        request += input('Enter a full name or "list" to view names\n>>> ')
    #
    if 'list' == request.strip().lower():
        return print_name_list()
    else:
        # add the name is it is not in the database
        if request not in my_data:
            add_new_name(name=request)
        #
        donation = 0.
        if not skip_donation:
            # get the donation amount
            # if the number isn't castable to a float, warn user and exit function.
            try:
                donation += float(input("Enter amount:\n>>> ").replace("$", "").strip())
            except ValueError:
                "The value you entered is not a valid donation.  Error: '{}'\n>>> ".format(donation)
            # add the donation to their existing amount
            add_donation(name=request, ammount=float(donation))
        # return the email string
        return compose_email(name=request, donation=float(donation), data=my_data.get(request))


def send_letters_all():
    # get the path from the user
    while True:
        pathx = input("Enter a path to write Thank you messages to.\n>>> ").strip()
        if os.path.exists(pathx):
            break
        else:
            print("Error: '{}' not found".format(pathx))
    # write each donor's message to the path
    print("Writing ...")
    for donor,data in my_data.items():
        with open(os.path.join(pathx, "thank_you_{}.txt".format(donor).replace(" ","_")), "w") as W:
            W.write(compose_email(name=donor, data=data))
    return "Writing Complete"


def report():
    """ Print report in the following format:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24"""
    s = "\n"
    s += "Donor Name                | Total Given | Num Gifts | Average Gift\n"
    s += ("-" * 66) + "\n"
    for i, data in enumerate(my_data.items()):
        total = "$ {:.2f}".format(data[1].total)
        average = "$ {:.2f}".format(data[1].total / data[1].number)
        s += "{name:<26}|{tot:>13}|{num:>11d}|{avg:>13}\n".format(name=data[0],
                                                                  tot=total,
                                                                  num=data[1].number,
                                                                  avg=average, )
    s += ("-" * 66) + "\n"
    return s


def quit_program():
    """Exit the application by unseating the switch"""
    print("\nGoodbye! Exiting program...")
    exit()


def error(inp: str = ""):
    """Report an error"""
    print("\nError on input.  Invalid selection \"{}\"".format(inp))
    return True


def main(args):
    """This is the controlling logic for the program.  The main loop will
    repeat forever until the user specifies to quit."""
    # while switch is true, loop
    while True:
        # Define main input
        msg = "1 : Send a Thank You\n" \
              "2 : Create a Report\n" \
              "3 : Send Thank you to all donors\n" \
              "q : quit\n>>> "
        # Query
        request = input("Select:\n{}".format(msg)).strip()
        # Error check
        if len(request) > 1:
            print("\nplease input only '1' or '2' or 'q'\n")
            # keep looping until valid result
            continue
        # Define the logic
        logic_dict = {'1':send_thank_you,
                      '2':report,
                      '3':send_letters_all,
                      'q':quit_program}
        # Get the corresponding function and execute it
        print(logic_dict.get(request, error)())


if __name__ == '__main__':
    main(sys.argv[1:])
