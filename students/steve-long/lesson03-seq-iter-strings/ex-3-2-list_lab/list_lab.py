#!/usr/bin/env python3
# ==============================================================================
# Python210 | Fall 2020
# ------------------------------------------------------------------------------
# Lesson03
# List Lab (list_lab.py)
# Steve Long 2020-09-27 | v0
#
# Requirements:
# =============
#
# In your student dir in the class repo, create a lesson03 dir and put in a new
# list_lab.py file. The file should be an executable Python script. That is to
# say that one should be able to run the script directly like so:
#
#   $ ./list_lab.py
#
# (At least on OS-X and Linux).
# – you do that with this command:
#
#   $ chmod +x list_lab.py
#
# (The +x means make this executable).
# The file will also need this on the first line:
#
#   #!/usr/bin/env python3
#
# This is known as the "she-bang" line – it tells the shell how to execute that
# file – in this case, with python3
#
# NOTE: on Windows, there is a python launcher which, if everything is
# configured correctly will look at that line to know you want python3 if there
# is more than one python on your system.
#
# If this doesn’t work on Windows, just run the file some other way:
#
#   $ python list_lab.py; OR
#   with run in ipython; OR
#   from your IDE or editor is you are using one
#
# Add the file to your clone of the repository and commit changes frequently
# while working on the following tasks. When you are done, push your changes to
# GitHub and issue a pull request.
#
# (if you are s"ll struggling with git – just write the code for now).
#
# When the script is run, it should accomplish the following four series of
# actions:
#
# Series 1
# --------
#   [1] Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
#   [2] Display the list (plain old print() is fine...).
#   [3] Ask the user for another fruit and add it to the end of the list.
#   [4] Display the list.
#   [5] Ask the user for a number and display the number back to the user and
#       the fruit corresponding to that number (on a 1-is-first basis).
#       Remember that Python uses zero-based indexing, so you will need to
#       correct.
#   [6] Add another fruit to the beginning of the list using "+" and display
#       the list.
#   [7] Add another fruit to the beginning of the list using insert() and
#       display the list.
#   [8] Display all the fruits that begin with "P", using a for loop.
#
# Series 2
# --------
#   Using the list created in series 1 above:
#   [1] Display the list.
#   [2] Remove the last fruit from the list.
#   [3] Display the list.
#   [4] Ask the user for a fruit to delete, find it and delete it.
#   [5] (Bonus: Multiply the list times two. Keep asking until a match is
#       found. Once found, delete all occurrences.)
#
# Series 3
# --------
#   Again, using the list from series 1:
#   [1] Ask the user for input displaying a line like "Do you like apples?" for
#       each fruit in the list (making the fruit all lowercase).
#   [2] For each "no", delete that fruit from the list.
#   [3] For any answer that is not "yes" or "no", prompt the user to answer
#       with one of those two values (a while loop is good here) Display the
#       list.
#
# Series 4
# --------
#   Once more, using the list from series 1:
#   [1] Make a new list with the contents of the original, but with all the
#       letters in each item reversed.
#   [2] Delete the last item of the original list. Display the original list
#       and the copy.
#
# # Implementation:
# ---------------
#
#   - Solutions presented in 4 steps, one for each series. Runs interactively
#     from command line.
#
#   - Function names, variables, block comments, line continuation, and
#     operator spacing per PEP8 guidelines. Checked with flake8.
#
# Script Usage:
# -------------
#
# 	./list_lab.py
#
# Issues:
# -------
#
#   -
#
# History:
# --------
# 000/2020-10-01/sal/Created.
# =============================================================================

# [1] Series 1
# ----------------------------------------------------------------------------
# Assumption: List development is sequential.
# Assumption: A degree of freedom is allowed for developing command-line UI.
# Assumption: Operations on common list may be destructive.


