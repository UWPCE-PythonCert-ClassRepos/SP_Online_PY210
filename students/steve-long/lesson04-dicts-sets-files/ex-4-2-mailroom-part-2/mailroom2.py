#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson04
# Mailroom Part 2 (mailroom2.py)
# Steve Long 2020-10-19 | v0
#
# Requirements:
# =============
#
#   [1]-Goal: Use dict where appropriate for functionality.
#   [2]-Convert main donor data structure to a dict.
#   [3]-Try to embed command operations into a dict.
#   [4]-Use a dict & .format to generate the donor thank-you message.
#   [5]-Add a function to generate a thank-you letter for all donors.
#       [5a]-Create a letter for each donor.
#       [5b]-Write each letter to disk as a text file.
#       [5c]-Each letter shall have a unique file name.
#       [5d]-Use flexible folder destination (not hard-coded).
#       [5e]-Optionally offer option to print to stdio or to file.
#
# Assumptions:
# ============
#
#   - A degree of design freedom is allowed for the solution.
#
# Implementation:
# ===============
#
#   There's a little extra polish on the UI and functionality, but the bulk
#   of this was implemented in the previous lesson.
#
#   [1]-App has multiple levels (UI) each with functionality (F):
#       - (UI) Main
#           - (F) :R Print donor report/ :L donor list
#           - (F) Select donor to display (by list ID or name)
#               - (UI) Donor
#                   - (F) :M Show donor thank-you message for latest gift
#                       - (UI) Donor messenger
#                           - (F) :S Send message to file
#                           - (F) :X Exit to donor UI
#                   - (F) Add another donor gift
#                   - (F) :X Exit to main UI
#           - (F) :N Add another donor
#               - (UI) New donor prompt
#                   - (F) Enter name for new donor
#                   - (F) Enter blank to return to main UI
#           - (F) :M Send messages to all donors (to file)
#           - (F) :Q Exit application
#
#   [2]-Main donor data structure is now a dict of donor tuples keyed on
#       the lowercase value of the donor's name. Donor names must be unique.
#
#   [3]-Operations are keyed on prompted user responses at each UI level. This
#       works by passing a generalized state representation of the data to
#       each routine, regardless of whether the state info is required. This
#       is a limitation of using a dict to act like a method dispatch table.
#
#   [4]-Dict is used to retrieve donors by name, .format used to populate
#       form letter based on donor attributes.
#
#   [5]-Function added to send messages to all donors:
#       [5a]-Letter addressed to donor by name and modified based on amount of
#            last gift.
#       [5b]-Letter written to file in folder named for donor. Folder is in
#            root folder in application folder.
#       [5c]-File name based on donor name, timestamp, and three-digit version
#            index (usually "000") - making file name unique.
#       [5d]-Destination in common root folder but separate folder for each
#            donor.
#       [5e]-Prints to both stdio and to file.
#
# Script Usage:
# =============
#
#   ./mailroom2.py
#
# Issues:
# =======
#
#   Requirements are a little vague, especially part about using a dict to
#   generate a form letter.
#
# History:
# ========
#
# 001/2020-10-25/sal/
#   Created mailroom v2 (mailroom2.py). Removed requirements notes for
#   previous version.
# 000/2020-10-20/sal/
#   Created mailroom v1 (mailroom.py).
#
# =============================================================================

from functools import reduce
from datetime import datetime
import pathlib

# -- Application constants ---------------------------------------------------


_BUSINESS_NAME = "ACME Charities"
_APP_TITLE = "Mailroom"
_APP_VERSION = "2.0"
_APP_WIDTH = 100


# -- Root data container -----------------------------------------------------


_Donors = {}


# -- Str utils ---------------------------------------------------------------


def clean_name(name):
    """
    Remove extraneous white space.
    HIST: 001/Incorporated Natasha's brevity suggestion.
          000/New
    """
    return " ".join(name.split())


def check_name_case(name, override_correction=True):
    """
    Clean and capitalize a name. If adjusted name is different from
    input, optionally allow the user choose preferred spelling. This
    will account for mixed-case names (Irish, Scot, Klingon, whatever.)

    HIST: 001/Fixed return value for override_correction=False.
          000/New
    """
    revised_name = " ".join(map(lambda nc: nc.capitalize(), name.split()))
    if (override_correction):
        if (name != revised_name):
            answer\
                = input("Use \"{}\" [Y] or original spelling [N]?: "
                        .format(revised_name))
            if (answer[0:1].upper() == "Y"):
                name = revised_name
            else:
                print("Reverting to original spelling")
    else:
        name = revised_name
    return name


