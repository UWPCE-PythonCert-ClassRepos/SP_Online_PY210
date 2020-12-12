#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson03
# Mailroom Part 1 (mailroom.py)
# Steve Long 2020-10-03 | v0
#
# Requirements:
# =============
#
# This is the first in a four-part that will make use of your Python
# programming skills as you develop them during this course.
#
# Overall Program Goal
# --------------------
#   You work in the mail room at a local charity. Part of your job is to write
#   incredibly boring, repetitive emails thanking your donors for their
#   generous gifts. You are tired of doing this over and over again, so you've
#   decided to let Python help you out of a jam and do your work for you.
#
# The Program: Part 1
# -------------------
#   Write a small command-line script called "mailroom.py". This script should
#   be executable. The script should accomplish the following goals:
#
#   (1) It should have a data structure that holds a list of your donors and a
#       history of the amounts they have donated. This structure should be
#       populated at first with at least five donors, with between 1 and 3
#       donations each. You can store that data structure in the global
#       namespace.
#
#   (2) The script should prompt the user (you) to choose from a menu of 3
#       actions: "Send a Thank You", "Create a Report" or "quit".
#
# Detail Requirements
# -------------------
#
#   1       Send a Thank You
#
#   1.1     If the user (you) selects "Send a Thank You" option, prompt for a
#           Full Name.
#
#   1.1.1   If the user types "list" show them a list of the donor names and
#           re-prompt.
#
#   1.1.2   If the user types a name not in the list, add that name to the data
#           structure and use it.
#
#   1.1.3   If the user types a name in the list, use it.
#
#   1.2     Once a name has been selected, prompt for a donation amount...
#
#   1.2.1   Convert the amount into a number; it is OK at this point for the
#           program to crash if someone types a bogus amount.
#
#   1.2.2   Add that amount to the donation history of the selected user.
#
#   1.2.3   Finally, use string formating to compose an email thanking the
#           donor for their generous donation. Print the email to the terminal
#           and return to the original prompt.
#
#   1.3     It is fine (for now) for the program not to store the names of the
#           new donors that had been added, in other words, to forget new
#           donors once the script quits running.
#
#   2       Create a Report
#
#   2.1     If the user (you) selected "Create a Report," print a list of your
#           donors, sorted by total historical donation amount.
#
#   2.1.1   Include donor name, total donated, number of donations, and average
#           donation amount as values in each row. You do not need to print out
#           all of each donor's donations, just the summary info.
#
#   2.1.2   Using string formatting, format the output rows as nicely as
#           possible. The end result should be tabular (values in each column
#           should align with those above and below). [See original assignment
#           PDF document for example report appearance.]
#
#   2.1.3   After printing this report, return to the original prompt.
#
#   2.2     At any point, the user should be able to quit their current task
#           and return to the original prompt.
#
#   2.3     From the original prompt, the user should be able to quit the
#           script cleanly.
#
#   Guidelines
#   ----------
#
#   (1) First, factor your script into separate functions. Each of the above
#       tasks can be accomplished by a series of steps. Write discreet
#       functions that accomplish individual steps and call them.
#
#   (2) Second, use loops to control the logical flow of your program.
#       Interactive programs are a classic use case for the while loop.
#
#   (3) Of course, input() will be useful here.
#
#   (4) Put the functions you write into the script at the top.
#
#   (5) Put your main interaction into an if __name__ == '__main__' block.
#
# Assumptions:
# ============
#
#   - A degree of design freedom is allowed for the solution.
#   - Requirement 1.3 is not truly a requirement.
#
# Implementation:
# ===============
#
#   - Requirements satisfied as indicated in source code.
#   - Executable via ./mailroom.py.
#   - Function names, variables, block comments, line continuation, and
#     operator spacing per PEP8 guidelines.
#   - Data manipulation implemented separately from user interface (UI).
#   - Solution implemented with 3-level UI:
#
#       Main UI
#           - display all donors
#           - display report
#           - add new donor
#           - quit
#           - select donor => Donor UI
#                           - add new gift
#                           - exit to Main UI
#                           - thank-you message => Messenger UI
#                                                   - send message
#                                                   - exit to Donor UI
#
# Script Usage:
# =============
#
#   ./mailroom.py
#
# Issues:
# =======
#
#   Requirements could use a little work.
#
# History:
# ========
# 000/2020-10-03/sal/Created.
#
# =============================================================================

from functools import reduce