def validated_menu_choice(choice_in, option_count):
    """
    validated_menu_choice(<choice_in>, <option_count>)
    --------------------------------------------------
    For problem [1-5]. Validate the user menu choice, returning an
    actionable int value.

    Entry: <choice_in>    ::= (str) Menu option number.
           <option_count> ::= (int) Number of menu options.
    Exit:  Returns...
           * int equivalent for 1 <= <choice_in> <= <option_count>; OR
           * 0 if <choice_in> = 'X'; OR
           * -1 for anything else,
    """
    choice_out = (0 if (choice_in.upper() == "X") else -1)
    if (choice_in.isnumeric()):
        choice = int(float(choice_in))
        if ((choice > 0) and (choice <= option_count)):
            choice_out = choice
        else:
            choice_out = -1
    return choice_out


def make_option_menu(options):
    """
    make_option_menu(<options>)
    ---------------------------
    For problem [1-5]. Make an enumerated str of menu options.

    Entry: <options> ::= (list(str*)) menu options, count > 0.
    Exit:  Returns a displayable str of the menu options prefixed with
           a menu option number starting with 1.
    """
    option_menu = ""
    option_count = len(options)
    if (option_count > 0):
        option_menu = "[1] {}".format(options[0])
        for n in range(1, option_count):
            option_menu = \
                option_menu + ", [{}]: {}".format((n + 1), options[n])
    return option_menu


def choose_option_from_menu(option_menu, option_count):
    """
    choose_option_from_menu(<option_menu>, <option_count>)
    ------------------------------------------------------
    For problem [1-5]. Present and respond to user menu choice.

    Entry: <option_menu>  ::= (str) Displayable menu options prefixed
                              with a menu option number starting with 1.
           <option_count> ::= (int) Number of menu options.
    Exit:  Returns int representing user choice.
    """
    prompt = "\n{}\nSelect by item number or X to eXit: "
    choice = input(prompt.format(option_menu))
    return validated_menu_choice(choice, option_count)


def select_from_menu(options):
    """
    select_from_menu(<options>)
    ---------------------------
    For problem [1-5]. Prompt user for a menu choice.

    Entry: <options> ::= (list(str*)) menu options, count > 0.
    Exit:  4 possible outcomes based on user choice...

           (1) Print 'Nothing on the menu today' and exit; OR
           (2) Print 'Exiting from menu' and exit; OR
           (3) Print 'Invalid choice <choice>' and ask again; OR
           (4) Print 'Selection is <choice> (<selection>)' and ask
               again.

           where <choice> is the menu option selection and
           <selection> is the name of the selection.
    """
    selection = ""
    option_count = len(options)
    if (option_count > 0):
        option_menu = make_option_menu(options)
        choice = -1
        while (choice < 0):
            choice = choose_option_from_menu(option_menu, option_count)
            if (choice == 0):
                print("\nExiting from menu")
                break
            elif (choice > 0):
                selection = options[choice - 1]
                print("\nSelection is #{} (\"{}\")".format(choice, selection))
                choice = -1
            else:
                print("\nInvalid choice \"{}\"".format(choice))
    else:
        print("\nNothing on the menu today")


def string_equal(a, b, ignore_case):
    """
    string_equal(<a>, <b>, <ignore_case>)
    -------------------------------------
    For problem [1-8]. Are two strings equivalent?

    Entry: <a>, <b>      ::= (str) Values to compare.
           <ignore_case> ::= (Boolean) When True, ignore char case.
    Exit:  Returns True if <a> and <b> are equivalent.
    """
    result = (a == b)
    if (ignore_case):
        result = (a.lower() == b.lower())
    return result


def collectp_via_loop(element_list):
    """
    collectp_via_loop(<element_list>)
    ---------------------------------
    For problem [1-8]. Iterate on a list of str, collecting values
    beginning with the letter 'p'.

    Entry: <element_list> ::= (list(str*))
    Exit:  Returns a list containing elements of <element_list>
           starting with the letter 'p'.
    """
    pfiltered = []
    for e in element_list:
        if (string_equal(e[0:1], "p", True)):
            pfiltered.append(e)
    return pfiltered