def is_floatable(v):
    """
    Can a value be coerced to a floating-point value? Implemented
    because just checking for <v>.isnumeric() won't work with a value
    containing a decimal.

    HIST: 001/Incorporated Natasha's brevity suggestion.
          000/New
    """
    try:
        float(v)
    except Exception:
        return False
    else:
        return True


def is_intable(v):
    """
    Can a value be coerced to an int value? Implemented to maintain
    similarity with is_floatable for interpreting int values.
    NOTE: I will come up with a better name for this series of
          functions later because this looks too much like a predicate
          testing for something 'in a table.'

    HIST: 001/Incorporated Natasha's brevity suggestion.
          000/New
    """
    try:
        int(v)
    except Exception:
        return False
    else:
        return True


def get_time_stamp():
    """
    Convert this moment into a YYYY-mm-dd-HH-MM-SS string.

    HIST: 001/New
    """
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


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

    HIST: 000/New
    """
    return donor[0]


def donor_total_gift(donor):
    """
    The donor's total gift value (float). Must be recalculated whenever
    a gift is added (or removed.)

    HIST: 000/New
    """
    return round(donor[2], 2)


def donor_average_gift(donor):
    """
    The donor's average gift value (float). Must be recalculated
    whenever a gift is added (or removed.)

    HIST: 000/New
    """
    return round(donor[3], 2)

# -- Donor modifiable cached attributes --------------------------------------


def donor_gifts(donor):
    """
    The donor's gift data (tuple of 0 or more floats). Initialized by
    input.

    HIST: 000/New
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

    HIST: 000/New
    """
    return len(donor_gifts(donor))


def donor_last_gift(donor):
    """
    Last gift of the donor's gift list.

    HIST: 000/New
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

    HIST: 000/New
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
    key = donor_name(revised_donor).lower()
    _Donors[key] = revised_donor
    return revised_donor

# -- Donor data load ----------------------------------------------------------


def initial_donors():
    """
    Retrieve the basic information about donors and their gifts.
    Returns a sequence of the form (<donor>*) where <donor> has the
    form (<name>, (<gift>*)). Names borrowed from Lectroid list. Gift
    values are random.

    HIST: 000/New
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

    HIST: 000/New
    """
    global _Donors
    _Donors = {}
    for donor in initial_donors():
        donor = apply_donor_rules(donor)
        name = (donor_name(donor)).lower()
        if (name not in _Donors):
            _Donors[name] = donor
    return len(_Donors)

# -- Donor add/delete/edit ---------------------------------------------------


def get_donor(name):
    """
    Retrieve a donor by name. Returns donor tuple or None.

    HIST: 000/New
    """
    global _Donors
    donor = None
    key = name.lower()
    if (key in _Donors):
        donor = _Donors[key]
    return donor


def add_donor(name):
    """
    Add a new donor to the donor aggregate. Returns True if successful,
    False otherwise.

    HIST: 001/Change keys retrieval.
          000/New
    """
    global _Donors
    result = False
    key = name.lower()
    if (key not in _Donors.keys()):
        _Donors[key] = (name, (), 0.00, 0.00)
        result = True
    return result


def add_donor_gift(donor_in, gift):
    """
    Add a gift to the donor. Returns True if successful, False
    otherwise.

    HIST: 001/Incorporated Natasha's brevity suggesion.
          000/New
    """
    try:
        gifts = list(donor_gifts(donor_in))
        gifts.append(gift)
        donor = (donor_name(donor_in), gifts)
        apply_donor_rules(donor)
    except Exception:
        return False
    else:
        return True


# -- Report generation -------------------------------------------------------


