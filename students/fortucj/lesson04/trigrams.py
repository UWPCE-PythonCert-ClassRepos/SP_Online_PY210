#!/usr/bin/env python

"""
Trigrams.

I chose to preserve all special characters.
To deal with them, seperate dicts were made which prevented situations such as non-matching
parenthesis, unclosed quotes, and sentences beginning without a period closing the prior one.
The new string builder selects which dict to use based on the existing characters in the str.
Lists of "closing" words (with periods, questions marks, excl marks) were built to close
sentences in which the last 2 words did not exist as keys in their appropriate dict.

Much of the complexity arises from this chosen technique.

The text was originally built for book text files from another source besides Project
Gutenberg. Selected material here had unique opening and closing quotation marks, which
optimally leverages processing techniques unlike that for the common quotation ("). Hence,
some stitching together of different processing methods is in this code.
"""

import random

import string

File = input("Please provide an absolute path with filename and extension to source file: \n")

# File = r'/Users/fortucj/Documents/skoo/Python/L04_src/airship.txt'

Dest = input("Please provide an absolute path with filename and extension for destination file: \n")

# Dest = r'/Users/fortucj/Documents/skoo/Python/L04_dst/new_string.txt'

Main_dict = {}
Start_dict = {}
Open_dict = {}
Opar_Nquo_dict = {}
Opar_Oquo_dict = {}
Oquo_Nbra_dict = {}
Oquo_Obra_dict = {}


def main_d():
    return Main_dict


def start_d():
    return Start_dict


def open_d():
    return Open_dict


def opar_nquo_d():
    return Opar_Nquo_dict


def opar_oquo_d():
    return Opar_Oquo_dict


def oquo_nbra_d():
    return Oquo_Nbra_dict


def oquo_obra_d():
    return Oquo_Obra_dict


# switch dict for changing trigram dicts
Switch_dict = {1: main_d, 2: start_d, 3: open_d, 4: opar_nquo_d, 5: opar_oquo_d,
                6: oquo_nbra_d, 7: oquo_obra_d}


# RETRIEVAL FUNCTION FOR QUERYING LAST CHARACTER
def get_last(item):
    return item[-1]


# RETRIEVAL FUNCTION FOR QUERYING FIRST CHARACTER
def get_first(item):
    return item[0]


# switch dict for querying first or last character of a word
# calling #7 is trivial, since the criteria for dict 7 excludes words with quotes anywhere
Switch_opr = {3: get_last, 4: get_last, 5: get_first,
                6: get_first, 7: get_last}

Dub_par = ['(', ')']
End_chrs = ['.', '?', '!']
Dub_brack = ['[', ']']

# criteria for dicts 3-7
Criteria = [[')', ']'], ['('] + Dub_brack, Dub_par + Dub_brack,
            [']'] + Dub_par, ['[', '"'] + Dub_par]


# TEXT PROCESSING: ADDS A PERIOD OR EXCL MARK TO A WORD THAT ALREADY HAS A CLOSED QUOTE OR...
# ...CLOSED PARENTHESIS
def close_str(srch_list, srch_chr, ind_mod, rep_chr):
    selection = random.choice(srch_list)
    sel_list = list(selection)
    if ',' in sel_list:
        sel_list.remove(',')
    if not any(x in selection for x in End_chrs):
        sym_ind = sel_list.index(srch_chr)
        sel_list.insert(sym_ind + ind_mod, rep_chr)
        selection = "".join(sel_list)
    return selection


# TEXT PROCESSING: ADDS A CLOSED QUOTE OR CLOSED PARENTHESIS TO A WORD THAT ALREADY HAS...
# ...A PERIOD
def add_quo_paren(current_follow, srch_chr, ind_mod, rep_chr):
    if rep_chr not in current_follow:
        acf_list = list(current_follow)
        sym_ind = acf_list.index(srch_chr)
        acf_list.insert(sym_ind + ind_mod, rep_chr)
        current_follow = "".join(acf_list)
    return current_follow