# -- Application constants ---------------------------------------------------

_APP_TITLE = "Mailroom"
_APP_VERSION = "1.0"
_APP_WIDTH = 100

# -- Command constants -------------------------------------------------------

_CMD_EXIT = ":EXIT"
_CMD_LIST = ":LIST"
_CMD_NEW = ":NEW"
_CMD_NONE = ":NONE"
_CMD_QUIT = ":QUIT"
_CMD_REPORT = ":REPORT"
_CMD_SEND = ":SEND"
_CMD_MESSENGER = ":MESSENGER"

# -- Root data container -----------------------------------------------------

_Donors = {}

# -- Str utils ---------------------------------------------------------------


def clean_name(name):
    """
    Remove extraneous white space.
    """
    comps = name.split()
    name = " ".join(comps)
    return name


def check_name_case(name, override_correction=True):
    """
    Clean and capitalize a name. If adjusted name is different from
    input, optionally allow the user choose preferred spelling. This
    will account for mixed-case names (Irish, Scot, Klingon, whatever.)
    """
    revised_name = " ".join(map(lambda nc: nc.capitalize(), name.split()))
    if (override_correction):
        if (name != revised_name):
            answer = input("Use \"{}\" [Y] or original spelling [N]?: "
                           .format(revised_name))
            if (answer[0:1].upper() == "Y"):
                name = revised_name
            else:
                print("Reverting to original spelling")
    return name


def is_floatable(v):
    """
    Can a value be coerced to a floating-point value? Implemented
    because just checking for <v>.isnumeric() won't work with a value
    containing a decimal.
    """
    status = False
    f = None
    try:
        f = float(v)
        status = (f is not None)
    except Exception:
        status = False
    return status


def is_intable(v):
    """
    Can a value be coerced to an int value? Implemented to maintain
    similarity with is_floatable for interpreting int values.
    NOTE: I will come up with a better name for this series of
          functions later because this looks too much like a predicate
          testing for something 'in a table.'
    """
    status = False
    i = None
    try:
        i = int(v)
        status = (i is not None)
    except Exception:
        status = False
    return status


# -- About the data structures -----------------------------------------------
#
# donor   -  An abstraction implemented as a tuple. Implemented as a tuple to
#            minimize casual alteration of data. element structure by index:
#
#            0: Donor name (str).
#            1: Gifts (tuple of 0 or more floats).
#            2: Summation of gifts (float).
#            3: Average gift (float).
#
# _Donors -  A module global dictionary containing donors keyed on name.
# ----------------------------------------------------------------------------

# -- Donor cached attributes -------------------------------------------------


def donor_name(donor):
    """
    The donor's name (str). Initialized by input.
    """
    return donor[0]


def donor_total_gift(donor):
    """
    The donor's total gift value (float). Must be recalculated whenever
    a gift is added (or removed.)
    """
    return round(donor[2], 2)


def donor_average_gift(donor):
    """
    The donor's average gift value (float). Must be recalculated
    whenever a gift is added (or removed.)
    """
    return round(donor[3], 2)


# -- Donor modifiable cached attributes --------------------------------------


def donor_gifts(donor):
    """
    The donor's gift data (tuple of 0 or more floats). Initialized by
    input.
    """
    gifts = ()
    if (len(donor) > 1):
        gifts = donor[1]
    return gifts


# -- Donor uncached attributes -----------------------------------------------


def donor_gift_count(donor):
    """
    The number of gifts from the donor (int). Not cached because this
    would be redundant and potentially in conflict with the len()
    function when applied to donor gifts.
    """
    return len(donor_gifts(donor))


def donor_last_gift(donor):
    """
    Last gift of the donor's gift list.
    """
    last_gift = None
    if (donor_gift_count(donor) > 0):
        last_gift = (donor_gifts(donor))[-1]
    return last_gift


# -- Modifiable attribute utils ----------------------------------------------


def apply_donor_rules(donor):
    """
    Recalculate all of the donor's dependent attributes, update the
    donor aggregate, and return the revised donor.
    """
    #
    # Modifiable attribute.
    #
    gifts = donor_gifts(donor)
    #
    # Total gift rule.
    #
    gift_total = 0.00
    for gift in gifts:
        gift_total += gift
    gift_total = round(gift_total, 2)
    gift_count = len(gifts)
    #
    # Average gift rule.
    #
    gift_average = 0.00
    if (gift_count > 0):
        gift_average = round(gift_total/gift_count, 2)
    revised_donor = (donor_name(donor),
                     gifts,
                     gift_total,
                     gift_average)
    _Donors[donor_name(revised_donor)] = revised_donor
    return revised_donor