def donor_data_width(v):
    """
    Calculate the required monospaced char count for a data value.
    Returns int value.

    HIST: 000/New
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


def report_col_names():
    """
    Names of columns for a donor gift report. Returns tuple of
    displayable column names. Implemented to provide flexibility for
    altering the set of donor attributes to be displayed.

    HIST: 000/New
    """
    return ("Donor Name", "Total Given", "Num Gifts", "Average Gift")


def report_column_widths(reported_donors):
    """
    Determine required column width for each reported donor's report
    attribute. Returns tuple of ints.

    HIST: 000/New
    """
    col_names = report_col_names()
    name_col_width = len(col_names[0])
    total_gift_col_width = len(col_names[1])
    gift_count_col_width = len(col_names[2])
    average_gift_col_width = len(col_names[3])
    for donor in reported_donors:
        name_col_width \
            = max(name_col_width,
                  donor_data_width(donor_name(donor)))
        total_gift_col_width \
            = max(total_gift_col_width,
                  donor_data_width(donor_total_gift(donor)))
        gift_count_col_width \
            = max(gift_count_col_width,
                  donor_data_width(donor_gift_count(donor)))
        average_gift_col_width \
            = max(average_gift_col_width,
                  donor_data_width(donor_average_gift(donor)))
    widths = [name_col_width,
              total_gift_col_width,
              gift_count_col_width,
              average_gift_col_width
              ]
    widths = tuple(widths)
    return widths


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

    HIST: 001/Revised (col_val) to truncate col_value that exceeds
              col_width (no current use-case, but possibly useful
              later.)
          000/New
    """
    just = (">" if (justification.upper() == "R") else "<")
    col_width = col_width - len(prefix)
    col_val = col_value[0:min(col_width, len(col_value))]
    s = ("{}{}{}:{}{}{}"
         .format(prefix, "{", "a", just, col_width, "}")).format(a=col_val)
    return s


def format_money(value, width):
    """
    Render a fixed-width str value for a monetary floating point value.
    Returns str value.

    HIST: 000/New
    """
    return justify("{:.2f}".format(round(value, 2)), width, "R", "$")


def format_int(value, width):
    """
    Render a fixed-width cell value for an integer value. Returns
    str value.

    HIST: 000/New
    """
    return justify("{:d}".format(value), width, "R", "")


def format_str(value, width):
    """
    Render a fixed-width cell value a string value. Returns a str.

    HIST: 000/New
    """
    return justify(value, width, "L", "")


def report_row_separator(sep_char, col_widths):
    """
    Render a row separator to span the full width of a set of columns.
    Returns str value.

    HIST: 000/New
    """
    row_width = \
        reduce(lambda sum, w: sum + w, col_widths, 0)\
        + ((len(col_widths) - 1) * 3)
    return sep_char * row_width


def report_header(col_names, col_widths):
    """
    Render a donor report header (title and column rows.) Returns str
    value.

    HIST: 000/New
    """
    s = "\nDonor Report"
    s = "{}\n{}".format(s, report_row_separator("=", col_widths))
    s = "{}\n{}".format(s, format_str(col_names[0], col_widths[0]))
    for n in range(1, len(col_names)):
        s = "{} | {}".format(s, format_str(col_names[n], col_widths[n]))
    s = "{}\n{}".format(s, report_row_separator("-", col_widths))
    return s