# THIS READS THE SOURCE TEXT AND GENERATES A LIST OF WORDS
def read_file():
    with open(File, 'r') as source:
        file_list = []
        remove_objs = []  # populate this list if you want to remove characters
        status = 'start'
        status_log = 0
        toss_list = ['adventure', 'chapter', 'part', 'book', 'episode', 'act']
        num_list = ['I', 'V', 'X', 'L', '.']
        dig_list = list(string.digits) + list('.')
        cut_list = ['End', 'of', 'Project', 'Gutenberg']
        for i, line in enumerate(source):
            line_list = line.split( )
            if line not in string.whitespace and status != 'scan':
                # log title
                if status == 'start' and line_list[0] == 'Title:':
                    title = line_list[1:]
                    status = 'title'
                # log author
                elif status == 'title' and line_list[0] == 'Author:':
                    author = line_list[1:]
                    status = 'auth'
                    # log criteria fo material after the end of text
                    crit_list = ['End', 'of', 'Project'] + title
                # criteria for start of table of contents
                elif status == 'auth' and (line_list[0] in ['I', 'I.', '1', '1.']):
                    status = 'first'
                    status_log = i
                # criteria for confirming table of contents
                elif status == 'first' and (i == status_log + 1) and\
                    (line_list[0] in ['II', 'II.', '2', '2.']):
                    status = 'second'
            # go into scan mode after the table of contents is passed
            elif status == 'second' and (line in string.whitespace):
                status = 'scan'
            elif status == 'scan' and (line not in string.whitespace):
                # if a line resembles the material after the end of text, look for the title...
                # ...and remove the ending comma
                if all(x in line_list for x in crit_list[:-1]):
                    word_ind = line_list.index(title[-1] + ',')
                    line_list.remove(title[-1] + ',')
                    line_list.insert(word_ind, title[-1])
                first_str = line_list[0]
                first_lst = list(first_str)
                # define variables for following criteria
                if len(line_list) > 1:
                    second_str = line_list[1]
                    second_lst = list(second_str)
                # skip line if it looks like a chapter heading (chapter or equivalent and num)
                if len(line_list) > 1 and ((first_str.lower() in toss_list) and (all(x in\
                    num_list for x in second_lst) or all(x in dig_list for x in second_lst))):
                    pass
                # skip line if it looks like another form of a chapter heading (number only)
                elif (all(x in num_list for x in first_lst) or all(x in dig_list for x in
                    first_lst)) and (first_lst[-1] == '.'):
                    pass
                # if it indeed is the material after the end of text, t
                elif all(x in line_list for x in crit_list):
                    break
                else:  # add a word to the list of words
                    for word in line_list:
                        word_list = list(word)
                        # if the remove objs list is poplated, this will cleanup characters
                        for char in word_list:
                            if char in remove_objs:
                                word_list.remove(char)
                        word_new = "".join(word_list)
                        file_list.append(word_new)
    return file_list


# THIS BUILDS A LIST OF WORDS ENCLOSED IN "QUOTES"
def build_dql(file_list):
    dub_quo_list = []
    for word in file_list:
        if word[0] == '"' and word[-1] == '"':
            dub_quo_list.append(word)
    return dub_quo_list


# THIS BUILDS THE TRIGRAM MAIN DICT
def build_main(file_list):
    main_dict = {}
    for i in range(len(file_list) - 2):
        key = tuple(file_list[i:i + 2])
        follow = file_list[i + 2]
        if (i == 0) or (key not in main_dict):
            main_dict[key] = [follow]
        elif key in main_dict:
            main_dict[key].append(follow)
    return main_dict