def collectp_via_filter(element_list):
    """
    collectp_via_filter(<element_list>)
    -----------------------------------
    For problem [1-8]. Collect values of a list of str with the filter
    function checking for the first letter as 'p'.

    Entry: <element_list> ::= (list(str*))
    Exit:  Returns a list containing elements of <element_list>
           starting with the letter 'p'.
    """
    return list(filter(lambda e: string_equal(e[0:1],
                       "p", True),
                       element_list))


# ----------------------------------------------------------------------------
# _Fruits - common data between series 1 thru 4
# ----------------------------------------------------------------------------

_Fruits = []


def reset_fruits():
    """
    Reset the global container _Fruits.
    """
    global _Fruits
    _Fruits = ["Apples", "Pears", "Oranges", "Peaches"]


def member_of(list_to_search, element):
    """
    Is element and member of the list?
    """
    found = False
    try:
        found = (list_to_search.index(element) >= 0)
    except Exception:
        found = False
    return found


# [1] Series 1
# ----------------------------------------------------------------------------
# Assumption: List development is sequential.
# Assumption: A degree of freedom is allowed for developing command-line UI.
# Assumption: Operations on common list may be destructive.


def series_1():
    """
    series_1()
    ----------
    Satisfy Series-1 requirements 1 through 8.

    Entry: -
    Exit:  Multiple input and output events. Modifies content of global
           var _Fruits.
    """
    global _Fruits
    print("\nSeries-1 Solutions\n")
    print("{}".format("-" * 50))
    #
    # [1-1] ...creating the initial list.
    #
    reset_fruits()
    #
    # [1-2] ...printing the results of [1-1].
    #
    print("\nfruits are {}".format(_Fruits))
    #
    # [1-3] ...also added a new element check and some formatting on the
    #       input.
    #
    is_new_fruit = False
    while(not is_new_fruit):
        next_fruit = input("\n=>Enter a new fruit: ")
        is_new_fruit = (not member_of(_Fruits, next_fruit))
    next_fruit = next_fruit.replace("\"", "").strip().capitalize()
    _Fruits.append(next_fruit)
    #
    # [1-4] ...printing the results of [1-3].
    #
    print("\nfruits are {}".format(_Fruits))
    #
    # [1-5] ...a slightly more sophisticated fruit selector.
    #
    select_from_menu(_Fruits)
    #
    # [1-6] ...adding to the head of a list and printing the results.
    #
    print("\nInsert an item at the head of a list using '+' operator:")
    f = "Kiwi"
    more_fruits = [f] + _Fruits
    print(f"\n[{f}] + {_Fruits} = {more_fruits}")
    _Fruits = more_fruits
    #
    # [1-7] ...adding to the head of a list and printing the results (again).
    #
    print("\nInsert an item at the head of a list using the 'insert' method:")
    f = "Pomegranate"
    initial_fruits = _Fruits.copy()
    _Fruits.insert(0, f)
    print(f"\n{initial_fruits}.insert(0,\"{f}\") = {_Fruits}")
    #
    # [1-8] ...filtering via loop (and by the filter function).
    #
    print("\nFiltering fruits starting with 'P' (upper or lower case):")
    pfruits = collectp_via_loop(_Fruits)
    print(f"\ncollectp_via_loop({_Fruits}) = {pfruits}")
    pfruits = collectp_via_filter(_Fruits)
    print(f"\ncollectp_via_filter({_Fruits}) = {pfruits}")
    print("\nSeries-1 Done")


# [2] Series 2
# ----------------------------------------------------------------------------
# Assumption: List development is sequential.
# Assumption: A degree of freedom is allowed for developing command-line UI.
# Assumption: Operations on common list may be destructive.


def delete_fruit_by_name(fruits_in):
    """
    """
    fruit_to_delete = ""
    fruit_exists = False
    print(f"\nfruits_in = {fruits_in}")
    if (len(fruits_in) > 0):
        while(not fruit_exists):
            fruit_to_delete = input("\nWhich fruit shall be deleted? ")
            fruit_to_delete\
                = fruit_to_delete.replace("\"", "").strip().capitalize()
            fruit_exists = any(string_equal(fruit, fruit_to_delete, True)
                               for fruit in fruits_in)
            if (not fruit_exists):
                print("\nThat fruit does not exist. Pick one from the list.")
        while fruit_exists:
            fruits_in.remove(fruit_to_delete)
            fruit_exists = any(string_equal(fruit, fruit_to_delete, True)
                               for fruit in fruits_in)
        # [3] Display the list.
        print("\ndelete_fruit_by_name(fruits_in) = {}".format(fruits_in))
    else:
        print("\nThere is no fruit in the fruits list.")
    return fruits_in