def report_row(donor, accessors, col_widths, col_fmts):
    """
    report_row(<donor>, <accessors>, <col_widths>, <col_fmts>)
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

    HIST: 000/New
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

    HIST: 000/New
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


def make_donors_report():
    """
    make_donors_report()
    ----------------------------
    Generate a donor report string.

    Entry: (for simplification, <donors> no longer an arg)
    Exit:  Returns a string that looks like a table showing donor name
           and total value, number of, and average value of gifts.

    HIST: 000/New
    """
    donors = _Donors
    attr_accessors = \
        (donor_name, donor_total_gift, donor_gift_count, donor_average_gift)
    col_names = report_col_names()
    col_fmts = tuple([format_str, format_money, format_int, format_money])
    reported_donors = tuple(
                        sorted(
                            list(donors.values()),
                            key=donor_total_gift,
                            reverse=True
                            )
                        )
    col_widths = report_column_widths(reported_donors)
    separator = report_row_separator("-", col_widths)
    displayable = report_header(col_names, col_widths)
    for donor in reported_donors:
        row = report_row(donor, attr_accessors, col_widths, col_fmts)
        displayable = "{}\n{}".format(displayable, row)
    displayable\
        = "{}\n{}\n{}\n{}"\
          .format(
            displayable,
            separator,
            make_donors_net_values_report(donors),
            separator
            )
    return displayable


# -- Message file management -------------------------------------------------


def create_folder(folder_path):
    """
    Create an actual folder at the specified path if it does not already exist
    and return True if successful, otherwise return False.

    HIST: 001/New
    """
    success = True
    try:
        if (folder_path.exists()):
            if (not folder_path.is_dir()):
                folder_path.unlink()
                folder_path.mkdir()
        else:
            folder_path.mkdir()
    except Exception as ex:
        repr(ex)
        success = False
    return success


def make_donor_basename(name):
    """
    Generate a name for the donor message folder or prefix for the donor
    message documents. Returns a string composed of the donor's name.

    HIST: 001/New
    """
    names = name.lower().split(" ")
    names_out = []
    if (len(names) > 1):
        names = [names[-1]] + names[0:-1]
    for name_out in names:
        if (len(name_out) > 0):
            names_out.append("".join([c for c in name_out if c.isalnum()]))
    return "-".join(names_out)


def root_folder_path():
    """
    Create the root folder for all donor messages. Returns the
    root folder path.
    REVISED: working_directory_path will now be in the app folder for
    simplicity rather than asking the user to worry about this.

    HIST: 001/New
    """
    working_directory_path = pathlib.Path.cwd()
    target_foldername = "donor-messages"
    folder_path = working_directory_path.joinpath(target_foldername)
    if (not create_folder(folder_path)):
        folder_path = None
    return folder_path


def donor_folder_path(root_folder_path, donor_name):
    """
    Create a folder for donor messages. Returns the folder path.

    HIST: 001/New
    """
    folder_name = make_donor_basename(donor_name)
    folder_path = root_folder_path.joinpath(folder_name)
    if (not create_folder(folder_path)):
        folder_path = None
    return folder_path


def donor_document_path(folder_path, donor_name, t_stamp):
    """
    Create a document for the donor message text. Returns a the document path.

    HIST: 001/New
    """
    MAX_ATTEMPT_COUNT = 301
    success = False
    doc_name_root = "{}-{}".format(make_donor_basename(donor_name), t_stamp)
    doc_name = "{}-000.txt".format(doc_name_root)
    doc_path = folder_path.joinpath(doc_name)
    if (doc_path.exists()):
        for i in range(1, MAX_ATTEMPT_COUNT):
            suffix = "{:0>3}".format(i)
            doc_name = "{}-{}.txt".format(doc_name_root, suffix)
            doc_path = folder_path.joinpath(doc_name)
            if (not doc_path.exists()):
                success = True
                break
    else:
        success = True
    return (doc_path if success else None)


# -- UI utilities ------------------------------------------------------------


def make_state(name=None, id=None, gift=None, message=None):
    """
    Aggregate state data in the form of a dict for UI.

    HIST: 001/New
    """
    state = {
        "name": name,
        "id": id,
        "gift": gift,
        "message": message,
        "time_stamp": get_time_stamp()
    }
    return state


def do_cmd(fmap, cmd, state):
    """
    Retrieve the function in <fmap> mapped to <cmd>. Execute the
    function, applying <args> as arguments, if any, returning the result.

    HIST: 001/New
    """
    result = None
    if (cmd in fmap):
        f = fmap[cmd]
        result = f(state)
    return result


def make_menu_prompt(menu_directions):
    """
    Render a command-line user prompt consisting of a UI name and key
    input options.

    HIST: 001/Incorporated Natasha's brevity suggestion.
          000/New
    """
    return "INPUT: {} > ".format(menu_directions)


def sorted_donor_names():
    """
    Retrieve the sorted names of a dictionary donors. Argument used to
    provide flexibility for allowing a subset of donors (instead of
    _Donors). Returns a list of donor tuples.

    HIST: 000/New
          001/Arg list removed.
    """
    names = map(lambda donor: donor_name(donor), _Donors.values())
    return list(sorted(names))


def generate_message(donor):
    """
    Generate thank-you message for donor's last gift.

    HIST: 000/New
          001/More use of format, less string construction.
    """
    dname = donor_name(donor)
    last_gift = donor_last_gift(donor)
    body = (("Please consider making a gift to our organization."
             " It's tax deductible.")
            if (last_gift is None)
            else "Thanks for your recent gift of ${:.2f}.".format(last_gift))
    message = "Dear {}\n\n{}\n\nRegards,\n\nACME Charities".format(dname, body)
    return message


# -- User-input translation --------------------------------------------------


def is_cmd(choice):
    """
    Does a command-line entry have the format of an application
    command? Returns bool value.

    HIST: 000/New
    """
    status = False
    if (type(choice) is str):
        status = (choice[0:1] == ":")
    return status


def interpret_response(response_in, override_correction):
    """
    Interpret user input from keyboard. Parameter override_correction
    allows suppression of automatic capitalization correction of
    proper name.

    HIST: 000/New
          001/Simplified as side-effect of using command function map.
    """
    response_out = None
    response_in = clean_name(response_in.strip())
    if (is_cmd(response_in)):
        response_out = response_in[0:2].upper()
    elif (is_floatable(response_in)):
        #
        # <response> is probably a gift.
        #
        response_out = response_in
    elif (is_intable(response_in)):
        #
        # <response> is probably a choice index.
        #
        response_out = response_in
    else:
        #
        # <response> is probably a donor name but could be nonsense.
        #
        response_out = check_name_case(response_in, override_correction)
    return response_out


def send_message_to_donor(state):
    """
    Write message to donor by writing to file.

    HIST: 001/New
    """
    success = False
    dname = state["name"]
    root_path = root_folder_path()
    if (root_path is None):
        print("Error: Can't access donor message root path")
    else:
        folder_path = donor_folder_path(root_path, dname)
        if (folder_path is None):
            print(("Error: Can't access path to "
                   "message folder for {}").format(dname))
        else:
            t_stamp = state["time_stamp"]
            doc_path = donor_document_path(folder_path, dname, t_stamp)
            if (doc_path is None):
                print(("Error: Can't create new "
                       "message document for {}").format(dname))
            else:
                with open(doc_path, 'w') as file:
                    file.write(state["message"])
                    success = True
    return success


def send_message(dname, message, t_stamp):
    """
    Write message to donor by writing to file.

    HIST: 001/New
    """
    success = False
    root_path = root_folder_path()
    if (root_path is None):
        print("Error: Can't access donor message root path")
    else:
        folder_path = donor_folder_path(root_path, dname)
        if (folder_path is None):
            print(("Error: Can't access path to "
                   "message folder for {}").format(dname))
        else:
            doc_path = donor_document_path(folder_path, dname, t_stamp)
            if (doc_path is None):
                print(("Error: Can't create new "
                       "message document for {}").format(dname))
            else:
                with open(doc_path, 'w') as file:
                    file.write(message)
                    success = True
    return success


def send_messages_to_donors(state):
    """
    Write messages to all donors.

    HIST: 001/New
    """
    completed = 0
    total = 0
    success = True
    for donor in _Donors.values():
        message = generate_message(donor)
        state["name"] = donor_name(donor)
        state["message"] = message
        total += 1
        if (send_message_to_donor(state)):
            completed += 1
        else:
            success = False
    if (success):
        print(("\nThank-you messages transmitted to all donors for their"
               " latest donation or to bug them to donate in the future"))
    else:
        success_factor = (100.0 * completed)/total
        print(("{:.2f}% of the donor thank-you "
               "messages were transmitted").format(success_factor))
    state = make_state()
    return success


# -- One-line layout and information printing --------------------------------


def print_app_title():
    """
    Print command-line application banner for startup.

    HIST: 000/New
    """
    ui_title = "{} v{}".format(_APP_TITLE, _APP_VERSION)
    print("\n\n{}\n{}".format(_BUSINESS_NAME, ui_title))


def print_ui_header(ui_title):
    """
    Display UI header bar for screen.

    HIST: 000/New
    """
    fmt = "\n\n{}:=<{}{}".format("{", _APP_WIDTH, "}")
    print(fmt.format("== {} ".format(ui_title)))


def print_ui_menu_break_line():
    """
    Print a line of chars a command-line screen visual break.

    HIST: 000/New
    """
    print("\n{}".format("-" * _APP_WIDTH))


def print_vmsg(ver_name, data, msg):
    """
    Print an input data verification failure message of the form
    'ERROR: Rule: <ver_name> (<data>) <msg>'.

    HIST: 000/New
    """
    print("\nERROR: Rule: {} ({}): {}\n".format(ver_name, data, msg))


# -- Data verification rules ------------------------------------------------


def verify_existing_donor_name(name):
    """
    Verify that a donor <name> exists. If verification fails, print
    message. Returns True if <name> is verified.

    Rule: The name shall exist in donor aggregate. Context:
          Retrieving a donor by name.

    HIST: 000/New
    """
    global _Donors
    ver_name = "existing-donor-name"
    verified = False
    key = name.lower()
    if (key in _Donors):
        verified = True
    else:
        print_vmsg(ver_name, name, "Donor does not exist")
    return verified


def verify_existing_donor_id(id):
    """
    Verify that a donor <id> exists in a donor display sequence. If
    verification fails, print message. Returns True if <id> is
    verified.

    Rule: The ID of a donor shall be 1 greater than an index in a donor
          display sequence. Context: Retrieving a donor from an
          enumerated display list.

    HIST: 000/New
    """
    ver_name = "existing-donor-id"
    verified = False
    donor_count = len(_Donors)
    if ((id > 0) and (id <= donor_count)):
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

    HIST: 001/Revised rules for new donor:
              * Must be at least TWO chars in length ("QB", not just "Q")
              * Must contain at least ONE letter ("B4", not just "4")
              * May optionally include numbers ("2Pac Shakur")
              * May optionally include symbols "'", "-", and space
                ("B'Elanna", "Dever-Conner", not "$include")
          000/New
    """
    global _Donors
    ver_name = "new-donor-name"
    verified = False
    msg = None
    if (len(name) < 2):
        msg = "Donor name must be 2 or more chars"
    elif (name.isnumeric()):
        msg = "Donor name cannot be purely numeric"
    else:
        msg = "Donor name must contain at least one letter"
        for c in name:
            if (not c.isalnum()):
                if (c not in (" '-")):
                    msg =\
                        ("Donor name may contain only letters, numbers, \"'\","
                         " and \"-\"")
                    break
            elif (c.isalpha()):
                msg = None
            else:
                next
    if (msg is None):
        key = name.lower()
        if (key not in _Donors):
            verified = True
        else:
            print_vmsg(ver_name, name, "Donor already exists")
    else:
        print_vmsg(ver_name, name, msg)
    return verified