# -- Donor data load ----------------------------------------------------------

def load_donors_seq():
    """
    Retrieve the basic information about donors and their gifts.
    Returns a sequence of the form (<donor>*) where <donor> has the
    form (<name>, (<gift>*)). Names borrowed from Lectroid list. Gift
    values are random.
    Satisfies: requirement The Program: Part 1 (1)
    """
    donors = (("Rene Descartes", (21.00, 199.95, 2063.45, 77.00, 1638.00)),
              ("Immanuel Kant", (153784.00, 153784.00)),
              ("Soren Kierkegaard", (334.00, 43821.00, 3978.00)),
              ("Vandana Shiva", (661.12,)),
              ("Jean-Paul Sartre", ()),
              ("Albert Camus", (5000.00, 5000.00, 5000.00, 5000.00)),
              ("Ralph Ellison",
               (3950.00, 4051.00, 4152.00, 4253.00, 4354.00, 4455.00)
               ),
              ("Michel Foucault",
               (72452.00, 72454.00, 72936.00, 73024.00, 73918.00, 87270.00)
               ),
              ("David Hume",
               ()
               ),
              ("Thomas Aquinas",
               (75.00, 0.57)
               ),
              ("Friedrich Nietzsche",
               (602.05, 605.97, 618.26, 618.27, 620.06, 668.08, 668.08,
                703.52, 709.15, 712.01, 720.15
                )
               )
              )
    return donors


def load_donors():
    """
    Load donor basic information into _Donors. Returns int, the number
    of donors.
    """
    global _Donors
    _Donors = dict()
    for donor in load_donors_seq():
        donor = apply_donor_rules(donor)
        name = donor_name(donor)
        if (name not in _Donors):
            _Donors[name] = donor
    return len(_Donors)


# -- Donor add/delete/edit ---------------------------------------------------


def get_donor(name):
    """
    Retrieve a donor by name. Returns donor tuple or None.
    """
    global _Donors
    donor = None
    if (name in _Donors):
        donor = _Donors[name]
    return donor


def add_donor(name):
    """
    Add a new donor to the donor aggregate. Returns True if successful,
    False otherwise.
    """
    global _Donors
    result = False
    if (name not in _Donors.copy()):
        _Donors[name] = (name, (), 0.00, 0.00)
        result = True
    return result


def remove_donor(name):
    """
    Remove a donor by name from the donor aggregate, returning the
    donor. Not used in mailroom part 1 assignment.
    """
    global _Donors
    donor = None
    if (name in _Donors):
        donor = _Donors.pop(name)
    return donor


def add_gift(donor_in, gift):
    """
    Add a gift to the donor. Returns True if successful, False
    otherwise.
    """
    success = False
    try:
        gifts = list(donor_gifts(donor_in))
        gifts.append(gift)
        donor = (donor_name(donor_in), gifts)
        apply_donor_rules(donor)
        success = True
    except Exception:
        success = False
    finally:
        return success


def calc_donor_data_width(v):
    """
    Calculate the required monospaced char count for a data value.
    Returns int value.
    """
    width = 0
    if (type(v) is int):
        width = len("{}".format(v))
    elif (type(v) is float):
        width = len("{}".format(round(v, 2)))
    elif (type(v) is str):
        width = len(v)
    else:
        width = len(f"{v}")
    return width


def get_col_names():
    """
    Names of columns for a donor gift report. Returns tuple of
    displayable column names. Implemented to provide flexibility for
    altering the set of donor attributes to be displayed.
    """
    return ("Donor Name", "Total Given", "Num Gifts", "Average Gift")


def get_report_attribute_accessors():
    """
    Accessors for donor report attributes. Returns tuple of
    functions. Implemented to provide flexibility for altering the set
    of donor attributes to be displayed.
    """
    return (donor_name, donor_total_gift, donor_gift_count, donor_average_gift)