# THIS BUILDS DICTS 2-7
def build_27(main_dict, dub_quo_list):
    for keys in main_dict:  # cycle through each key
        # THE FOLLOWING BUILDS THE TRIGRAM START DICT
        key_a = keys[0]  # get the first item in the key
        key_b = keys[1]
        value = ' '.join(main_dict[keys])
        last_chrs = [key_a[-1], key_b[-1], value[-1]]
        str_joint = key_a + " " + key_b + " " + value
        list_test = [key_a, key_b, value]
        # criteria for keys that start with a capital letter
        if key_a[0].isupper() and ((not any(x in str_joint for x in Criteria[0]) and not
                any(x in last_chrs for x in ['"'])) or (all(x in str_joint for x in Dub_par))
                or (all(x in dub_quo_list for x in list_test)) or (all(x in str_joint for x in
                Dub_brack))):
            # build dict for starting the newly generated string
            Start_dict[keys] = main_dict[keys].copy()
        Open_dict[keys] = []  # setup open dict keys & values
        Opar_Nquo_dict[keys] = []  # setup dict for parenthesis opened, no quote. keys & values
        Opar_Oquo_dict[keys] = []  # setup dict for parenthesis opened, quote opened.
        Oquo_Nbra_dict[keys] = []  # setup dict for quote opened, no bracket.
        Oquo_Obra_dict[keys] = []  # setup dict for quote opened, bracket opened.
        for i, cases in enumerate(range(3, 8)):  # THE FOLLOWING BUILDS TRIGRAM DICTS 3-7
            for item in main_dict[keys]:  # cycle through each item in the key value
                if (not any(x in item for x in Criteria[i]) and (Switch_opr.get(cases)
                    (item) != '"')) or (all(x in item for x in Dub_par)) or (item in
                    dub_quo_list) or (all(x in item for x in Dub_brack)):
                    Switch_dict.get(cases)()[keys].append(item)  # add the item to key value
            # If none of the item values met the dict criteria then remove the key
            if Switch_dict.get(cases)()[keys] == []:
                Switch_dict.get(cases)().pop(keys)
    return Switch_dict.get(2)(), Switch_dict.get(3)(), Switch_dict.get(4)(),\
        Switch_dict.get(5)(), Switch_dict.get(6)(), Switch_dict.get(7)()


# THIS BUILDS LISTS OF CLOSEOUT ITEMS
def close_lists(file_list, dub_quo_list):
    quo_close_list = []
    paren_close_list = []
    end_close_list = []
    for item in file_list:
        # words to close quotes
        if (Switch_opr.get(7)(item) == '"') and (item not in dub_quo_list):
            quo_close_list.append(item)
        # words to close parenthesis
        if (')' in item) and (not all(x in item for x in Dub_par)):
            paren_close_list.append(item)
        # words to end sentences
        if (any(x in list(item) for x in End_chrs)) and (not any(x in list(item)
            for x in [Dub_par, Dub_brack]) and (item not in dub_quo_list)):
            end_close_list.append(item)
    return quo_close_list, paren_close_list, end_close_list