def verify_gift(gift):
    """
    Verify that a gift value is acceptable. If verification fails,
    print message. Returns True if <gift> is verified.

    Rule: Gift value ($) must be a numeric value > 0. Context:
          Entering a gift value.

    HIST: 000/New
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


def print_donors_report(_state):
    """
    Display the donor statistics report. NOTE: Param prefixed with "_" means
    ignore the arg.

    HIST: 001/Donors no longer an arg.
          000/New
    """
    print("\n{}".format(make_donors_report()))


def print_donor_names(_state):
    """
    Display donor name with selection ID.

    HIST: 000/New
          001/sorted_names no longer an arg.
    """
    sorted_names = sorted_donor_names()
    sn_count = len(sorted_names)
    s = ""
    if (sn_count > 0):
        n = 0
        s = "{:>3} {}".format((n + 1), sorted_names[n])
        for n in range(1, sn_count):
            s = "{}\n{:>3} {}".format(s, (n + 1), sorted_names[n])
    s = "{}\n\nDonor count = {}".format(s, sn_count)
    print("\n{}".format(s))


def print_donor(donor):
    """
    Display donor stats and individual gifts.

    HIST: 001/New
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


def fmap_messenger_ui():
    """
    Maps commands (cmd) to functions for messenger_ui.

    HIST: 001/New
    """
    fmap = dict()
    fmap[":S"] = send_message_to_donor
    return fmap