def calc_col_widths(reported_donors):
    """
    Determine required column width for each reported donor's report
    attribute. Returns tuple of ints.
    """
    col_names = get_col_names()
    name_col_width = len(col_names[0])
    total_gift_col_width = len(col_names[1])
    gift_count_col_width = len(col_names[2])
    average_gift_col_width = len(col_names[3])
    for donor in reported_donors:
        name_col_width \
            = max(name_col_width,
                  calc_donor_data_width(donor_name(donor)))
        total_gift_col_width \
            = max(total_gift_col_width,
                  calc_donor_data_width(donor_total_gift(donor)))
        gift_count_col_width \
            = max(gift_count_col_width,
                  calc_donor_data_width(donor_gift_count(donor)))
        average_gift_col_width \
            = max(average_gift_col_width,
                  calc_donor_data_width(donor_average_gift(donor)))
    col_widths = [name_col_width,
                  total_gift_col_width,
                  gift_count_col_width,
                  average_gift_col_width
                  ]
    col_widths = tuple(col_widths)
    return col_widths


def justify(col_value, col_width, justification, prefix):
    """
    justify(<col_value>, <col_width>, <justification>, <prefix>)
    ------------------------------------------------------------
    Fixed width justified cell value for donor report.

    Entry: <col_value>     ::= String or numeric value
           <col_width>     ::= Monospaced char count width of column.
           <justification> ::= (L)eft- or (R)ight-justified column
                               cell.
           <prefix>        ::= Additional units prefix
    Exit:  Returns string <col_width> wide containing justified
           <col_value>.
    """
    just = (">" if (justification.upper() == "R") else "<")
    col_width = col_width - len(prefix)
    s = ("{}{}{}:{}{}{}".format(prefix, "{", "a", just, col_width, "}"))\
        .format(a=col_value)
    return s


def format_money(value, width):
    """
    Render a fixed-width str value for a monetary floating point value.
    Returns str value.
    """
    return justify("{:.2f}".format(round(value, 2)), width, "R", "$")


def format_int(value, width):
    """
    format_int()
    -------------------------
    Render a fixed-width cell value for an integer value. Returns
    str value.
    """
    return justify("{:d}".format(value), width, "R", "")


def format_str(value, width):
    """
    Render a fixed-width cell value a string value. Returns a str.
    """
    return justify(value, width, "L", "")


def make_report_row_separator(sep_char, col_widths):
    """
    Render a row separator to span the full width of a set of columns.
    Returns str value.
    """
    row_width = \
        reduce(lambda sum, w: sum + w, col_widths, 0)\
        + ((len(col_widths) - 1) * 3)
    return sep_char * row_width


def make_report_header(col_names, col_widths):
    """
    Render a donor report header (title and column rows.) Returns str
    value.

    Satisfies: requirement 2.1.2
    """
    s = "\nDonor Report"
    s = "{}\n{}".format(s, make_report_row_separator("=", col_widths))
    s = "{}\n{}".format(s, format_str(col_names[0], col_widths[0]))
    for n in range(1, len(col_names)):
        s = "{} | {}".format(s, format_str(col_names[n], col_widths[n]))
    s = "{}\n{}".format(s, make_report_row_separator("-", col_widths))
    return s


def make_report_row(donor, accessors, col_widths, col_fmts):
    """
    make_report_row(<donor>, <accessors>, <col_widths>, <col_fmts>)
    ---------------------------------------------------------------
    Rendor report data row for the donor.

    Entry: <donor>       ::= Donor data structure.
           <accessors>   ::= Donor attribute accessor functions.
           <col_widths>  ::= Monospaced char count widths for each
                             donor gift
                             attribute.
           <col_fmts>    ::= Formatting functions for each donor gift
                             attribute.
    Exit:  Returns a string for a row for a donor report.

    Satisfies: requirement 2.1.1
    """
    s = col_fmts[0](accessors[0](donor), col_widths[0])
    for n in range(1, len(accessors)):
        s = "{}   {}".format(s,
                             col_fmts[n](accessors[n](donor),
                                         col_widths[n]))
    return s


