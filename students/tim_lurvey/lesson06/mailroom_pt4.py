#!/usr/bin/env python
__author__ = 'Tim Lurvey, ig408c'

import sys
import os


class RunningTotal(object):
    """A class for storing donor data"""
    _key = ""
    _total = 0.
    _count = 0

    def __init__(self, new_key: str, total: float = 0., count: int = 0):
        self._set_key(new_key=new_key)
        self._set_total(new_total=total)
        self._set_count(new_count=count)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._set_key(new_key=new_key)

    def _set_key(self, new_key):
        try:
            assert isinstance(new_key, str)
            self._key = new_key
        except AssertionError:
            raise TypeError("Error:key must be a string")

    @property
    def total(self):
        return self._total

    def _set_total(self, new_total):
        try:
            self._total = float(new_total)
        except AssertionError:
            raise TypeError("Error:total must be numeric")

    @property
    def count(self):
        return self._count

    def _set_count(self, new_count):
        try:
            assert isinstance(new_count, int)
            self._count = new_count
        except AssertionError:
            raise TypeError("Error:key must be a integer")

    def add_to_total(self, ammount):
        self._total = self.total + ammount
        self._count += 1

    @property
    def average(self):
        return (self._total / self._count)


my_data = set()
my_data.add(RunningTotal(new_key='Tom Hanks', total=24536.20, count=3))
my_data.add(RunningTotal(new_key='Barry Larkin', total=4521., count=3))
my_data.add(RunningTotal(new_key='Mo Sizlack', total=88.88, count=2))
my_data.add(RunningTotal(new_key='Anonymous', total=100., count=1))
my_data.add(RunningTotal(new_key='Donnald Trump', total=1., count=3))


def get_name_matches(name: str, data: any=my_data):
    return [o for o in data if name.lower() in o.key.lower()]


def add_new_name(new_name: str, data: any=my_data):
    if len(get_name_matches(name=new_name, data=data)) == 0:
        new_obj = RunningTotal(new_key=new_name)
        if hasattr(data, 'add'):
            data.add(new_obj)
        elif hasattr(data, 'append'):
            data.append(new_obj)
        else:
            raise AttributeError("Data object cannot be added to")
        # recast object the same pointer?
        # l = list(data)
        # l.append(RunningTotal(new_key=new_name))
        # data = type(data)(l)
        return True
    else:
        return False


def get_data_object(key: str, data: any=my_data):
    """get the data object of a name.  Add new name to object if none exists for name"""
    results = get_name_matches(name=key, data=data)
    if len(results) == 1:
        return results[0]
    elif len(results) == 0:
        if add_new_name(new_name=key, data=data):
            get_data_object(key=key, data=data)
        else:
            return None
    else:
        return None


def compose_email(name: str, new_donation: float = 0., data=my_data):
    """return the string of the formatted email"""
    # get data object from name
    donor_obj = get_data_object(key=name, data=data)
    # determine plurals
    if donor_obj.count < 1:
        s = ""
        is_are = "is"
    else:
        s = "s"
        is_are = "are"
    # create new donation string, if needed
    fnew_donation = ""
    if new_donation:
        donor_obj.add_to_total(ammount=new_donation)
        fnew_donation += "Thank you for your generous donation of $ {donation:.2f}.\n".format(donation=new_donation, )
    # format email string
    email_str = "\nHello {name},\n\n" \
                "{new_donation}" \
                "Your {count} donation{s}, totaling $ {total:.2f}, {is_are} greatly appreciated.\n\n" \
                "Thank you\n\n".format(name=donor_obj.key,
                                       new_donation=fnew_donation,
                                       count=donor_obj.count,
                                       s=s,
                                       total=donor_obj.total,
                                       is_are=is_are)
    return email_str


def add_donation(name: str = "", ammount: float = 0.):
    get_data_object(key=name).add_to_total(ammount=ammount)
    return True


def print_name_list():
    print_list = "The following names are available:\n"
    for i, item in enumerate(my_data):
        print_list += "{i:>3} : {name}\n".format(i=i, name=item.key)
    return print_list[:-1]


def send_thank_you(request: str = "", skip_donation: bool = False):
    """This method will send a thank you notice to a user in the database
    who has made a new donation."""
    # add the key is it is not in the database
    if request not in my_data:
        add_new_name(new_name=request)
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
    return compose_email(name=request, new_donation=float(donation))


def write_letter_to_path(name: str, message: str, pathx: str):
    with open(os.path.join(pathx, "thank_you_{}.txt".format(name).replace(" ", "_")), "w") as W:
        W.write(message)


def get_path_for_letters(write_path:str="", data=my_data):
    # get the path from the user
    while True:
        if not write_path:
            write_path += input("Enter a path to write Thank you messages to.\n>>> ").strip()
        if os.path.exists(write_path):
            break
        else:
            print("Error: '{}' not found".format(write_path))
    # write each donor's message to the path
    print("Writing ...")
    for o in data:
        write_letter_to_path(name=o.key,
                             message=compose_email(name=o.key, data=data),
                             pathx=write_path)
    return "Writing Complete"


def report_header():
    """ Print report in the following format:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24"""
    s = "\n"
    s += "Donor Name                | Total Given | Num Gifts | Average Gift\n"
    s += ("-" * 66) + "\n"
    return s


def report_data_line(name: str = "dafualt key", total: float = 0.0, count: int = 1):
    """create a single report line of formatted inputs"""
    ftotal = "$ {:.2f}".format(total)
    average = "$ {:.2f}".format(total / count)
    return "{name:<26}|{tot:>13}|{num:>11d}|{avg:>13}\n".format(name=name,
                                                                tot=ftotal,
                                                                num=count,
                                                                avg=average, )


def report(data=my_data):
    """Assemble the report string and return it"""
    s = ""
    for i, o in enumerate([o for o in data]):
        s += report_data_line(name =o.key,
                              total=o.total,
                              count=o.count
                              )
    s += ("-" * 66) + "\n"
    return s


def quit_program():
    """Exit the application by unseating the switch"""
    exit("\nGoodbye! Exiting program...")


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
        msg = "1 : See a list of donor names\n" \
              "2 : Print a Thank You to individual donor\n" \
              "3 : Create Report of all donors\n" \
              "4 : Send Thank you to all donors\n" \
              "q : quit\n>>> "
        # Query
        request = input("Select:\n{}".format(msg)).strip()
        # Error check
        if len(request) > 1:
            print("\nplease input only '1' or '2' or 'q'\n")
            # keep looping until valid result
            continue
        # Define the logic
        logic_dict = {'1': print_name_list,
                      '2': send_thank_you,
                      '3': report,
                      '4': get_path_for_letters,
                      'q': quit_program}
        # Get the corresponding function and execute it
        print(logic_dict.get(request, error)())


if __name__ == '__main__':
    main(sys.argv[1:])