def show_messenger_ui(state):
    """
    Prior to transmittal, display a thank-you message to the donor for
    the last gift they made or to encourage them to donate if they
    haven't yet made a gift but are on the list. The reasoning behind
    this is that in theory the charity already sent thank-yous for
    previous gifts.

    Actions:  :S ::= Send message (email) to donor and exit from UI
              :X ::= Exit from UI

    HIST: 001/New
    """
    ui_title = "MAILROOM: DONOR: MESSENGER"
    donor = get_donor(state["name"])
    if (donor is None):
        print("\nopen_message_ui called with null donor\n")
    else:
        fmap = fmap_messenger_ui()
        valid_cmds = (":S", ":X")
        dname = donor_name(donor)
        ui_title = "MAILROOM: DONOR ({}): MESSENGER".format(dname)
        dmsg = generate_message(donor)
        fmt = "\nTransmitting the following message to donor {}:\n\n{}\n"
        msg = fmt.format(donor_name(donor), dmsg)
        prompt = make_menu_prompt("Enter [:S]end e-mail or e[:X]it")
        cmd = ""
        while (cmd != ":X"):
            print_ui_header(ui_title)
            print(msg)
            print_ui_menu_break_line()
            response = interpret_response(input(prompt), False)
            if (response in valid_cmds):
                cmd = response
                state["time_stamp"] = get_time_stamp()
                state["message"] = dmsg
                do_cmd(fmap, cmd, state)
                print("\nMessage sent.")
                cmd = ":X"
    print("\nExiting {}".format(ui_title))


