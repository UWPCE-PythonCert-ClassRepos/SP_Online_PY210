#!/usr/bin/env python
__author__ = 'Tim Lurvey, ig408c'

import sys

sys.path.append('C:\\Users\\ig408c\\Documents\\!SCHOOL\\!Python\\SP_Online_PY210-master\\students\\tim_lurvey')
from myClasses import bunch

myData = {}
myData.update({'Tom Hanks': bunch(total=24536.20, number=3)})
myData.update({'Barry Larkin': bunch(total=4521., number=3)})
myData.update({'Mo Sizlack': bunch(total=88.88, number=2)})
myData.update({'Anonymous': bunch(total=100., number=1)})
myData.update({'Donnald Trump': bunch(total=1., number=3)})


def add_new_name(name: str = ""):
    myData.update({name: bunch(total=0., number=0)})
    return True


def compose_email(name: str = "", donation: float = 0., data: any = None):
    """return the string of the formatted email"""
    if data.number < 1:
        s = ""
        is_are = "is"
    else:
        s = "s"
        is_are = "are"
    #
    email_str = "\nHello {name},\n\n" \
                "Thank you for your generous donation of $ {donation:.2f}.\n" \
                "Your {count} donation{s}, totaling $ {total:.2f}, {is_are} greatly appreciated.\n\n" \
                "Thank you\n\n".format(name=name,
                                       donation=donation,
                                       count=data.number,
                                       s=s,
                                       total=data.total,
                                       is_are=is_are)
    return email_str


def add_donation(name: str = "", ammount: float = 0.):
    data = myData.get(name)
    data.total += float(ammount)
    data.number += 1
    myData.update({name: data})
    return True


def print_name_list():
    print_list = "The following names are available:\n"
    for i, item in enumerate(myData.items()):
        print_list += "{i:>3} : {name}\n".format(i=i, name=item[0])
    print(print_list[:-1])
    return True


def send_thank_you():
    """This method will send a thank you notice to a user in the database
    who has made a new donation."""
    request = input('Enter a full name or "list" to view names\n>>> ')
    #
    if 'list' == request.strip().lower():
        print_name_list()
        return True
    else:
        # add the name is it is not in the database
        if request not in myData:
            add_new_name(name=request)
        # get the donation amount
        donation = input("Enter amount:").replace("$", "").strip()
        # if the number isn't castable to a float, warn user and exit function.
        try:
            float(donation)
        except ValueError:
            print("The value you entered is not a valid donation.  Error: '{}'\n>>> ".format(donation))
            return True
        # add the donation to their existing amount
        add_donation(name=request, ammount=float(donation))
        # return the email string
        print(compose_email(name=request, donation=float(donation), data=myData.get(request)))
        return True


def report():
    """ Print report in the following format:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24"""
    s = "\n"
    s += "Donor Name                | Total Given | Num Gifts | Average Gift\n"
    s += ("-" * 66) + "\n"
    for i, data in enumerate(myData.items()):
        total = "$ {:.2f}".format(data[1].total)
        average = "$ {:.2f}".format(data[1].total / data[1].number)
        s += "{name:<26}|{tot:>13}|{num:>11d}|{avg:>13}\n".format(name=data[0],
                                                                  tot=total,
                                                                  num=data[1].number,
                                                                  avg=average, )
    s += ("-" * 66) + "\n"
    print(s)
    return True


def quit():
    """Exit the application by unseating the switch"""
    print("\nGoodbye! Exiting program...")
    return False

def error(input: str = ""):
    """Report an error"""
    print("\nError on input.  Invalid selection \"{}\"".format(input))
    return True


def main(args):
    """This is the controlling logic for the program.  The main loop will
    repeat forever until the user specifies to quit."""
    # this is the switch variable
    CONTINUE = True
    # while switch is true, loop
    while CONTINUE:
        # Define main input
        msg = """1 : Send a Thank You\n2 : Create a Report\nq : quit\n>>> """
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
                      'q':quit}
        # Get the corresponding function and execute it
        CONTINUE = logic_dict.get(request, error)()


if __name__ == '__main__':
    main(sys.argv[1:])