def series_2():
    """
    series_2()
    ----------
    Satisfy Series-2 requirements 1 through 5.
    """
    global _Fruits
    reset_fruits()
    print("\nSeries-2 Solutions")
    print("{}".format("-"*50))
    #
    # [1] Display the last state of list fruits.
    #
    print(f"\nfruits = {_Fruits}")
    #
    # [2] Remove the last fruit from the list.
    #
    last_index = len(_Fruits) - 1
    del(_Fruits[last_index])
    #
    # [3] Display the list.
    #
    print("\ndel(fruits[{}])\n\nfruits = {}".format(last_index, _Fruits))
    #
    # [4] Remove a fruit from list by name.
    #
    existing_fruits = _Fruits.copy()
    delete_fruit_by_name(existing_fruits)
    #
    # [5] Add duplicates of every item in list and repeat task [4] so that
    #     all occurrences of fruit are removed.
    #
    double_fruits = existing_fruits.copy()*2
    delete_fruit_by_name(double_fruits)
    #
    # Set shared list to last working list.
    #
    _Fruits = double_fruits
    print("\nSeries-2 Done")


# [3] Series 3
# ----------------------------------------------------------------------------
# Assumption: List development is sequential.
# Assumption: A degree of freedom is allowed for developing command-line UI.
# Assumption: Operations on common list may be destructive.

# --------------------------
# Series 3 command constants
# --------------------------
_SER3_CMD_YES = ":yes"
_SER3_CMD_NO = ":no"
_SER3_CMD_EXIT = ":exit"


def response_to_command(user_response):
    """
    response_to_command(<user_response>)
    ------------------------------------
    Convert a user response to a function command.

    Entry: <user_response> ::= (str) from input function.
    Exit:  Returns _SER3_CMD_YES for <user_response> like "y*"; OR
           _SER3_CMD_NO for <user_response> like "n*"; OR
           _SER3_CMD_EXIT for <user_response> like "ex*"; OR
           "" for all other input.
    """
    global _SER3_CMD_YES
    global _SER3_CMD_NO
    global _SER3_CMD_EXIT
    result = "?"
    if (string_equal(user_response[0:1], "y", True)):
        result = _SER3_CMD_YES
    elif (string_equal(user_response[0:1], "n", True)):
        result = _SER3_CMD_NO
    elif (string_equal(user_response[0:2], "ex", True)):
        result = _SER3_CMD_EXIT
    else:
        result = ""
    return result


def equalp(a, b, ignore_case):
    """
    equalp(<a>, <b>, <ignore_case>)
    -------------------------------------
    For problem [1-8]. Are two values equivalent?

    Entry: <a>, <b>      ::= (str) Values to compare.
           <ignore_case> ::= (Boolean) When True, ignore char case when
                             both <a> and <b> are strings.
    Exit:  Returns True if <a> and <b> are equivalent.
    """
    if ((type(a) is str) and (type(b) is str)):
        result = string_equal(a, b, ignore_case)
    else:
        result = (a == b)
    return result


def delete_from_list(list_in, element_to_delete):
    """
    delete_from_list(<list_in>, <element_to_delete>)
    ------------------------------------------------
    Delete all occurrences of a value from a list.

    Entry: <list_in>           ::= (list) to delete from.
           <element_to_delete> ::= Value to delete.
    Exit:  Returns <list_in> with <element_to_delete>) removed.
    """
    element_exists = any(equalp(element, element_to_delete, True)
                         for element in list_in)
    while element_exists:
        list_in.remove(element_to_delete)
        element_exists = any(equalp(element, element_to_delete, True)
                             for element in list_in)
    return list_in