def get_donor_by_id(id):
    """
    Retrieve donor by sort order ID.

    HIST: 001/New
    """
    id = int(id)
    donor = None
    if (verify_existing_donor_id(id)):
        donor_names = sorted_donor_names()
        name = donor_names[id - 1]
        donor = get_donor(name)
    return donor


def get_donor_by_name(name):
    """
    Retrieve donor by name.

    HIST: 001/New
    """
    if (verify_existing_donor_name(name)):
        return get_donor(name)
    else:
        return None


def add_gift(state):
    """
    Append a gift to the donor's list.

    HIST: 000/New
          001/Revised parameters.
    """
    gift = state["gift"]
    if (verify_gift(gift)):
        gift = round(float(gift), 2)
        dname = state["name"]
        donor = get_donor(dname)
        if (add_donor_gift(donor, gift)):
            msg = "Added gift (${:.2f}) to donor ({})".format(gift, dname)
        else:
            msg = "Failed to add gift (${}) to donor ({})".format(gift, dname)
        print("\n{}\n".format(msg))


def fmap_donor_ui():
    """
    Maps commands (cmd) to functions for donor_ui.

    HIST: 001/New
    """
    fmap = dict()
    fmap[":M"] = show_messenger_ui
    fmap[":G"] = add_gift
    return fmap


def show_donor_ui(state):
    """
    Start the UI for viewing the donor's information, adding gift, and
    sending a thank-you note.

    Actions: numeric ::= Add another gift to the donor's gift list
             :M     ::= Show thank-you message UI for the donor
             :X      ::= Exit from UI

    HIST: 000/New
          001/Revised to use command function map.
    """
    ui_title = "MAILROOM: DONOR"
    donor = None
    name_or_id = state["name"]
    if (name_or_id.isnumeric()):
        donor = get_donor_by_id(name_or_id)
    else:
        donor = get_donor_by_name(name_or_id)
    if (donor is None):
        print("\nNo donor name or id \"{}\"".format(name_or_id))
    else:
        fmap = fmap_donor_ui()
        valid_cmds = (":M", ":X")
        dname = donor_name(donor)
        ui_title = "MAILROOM: DONOR ({})".format(dname)
        cmd = ""
        prompt = \
            make_menu_prompt(
                ("Enter gift value ($), [:M]essenger to send thank you,"
                 " or e[:X]it")
                )
        while (cmd != ":X"):
            print_ui_header(ui_title)
            print_donor(donor)
            print_ui_menu_break_line()
            response = interpret_response(input(prompt), False)
            state["name"] = dname
            if (response in valid_cmds):
                cmd = response
                do_cmd(fmap, cmd, state)
            else:
                if (is_floatable(response) or is_intable(response)):
                    cmd = ":G"
                    state["gift"] = response
                    do_cmd(fmap, cmd, state)
            donor = get_donor(dname)
    print("\nExiting {}".format(ui_title))


def add_new_donor(state):
    """
    Add a new donor (with messaging).

    HIST: 001/New
    """
    name = state["name"]
    if (verify_new_donor(name)):
        if (add_donor(name)):
            print("\nAdded donor \"{}\"\n".format(name))
        else:
            print("\nFailed to add donor \"{}\"\n".format(name))


def fmap_new_donor_ui():
    """
    Maps commands (cmd) to functions for add_new_donor_ui.

    HIST: 001/New
    """
    fmap = dict()
    fmap[":N"] = add_new_donor
    return fmap