def make_donors_net_values_report(donors):
    """
    Render diplayable aggregate data to be appended to the report data
    table created in make_donors_report. Includes number of donors,
    total number of gifts, net gifts and average of donor gift
    averages.
    """
    donor_seq = list(donors.values())
    donor_count = len(donors)
    net_gifts = reduce(
                    lambda sum, donor: sum + donor_total_gift(donor),
                    donor_seq,
                    0.00)
    gift_count = reduce(
                        lambda sum, donor: sum + donor_gift_count(donor),
                        donor_seq,
                        0)
    average_gift = ((net_gifts/gift_count) if (gift_count > 0) else 0)
    label_width = 12
    value_width = 12
    data = ((("Donor count", label_width, format_str),
             (donor_count, value_width, format_int)),
            (("Gift count", label_width, format_str),
             (gift_count, value_width, format_int)),
            (("Net gifts", label_width, format_str),
             (net_gifts, value_width, format_money)),
            (("Average gift", label_width, format_str),
             (average_gift, value_width, format_money)))
    dpair = data[0]
    label_spec = dpair[0]
    label_str = label_spec[2](label_spec[0], label_spec[1])
    value_spec = dpair[1]
    value_str = value_spec[2](value_spec[0], value_spec[1])
    s = "{} = {}".format(label_str, value_str)
    for dpair in data[1:]:
        label_spec = dpair[0]
        label_str = label_spec[2](label_spec[0], label_spec[1])
        value_spec = dpair[1]
        value_str = value_spec[2](value_spec[0], value_spec[1])
        s = "{}\n{} = {}".format(s, label_str, value_str)
    return s


def make_donors_report(donors):
    """
    make_donors_report(<donors>)
    ----------------------------
    Generate a donor report string.

    Entry: <donors> ::= Dictionary of donors keyed on name.
    Exit:  Returns a string that looks like a table showing donor name
           and total value, number of, and average value of gifts.

    Satisfies: requirement 2
    """
    attr_accessors = get_report_attribute_accessors()
    col_names = get_col_names()
    col_fmts = tuple([format_str, format_money, format_int, format_money])
    reported_donors = tuple(
                        sorted(
                            list(donors.values()),
                            key=donor_total_gift,
                            reverse=True
                            )
                        )
    col_widths = calc_col_widths(reported_donors)
    separator = make_report_row_separator("-", col_widths)
    displayable = make_report_header(col_names, col_widths)
    for donor in reported_donors:
        report_row = make_report_row(
                        donor, attr_accessors, col_widths, col_fmts
                        )
        displayable = "{}\n{}".format(displayable, report_row)
    displayable\
        = "{}\n{}\n{}\n{}"\
          .format(
            displayable,
            separator,
            make_donors_net_values_report(donors),
            separator
            )
    return displayable


# -- UI utilities ------------------------------------------------------------


def make_menu_prompt(menu_directions):
    """
    Render a command-line user prompt consisting of a UI name and key
    input options.
    """
    prompt = "INPUT: {} > ".format(menu_directions)
    return prompt


def sorted_donor_names(donors):
    """
    Retrieve the sorted names of a dictionary donors. Argument used to
    provide flexibility for allowing a subset of donors (instead of
    _Donors). Returns a list of donor tuples.
    """
    return list(sorted(list(donors.keys())))


def generate_message(donor):
    """
    Generate thank-you message for donor's last gift.

    Satisfies: requirement 1.2.3
    """
    dname = donor_name(donor)
    last_gift = donor_last_gift(donor)
    if (last_gift is None):
        msg = ("  Please consider making a gift to our organization."
               " It is tax deductible.")
    else:
        msg = "  Thanks for your recent gift of ${:.2f}.".format(last_gift)
    fmt = "  Dear {},\n\n  {}\n\n  Regards,\n\n  ACME Charities"
    email_text = fmt.format(dname, msg)
    fmt = "\nWill transmit the following message to donor {}:\n\n{}\n"
    msg = fmt.format(dname, email_text)
    return msg


# -- User-input translation --------------------------------------------------


def is_cmd(choice):
    """
    Is does a command-line entry have the format of an application
    command? Returns bool value.
    """
    status = False
    if (type(choice) is str):
        status = (choice[0:1] == ":")
    return status


def interpret_response(response, override_correction=True):
    """
    Interpret command-line user response as a command, an integer
    value, a floating point value, or a string (cleaned, capitalized)
    value. Returns str value.
    """
    response = clean_name(response)
    if (is_cmd(response)):
        choice = response[0:2].upper()
        #
        # As long as the first two chars of <response> match a defined
        # command, it will be interpreted as a command.
        #
        if (choice == ":L"):
            choice = _CMD_LIST
        elif (choice == ":M"):
            choice = _CMD_MESSENGER
        elif (choice == ":N"):
            choice = _CMD_NEW
        elif (choice == ":Q"):
            choice = _CMD_QUIT
        elif (choice == ":R"):
            choice = _CMD_REPORT

        elif (choice == ":S"):
            choice = _CMD_SEND
        elif (choice == ":X"):
            choice = _CMD_EXIT
        else:
            #
            # <response> looks like a command but isn't.
            #
            choice = response.upper()
    else:
        if (is_floatable(response)):
            #
            # <response> is probably a gift.
            #
            choice = response
        elif (is_intable(response)):
            #
            # <response> is probably a choice index.
            #
            choice = response
        else:
            #
            # <response> is probably a donor name but could be nonsense.
            #
            choice = check_name_case(response, override_correction)
    return choice