# THIS FUNCTION BUILDS THE NEW STRING BASED ON TRIGRAMS
def do_trigrams(quo_close_list, paren_close_list, end_close_list, dub_quo_list):
    case = 2
    # This selects the initial tuple from the start_dict
    initial_tuple = random.choice(list(Switch_dict.get(case)().keys()))
    sentence = ''
    current_follow = ''
    # THIS BUILDS A TRIGRAM BASED ON INPUT WORD TURPLES, WITHOUT ADDING TO STRING
    while True:
        if case == 2:  # Setting the initial tuple
            current_tuple = initial_tuple[:]
        elif case == 8:  # If we already added a closing parethesis  or quote to a word with...
            # ...a period, generate a new sentence afterwards using the start dict (case 2).
            case = 2
            current_tuple = random.choice(list(Switch_dict.get(case)().keys()))
        else:
            # General scenario, where the current tuple is now the latter of the prior tuple...
            # ...paired with the prior follow
            current_tuple = ((current_tuple[1], current_follow))
        current_pair = " ".join(current_tuple)
        if current_tuple in Switch_dict.get(case)():  # scenario for an available key
            current_follow = random.choice(Switch_dict.get(case)()[current_tuple])

        # WHAT TO DO IF CURRENT TUPLE ISN'T A KEY
        else:
            # TEST LINE: print('closeout', current_pair)
            # Select a word that has a period prior to terminating string...
            # ...and remove any parenthesis or quote if present
            if case == 3 and (current_follow not in end_close_list):
                close_sel = random.choice(end_close_list)
                cs_list = list(close_sel)
                if '"' in cs_list:
                    cs_list.remove('"')
                if ')' in cs_list:
                    cs_list.remove(')')
                close_sel = "".join(cs_list)
                sentence += " " + close_sel
            # Select a word with a closing parenthesis,...
            # ...and add a period prior to terminating string
            if case == 4:
                sentence += close_str(paren_close_list, ')', 1, '.')
            # Select a word with a closing quote,...
            # ...and add a period prior to terminating string
            if case == 6:
                sentence += close_str(paren_close_list, '"', 0, '!')
            break  # end command

        # WHAT TO DO IF THERE IS AN OPEN QUOTE OR PARENTHESIS LINGERING AND WE HAVE TO CLOSE IT
        if (case in [4, 5, 6]) and (current_follow in end_close_list) and \
            (current_tuple in Switch_dict.get(case)()):
            if '.' in current_follow:
                srch = '.'
            elif '!' in current_follow:
                srch = '!'
            elif '?' in current_follow:
                srch = '?'
            if case == 4:  # scenario for closing a parenthesis and sentence with same word.
                current_follow = add_quo_paren(current_follow, srch, 0, ')') + " "
            else:
                # scenario for closing a quote and sentence with the same word
                current_follow = add_quo_paren(current_follow, srch, 1, '"') + " "
                # Scenario for closing a quote, parenthesis, and sentence with the same word
                if case == 5:
                    current_follow = add_quo_paren(current_follow, srch, 1, ')') + " "
                # UNCOMMENT/COMMENT THESE LINES IF YOU WANT/DON'T-WANT TO CLOSE THE NEW...
                # ...STRING WITH A QUOTE (STYLE PREFERENCE)
                # if case == 6:
                    # sentence += " " + current_follow
                    # break
            case = 8

        # THIS ADDS NEW MATERIAL TO THE STRING
        if case == 2:  # Special scenario where the entire trigram is added.
            sentence += current_pair + " " + current_follow
            # Identifies characters for testing which dicts to use.
            test_str = current_pair + " " + current_follow
            test_list = test_str.split( )
            first_chrs = [test_list[0][0], test_list[1][0], test_list[2][0]]
            last_chrs = [test_list[0][-1], test_list[1][-1], test_list[2][-1]]
        else:  # Default scenario for adding the third word in the trigram
            sentence += " " + current_follow
            # Identifies characters for testing which dicts to use.
            test_str = current_follow
            test_list = [test_str]
            first_chrs = test_str[0]
            last_chrs = test_str[-1]

        # THESE TOGGLE BETWEEN VARIOUS DICTS, IN ORDER TO DEAL WITH...
        # ...CHARACTERS REQUIRING CLOSURE
        if case not in [4, 5, 6, 7, 8]:  # test if trigram dicts 3, 4, or 6 should be used
            if (not any(x in test_str for x in ['(', '[']) and ('"' not in first_chrs)) or\
                (all(x in test_str for x in Dub_par)) or (any(x in dub_quo_list for x in
                test_list)) or (all(x in test_str for x in Dub_brack)):
                case = 3
            elif ('(' in test_str) and (not all(x in test_str for x in Dub_par)) and \
                ('"' not in first_chrs):
                case = 4
            elif ('"' in first_chrs) and (not any(x in dub_quo_list for x in test_list)) and\
                ('[' not in test_str):
                case = 6
        # If there has been an unclosed parenthesis and no quotes, check if...
        # ...there is a closing parenthesis or an open quote
        elif (case == 4):
            if ('"' in first_chrs) and (not any(x in dub_quo_list for x in test_list)):
                case = 5
            if (')' in test_str) and (not all(x in test_str for x in Dub_par)):
                case = 3
        # If there has been an unclosed parenthesis and an unclosed quote,...
        # ...check if the quote has been closed
        elif (case == 5) and ('"' in last_chrs):
            case = 4
        # If there has been an unclosed quote and no brackets,...
        # ...check if there is a closing quote or an opening bracket
        elif (case == 6):
            if ('[' in test_str) and (not all(x in test_str for x in Dub_brack)):
                case = 5
            if ('"' in last_chrs) and (not any(x in dub_quo_list for x in
                test_list)):
                case = 3
        # If there has been an unclosed quote and an unclosed bracket,...
        # ...check if the bracket has been closed
        elif (case == 7) and (']' in test_str):
            case = 6
    return sentence

# THIS WRITES TO NEW FILE


# THIS IS THE MAIN FUNCTION
def main():
    file_list = read_file()
    dub_quo_list = build_dql(file_list)
    Main_dict = build_main(file_list)
    Start_dict, Open_dict, Opar_Nquo_dict, Opar_Oquo_dict, Oquo_Nbra_dict, \
        Oquo_Obra_dict = build_27(Main_dict, dub_quo_list)
    quo_close_list, paren_close_list, end_close_list = close_lists(file_list, \
        dub_quo_list)
    sentence = do_trigrams(quo_close_list, paren_close_list, end_close_list, dub_quo_list)
    with open(Dest, 'w') as new:
        new.write(sentence)


if __name__ == "__main__":
    main()