def show_new_donor_ui(state):
    """
    User prompt for adding a new donor to the donor aggregate. For a
    valid new donor name, adds and returns the donor. Entering nothing
    skips adding a new donor.

    Actions: text ::= Name for new donor

    HIST: 001/Revised to use command function map.
          000/New
    """
    fmap = fmap_new_donor_ui()
    prompt = \
        make_menu_prompt("Enter new donor name or blank to abort")
    cmd = ""
    while (cmd != ":X"):
        print_ui_menu_break_line()
        response = interpret_response(input(prompt), True)
        if (not response):
            cmd = ":X"
        else:
            state["name"] = response
            cmd = ":N"
            do_cmd(fmap, cmd, state)
            cmd = ":X"
        state = make_state()


def fmap_mailroom_ui():
    """
    Maps commands (cmd) to functions for mailroom_ui.

    HIST: 001/New
    """
    fmap = dict()
    fmap[":L"] = print_donor_names
    fmap[":M"] = send_messages_to_donors
    fmap[":N"] = show_new_donor_ui
    fmap[":O"] = show_donor_ui
    fmap[":R"] = print_donors_report
    return fmap


def show_mailroom_ui():
    """
    Start the mailroom user interface.

    Actions: :L   ::= Show donor name list
             :M   ::= Send thank-you messages for all donor's latest gifts.
             :N   ::= Prompt for new donor name
             :Q   ::= Quit application
             :R   ::= Show donor gift report
             int  ::= Open Donor UI for donor specified by list ID
             text ::= Open Donor UI for donor specified by name

    HIST: 000/New
          001/Revised to use command function map.
    """
    fmap = fmap_mailroom_ui()
    valid_cmds = (":L", ":M", ":N", ":R", ":Q")  # Valid USER commands
    print_app_title()
    ui_title = "MAILROOM"
    prompt_1 = make_menu_prompt(
                    ("Enter donor ID to access, [:N]ew donor, [:R]eport,"
                     " [:M]essage all donors, [:Q]uit")
                    )
    prompt_2 = make_menu_prompt(
                    ("Enter donor name to access, [:N]ew donor,"
                     " [:L]ist donors, [:M]essage all donors, [:Q]uit")
                    )
    prompt = prompt_1
    cmd = ":L"
    state = make_state()
    while (cmd != ":Q"):
        if (cmd == ":R"):
            print_ui_header(ui_title)
            do_cmd(fmap, cmd, state)
            prompt = prompt_2
        elif (cmd == ":L"):
            print_ui_header(ui_title)
            do_cmd(fmap, cmd, state)
            prompt = prompt_1
        else:
            do_cmd(fmap, cmd, state)
            print_ui_header(ui_title)
            cmd = ":L"
            do_cmd(fmap, cmd, state)
        state = make_state()
        print_ui_menu_break_line()
        response = interpret_response(input(prompt), False)
        if (response in valid_cmds):
            cmd = response
        elif (is_cmd(response)):
            # User entered invalid command, so go back to just re-listing.
            cmd = ":L"
        else:
            # Not a command; probably a donor ID (or even name)
            cmd = ":O"  # :O Valid command callable by routine, not user
            state["name"] = response
    print("\nExiting {}".format(ui_title))


def run_mailroom():
    """
    Load charity mailroom data and run application.

    HIST: 000/New
          001/Added call to root_folder_path.
    """
    load_donors()
    root_folder_path()
    show_mailroom_ui()


if __name__ == '__main__':
    run_mailroom()


# MAILROOM -> Display all donors, prompt for ID, :R, :N, :Q
#   :L ->   Display all donors -> replace :L with :R
#   :M ->   Send thank-you messages to all donors
#   :N ->   Prompt for new donor name
#   :Q ->   Quit application
#   :R ->   Display all-donor stat table -> replace :R with :L
#   ID =>   DONOR -> Display selected donor info, prompt for Gift, :M, :X
#             Gift -> Add gift to donor and update attributes
#             :M => MESSENGER -> Display thank-you message for last gift,
#                                prompt for :S, :X
#                     :S -> Send thank-you email => Return to DONOR
#                     :X -> Return to MAILROOM
#           :X => Return to MAILROOM
#   Name => DONOR