# -- One-line layout and information printing --------------------------------


def print_app_title():
    """
    Print command-line application banner for startup.
    """
    print("{}\n".format("=" * _APP_WIDTH))
    ui_title = "{} v{}".format(_APP_TITLE, _APP_VERSION)
    print("\n{}".format(ui_title))


def print_ui_header(ui_title):
    fmt = "\n{}:-<{}{}".format("{", _APP_WIDTH, "}")
    print(fmt.format("-- {} ".format(ui_title)))


def print_ui_menu_break_line():
    """
    Print a line of chars a command-line screen visual break.
    """
    print("\n{}".format("-" * _APP_WIDTH))


def print_vmsg(ver_name, data, msg):
    """
    Print an input data verification failure message of the form
    'ERROR: Rule: <ver_name> (<data>) <msg>'.
    """
    print("\nERROR: Rule: {} ({}): {}\n".format(ver_name, data, msg))


# -- Data verification rules ------------------------------------------------


def verify_existing_donor_name(name):
    """
    Verify that a donor <name> exists. If verification fails, print
    message. Returns True if <name> is verified.

    Rule: The name shall exist in donor aggregate. Context:
          Retrieving a donor by name.
    """
    global _Donors
    ver_name = "existing-donor-name"
    verified = False
    if (name in _Donors):
        verified = True
    else:
        print_vmsg(ver_name, name, "Donor does not exist")
    return verified


def verify_existing_donor_id(donor_seq, id):
    """
    Verify that a donor <id> exists in a donor display sequence. If
    verification fails, print message. Returns True if <id> is
    verified.

    Rule: The ID of a donor shall be 1 greater than an index in a donor
          display sequence. Context: Retrieving a donor from an
          enumerated display list.
    """
    ver_name = "existing-donor-id"
    verified = False
    if ((id > 0) and (id <= len(donor_seq))):
        verified = True
    else:
        print_vmsg(ver_name, id, "Not a valid ID")
    return verified


def verify_new_donor(name):
    """
    Verify that a donor <name> does not yet exist. . If verification
    fails, print message. Returns True if <name> is verified.

    Rule: The name shall not exist in donor aggregate. Context: Adding
          a new donor.
    """
    global _Donors
    ver_name = "new-donor-name"
    verified = False
    if (len(name) > 1):
        if (":" not in name):
            if (not name.isnumeric()):
                if (name not in _Donors):
                    verified = True
                else:
                    print_vmsg(ver_name, name, "Donor already exists")
            else:
                print_vmsg(ver_name, name, "Donor name cannot be numeric")
        else:
            print_vmsg(ver_name, name, "Donor name cannot contain ':'")
    else:
        print_vmsg(ver_name, name, "Donor name must be greater than 1 char")
    return verified


def verify_gift(gift):
    """
    Verify that a gift value is acceptable. If verification fails,
    print message. Returns True if <gift> is verified.

    Rule: Gift value ($) must be a numeric value > 0. Context:
          Entering a gift value.
    """
    ver_name = "gift-value"
    verified = False
    data_type = type(gift)
    if ((data_type is int) or (data_type is float)):
        if (gift > 0.00):
            verified = True
        else:
            print_vmsg(ver_name, gift, "Value must be > 0.00")
    elif (data_type is str):
        if (is_floatable(gift)):
            gift = round(float(gift), 2)
            if (gift > 0.00):
                verified = True
            else:
                print_vmsg(ver_name, gift, "Value must be > 0.00")
        else:
            print_vmsg(ver_name, gift, "Value must be numeric")
    else:
        print_vmsg(ver_name, gift, "Invalid value")
    return verified


# -- Multi-line information display ------------------------------------------


def show_donor_report(donors):
    """
    Display the donor statistics report.
    """
    report = make_donors_report(donors)
    print("\n{}".format(report))