def get_user_command(subject):
    """
    get_user_command(<subject>)
    ---------------------------
    Get command response for dialog response to 'Do you like <subject>
    ([Y]es, [N]o, or e[X]it)?'

    Entry: <subject> ::= (str) subject of prompt
    Exit:  Returns _SER3_CMD_YES, _SER3_CMD_NO, _SER3_CMD_EXIT, or blank.
    """
    user_response = input("\nDo you like {} ([Y]es, [N]o, or e[X]it)? "
                          .format(subject.lower()))
    user_response = user_response.replace("\"", "").strip().lower()
    user_cmd = response_to_command(user_response)
    return user_cmd


def series_3():
    """
    series_3()
    ----------
    Satisfy Series-3 requirements 1 through 3.

    Entry: -
    Exit:  Multiple input and output events.
    """
    global _Fruits
    reset_fruits()
    valid_commands = (_SER3_CMD_YES, _SER3_CMD_NO, _SER3_CMD_EXIT)
    print("\nSeries-3 Solutions")
    print("{}".format("-"*50))
    #
    # [1] Query for user fruit fondness
    #
    local_fruits = _Fruits.copy()
    print("\nfruits = {}".format(local_fruits))
    unique_fruits = set(local_fruits)
    for unique_fruit in unique_fruits:
        user_cmd = get_user_command(unique_fruit)
        while (not (user_cmd in valid_commands)):
            #
            # [3] Limit user responses to "yes", "no"", and "exit" (last valid
            #     response allows user to bail out of processing every unique
            #     fruit, which can be tedious.)
            #
            print("\nInvalid response.")
            user_cmd = get_user_command(unique_fruit)
        if (user_cmd == _SER3_CMD_YES):
            #
            # No action for "yes" or "y*".
            #
            continue
        elif (user_cmd == _SER3_CMD_NO):
            #
            # [2] When the user response is "no". Also works for "na" and
            #     "nyet" and "non".
            #
            print(f"\nDeleting {unique_fruit}")
            local_fruits = delete_from_list(local_fruits, unique_fruit)
            print(f"\nfruits = {local_fruits}")
        elif (user_cmd == _SER3_CMD_EXIT):
            #
            # User entered "ex*". Exit loop.
            #
            break
        else:
            #
            # This should never be reached but I always include an 'else' in
            # an if-elif-else block.
            #
            continue
    print(f"\nRemaining fruits = {local_fruits}")
    print("\nNo fruit was bruised in the running of this function.")
    print("\nSeries-3 Done")


# [4] Series 4
# ----------------------------------------------------------------------------
# Assumption: List development is sequential.
# Assumption: A degree of freedom is allowed for developing command-line UI.
# Assumption: Operations on common list may be destructive.


def reverse_string(s):
    return s[::-1]


#   [1] Make a new list with the contents of the original, but with all the
#       letters in each item reversed.
#   [2] Delete the last item of the original list. Display the original list
#       and the copy.


def series_4():
    """
    series_4()
    ----------
    Satisfy Series-4 requirements 1 through 2.

    Entry: -
    Exit:  Multiple input and output events.
    """
    global _Fruits
    reset_fruits()
    print("\nSeries-4 Solutions")
    print("{}".format("-"*50))
    original_list = _Fruits.copy()
    #
    # [1] Original list with chars in string elements reversed.
    #
    print(f"\noriginal_list = fruits.copy() = {original_list}")
    rev_element_list = list(map(reverse_string, original_list))
    print("\nrev_element_list = list(map(reverse_string,original_list)) = {}"
          .format(rev_element_list))
    #
    # [2] Original list with last element removed.
    #
    copied_list = original_list.copy()
    print("\ncopied_list = {}".format(copied_list))
    del copied_list[-1]
    print("\ndel copied_list[-1]")
    print("\ncopied_list = {}".format(copied_list))
    print("\noriginal_list = {}".format(original_list))


if (__name__ == "__main__"):
    #
    # Satisfies overall requirement for command-line execution.
    #
    series_1()
    series_2()
    series_3()
    series_4()