def show_donor_names(sorted_names):
    """
    Display donor name with selection ID.
    """
    sn_count = len(sorted_names)
    s = ""
    if (sn_count > 0):
        n = 0
        s = "{:>3} {}".format((n + 1), sorted_names[n])
        for n in range(1, sn_count):
            s = "{}\n{:>3} {}".format(s, (n + 1), sorted_names[n])
    s = "{}\n\nDonor count = {}".format(s, sn_count)
    print("\n{}".format(s))


def show_donor(donor):
    """
    Display donor stats and individual gifts.
    """
    fmt = ("\n{}\n{}\n  {:<15}$  {:>10.2f}\n  {:<15}  {:>11d}\n  {:<15}"
           "$  {:>10.2f}\n{}")
    s = fmt.format(donor_name(donor),
                   "{}".format("-" * 32),
                   "Total Given",
                   donor_total_gift(donor),
                   "Num Gifts",
                   donor_gift_count(donor),
                   "Average Gift",
                   donor_average_gift(donor),
                   "{}".format("-" * 32)
                   )
    s = "{}\n{:<17}$".format(s, "  Gifts")
    gifts = donor_gifts(donor)
    if (len(gifts) > 0):
        s = "{}{:>12.2f}".format(s, gifts[0])
        for gift in gifts[1:]:
            s = "{}\n{:>30.2f}".format(s, gift)
    s = "{}\n".format(s)
    print(s)


# -- User interfaces ---------------------------------------------------------


def open_messenger_ui(donor):
    """
    Prior to transmittal, display a thank-you message to the donor for
    the last gift they made or to encourage them to donate if they
    haven't yet made a gift but are on the list. The reasoning behind
    this is that in theory the charity already sent thank-yous for
    previous gifts.

    Actions:  :S ::= Send message (email) to donor and exit from UI
              :X ::= Exit from UI

    Satisfies: requirement 1
    """
    ui_title = "MAILROOM: DONOR: MESSENGER"
    if (donor is None):
        print("\nopen_message_ui called with null donor\n")
    else:
        choice = _CMD_NONE
        msg = generate_message(donor)
        prompt = make_menu_prompt(
                    "Enter [:S]end e-mail or e[:X]it")
        # Satisfies: requirement 2.2
        while (choice != _CMD_EXIT):
            print_ui_header(ui_title)
            # Satisfies: requirement 1.2.3
            print(msg)
            print_ui_menu_break_line()
            choice = interpret_response(input(prompt), False)
            if (choice == _CMD_SEND):
                input("\nMessage sent to donor ([RETURN] to continue)")
                choice = _CMD_EXIT
    # Satisfies: requirement 1.2.3
    print("\nExiting {}\n".format(ui_title))


def open_donor_ui(donor):
    """
    Start the UI for viewing the donor's information, adding gift, and
    sending a thank-you note.

    Actions: numeric ::= Add another gift to the donor's gift list
             :S      ::= Show thank-you message UI for the donor
             :X      ::= Exit from UI
    """
    ui_title = "MAILROOM: DONOR"
    if (donor is None):
        print("\ndonor_ui called with null donor\n")
    else:
        dname = donor_name(donor)
        ui_title = "MAILROOM: DONOR ({})".format(dname)
        choice = _CMD_NONE
        # Satisfies: requirement 1.2
        prompt = \
            make_menu_prompt(
                ("Enter gift value ($), [:M]essenger to send thank you,"
                 " or e[:X]it")
                )
        # Satisfies: requirement 2.2
        while (choice != _CMD_EXIT):
            print_ui_header(ui_title)
            show_donor(donor)
            print_ui_menu_break_line()
            choice = interpret_response(input(prompt), False)
            msg = ""
            if (donor is None):
                continue
            else:
                if (choice == _CMD_MESSENGER):
                    # Satisfies: requirement 1.1
                    open_messenger_ui(donor)
                elif (choice == _CMD_EXIT):
                    continue
                else:
                    if (verify_gift(choice)):
                        # Satisfies: requirement 1.2.1
                        gift = round(float(choice), 2)
                        if (add_gift(donor, gift)):
                            # Satisfies: requirement 1.2.2
                            msg = "Added gift (${:.2f}) to donor ({})"\
                                    .format(gift, dname)
                            donor = get_donor(dname)
                        else:
                            msg = "Failed to add gift (${}) to donor ({})"\
                                    .format(gift, dname)
                        print("\n{}\n".format(msg))
    print("\nExiting {}\n".format(ui_title))


def add_new_donor_ui():
    """
    User prompt for adding a new donor to the donor aggregate. For a
    valid new donor name, adds and returns the donor. Entering nothing
    skips adding a new donor.

    Actions: text ::= Name for new donor

    Satisfies: requirement 1.1.2
    """
    prompt = \
        make_menu_prompt("Enter new donor name or blank to abort")
    donor = None
    choice = _CMD_NONE
    # Satisfies: requirement 2.2
    while (choice != _CMD_EXIT):
        print_ui_menu_break_line()
        choice = interpret_response(input(prompt), True)
        if (not choice):
            # Satisfies: requirement 2.2
            choice = _CMD_EXIT
        else:
            if (verify_new_donor(choice)):
                if (add_donor(choice)):
                    donor = get_donor(choice)
                    choice = _CMD_EXIT
                else:
                    print("\nFailed to add donor \"{}\"\n".format(choice))
    return donor


def open_mailroom_ui():
    """
    Start the mailroom user interface.

    Actions: :N   ::= Prompt for new donor name
             :L   ::= Show donor name list
             :R   ::= Show donor gift report
             :Q   ::= Quit application
             int  ::= Open Donor UI for donor specified by list ID
             text ::= Open Donor UI for donor specified by name
    """
    # Satisfies: The Program: Part 1 (2)
    print_app_title()
    ui_title = "MAILROOM"
    prompt_1 = make_menu_prompt(
                    ("Enter donor ID to access, [:N]ew donor, [:R]eport,"
                     " [:Q]uit")
                    )
    prompt_2 = make_menu_prompt(
                    ("Enter donor name to access, [:N]ew donor,"
                     " [:L]ist donors, [:Q]uit")
                    )
    prompt = prompt_1
    choice = _CMD_NONE
    # Satisfies: requirement 2.3
    while (choice != _CMD_QUIT):
        donor_names = sorted_donor_names(_Donors)
        print_ui_header(ui_title)
        if (choice == _CMD_REPORT):
            # Satisfies: requirement 2
            show_donor_report(_Donors)
            prompt = prompt_2
        else:
            # Satisfies: requirement 1.1.1
            show_donor_names(sorted_donor_names(_Donors))
            prompt = prompt_1
        print_ui_menu_break_line()
        choice = interpret_response(input(prompt), (prompt == prompt_2))
        if (is_cmd(choice)):
            if (choice == _CMD_NEW):
                # Satisfies; requirement 1.1.2
                donor = add_new_donor_ui()
            elif (choice == _CMD_LIST):
                # Satisfies: requirement 1.1.1
                continue
            elif (choice == _CMD_REPORT):
                # Satisfies: requirement 2.1, 2.1.3
                continue
            else:
                # Satisfies: requirement 2.2
                donor = None
        else:
            if (choice.isnumeric()):
                # Make donor selected by id the target
                id = int(choice)
                if (verify_existing_donor_id(donor_names, id)):
                    name = donor_names[id - 1]
                    donor = get_donor(name)
                    if (donor is None):
                        continue
                    else:
                        open_donor_ui(donor)
                else:
                    # Satisfies: requirement 2.2
                    donor = None
            elif (len(choice) > 0):
                # Satisfies: requirement 1.1.3
                if (verify_existing_donor_name(choice)):
                    donor = get_donor(choice)
                    open_donor_ui(donor)
                else:
                    # Satisfies: requirement 2.2
                    donor = None
            else:
                continue
    print("\nExiting {}\n".format(ui_title))


def run_mailroom():
    """
    Load charity mailroom data and run application.
    """
    load_donors()
    open_mailroom_ui()


if __name__ == '__main__':
    #
    # Satisfies: The Program: Part 1
    #
    run_mailroom()


# MAILROOM -> Display all donors, prompt for ID, :R, :N, :Q
#   :L ->   Display all donors -> replace :L with :R
#   :R ->   Display all-donor stat table -> replace :R with :L
#   :Q ->   Quit application
#   :N ->   Prompt for new donor name
#   ID =>   DONOR -> Display selected donor info, prompt for Gift, :M, :X
#             Gift -> Add gift to donor and update attributes
#             :M => MESSENGER -> Display thank-you message for last gift,
#                                prompt for :S, :X
#                     :S -> Send thank-you email => Return to DONOR
#                     :X -> Return to MAILROOM
#           :X => Return to MAILROOM
#   Name => DONOR
