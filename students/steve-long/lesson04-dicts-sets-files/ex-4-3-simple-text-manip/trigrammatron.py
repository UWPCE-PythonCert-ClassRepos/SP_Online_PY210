#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson04
# Simple Text Manipulation (trigrammatron.py)
# Steve Long 2020-10-16 | v0
#
# Requirements:
# =============
#
#   Trigrams
#   --------
#
#   Trigrams can be used to mutate text into new, surreal, forms. But what
#   heuristics do we apply to get a reasonable result?
#
#   The Problem
#   -----------
#
#   Trigram analysis is very simple. Look at each set of three adjacent words
#   in a document. Use the first two words of the set as a key, and remember
#   the fact that the third word followed that key. For example, given the
#   input...
#
#     I wish I may I wish I might
#
#   ...will yield the following relationship...
#
#     "I wish" => ["I", "I"]
#     "wish I" => ["may", "might"]
#     "may I"  => ["wish"]
#     "I may"  => ["I"]
#
#   To generate new text from this analysis, choose a word pair as a
#   starting point. Use this pair of words to look up the list of next words,
#   choose a random element from this list, and append it to the word pair
#   to form a phrase...
#
#     "I may I"
#
#   Use the last two words of this phrase as the next key ("may I") which is
#   mapped to word "wish". The next phrase becomes...
#
#     "may I wish"
#
#   For this exercise, try implementing a trigram algorithm that generates a
#   couple of hundred words of text using a book-sized file as input.
#
#   Objectives
#   ----------
#
#   The assignment includes using mapping data structures and determining the
#   heuristics for processing the text. What do we do with punctuation?
#   Paragraphs? Do we have to implement backtracking if we choose a next word
#   that turns out to be a dead end?
#
#   Developing Your Solution
#   ------------------------
#
#   This assignment has two parts: the trigrams exercise itself and the  text
#   processing to get a full book in shape for processing.
#
#   A large data file is required for processing.
#
#   The source text file may require cleanup prior
#   to building the trigram map.
#
#   There may be multiple occurrences of the 2-word pair mapped to different
#   third words; capture all of the third words.
#
#   Several additional cleanup operations may be implemented:
#
#     - Strip out punctuation? - If you do this, what about contractions, i.e.
#       the appostrophe in "can't" vs. a single quotation mark – which are the
#       same character.
#
#     - Remove capitalization? - If you do this, what about "I"? And proper
#       nouns?
#
#     - Any other ideas you may have.
#
# Assumptions:
# ============
#
#   There is enough ambiguity in the requirements to allow a degree of
#   artistic freedom. The implementation description reveals some of the
#   choices.
#
# Implementation:
# ===============
#
#   Trigrammatron sounded like an insidious title for the script, so I used it.
#
#   The filtering the text file data is implemented with the goal of providing
#   a set of words with minimal punctuation and symbolic characters (chars)
#   in order to generate at least a few sensible phrases. Data is processed on
#   a line basis, not with every word of the document chained together.
#   chaining the entire document word list into a single list only generates
#   additional nonsensical phrases. The word1+word2 key maps to a list
#   of unique word3 values.
#
#   *Output. The script accepts an input file name and provides the ability to
#   use the the trigram data structure three different ways. See the
#   documentation string for function run_trigrammatron_demo_ui below.
#
#   *File clean-up. File cleanup is extensive. Sequences of allowed and
#   disallowed substrings are collected into sets for checking and line, word,
#   and character substitution. It does not include removing item numbers and
#   certain other "technical" text (the marginal return on that time
#   expenditure was not deemed worthwhile.)
#
#   *Handling missing values. Function show_trigrams_haiku chains word 2 and 3
#   of a trigram into the key for the next phrase. If there is no entry for
#   that key (due to the word filtering process or because the word pair
#   appeared at the end of a line) then the output terminates.
#
#   Style. Function run_trigrammatron_demo_ui provides a crude user interface.
#
#   Checked with flake8.
#
# Script Usage:
# =============
#
# 	./trigrammatron.py
#
# Issues:
# =======
#
#   Requirements description should be simpler (it's a long explanation
#   for a simple concept).
#
# History:
# ========
# 000/2020-10-16/sal/Created.
#
# =============================================================================

import string
import random
import pathlib
from itertools import chain
from collections import defaultdict

# -- Generic functions --------------------------------------------------------


def is_blank(s):
    """
    Is string blank?
    """
    return (len(s) == 0)


def clean_string(s_in, delimiter):
    """
    clean_string(<s>, <delimiter>)
    ------------------------------
    Remove adjacent occurences of delimiter from a string.

    Entry: <s>         ::= (str) String to process.
           <delimiter> ::= (str) One or more consecutive chars to split and
                            rejoin <s> on.
    Exit:  Returns <s> with adjacent <delimiter> removed.
    """
    words = s_in.strip().split(delimiter)
    s = []
    for word in words:
        if (not is_blank(word)):
            s.append(word)
    s_out = delimiter.join(s)
    return s_out

# -- Char groups --------------------------------------------------------------

# ---- Non-alphanumeric symbols allowed on the INSIDE of a word ---------------


_Allowed_Symbols = ("(", ")", "[", "]", "{", "}", "<", ">", "\"", "'", "`",
                    "-", "_", "=", "|", "\\", "%", "$", "*", "@", "#", "~")

# ---- Non-alphanumeric symbols not allowed on the start or end of a word -----

_Disallowed_End_Symbols = ("-", "_", "=", "|", "\\", "%", "$", "*", "@", "#",
                           "~", ".", ",", "?", ":", ";", "!", "\"", "'",
                           "`", "(", ")", "[", "]", "{", "}", "<", ">")

# ---- Lines beginning or ending with these strings are discarded -------------

_Disallowed_Line_Ends = ("***",)

_All_Symbols = tuple(chain(_Allowed_Symbols, _Disallowed_End_Symbols))

_Allowed_Single_Letters = ("a", "I")

_Replacement_Symbols = (("_", " "), ("--", " "))

# -- Char sets ----------------------------------------------------------------

_Lowercase_Char_Set = set(string.ascii_lowercase)

_Allowed_Symbol_Set = set(_Allowed_Symbols)

_All_Symbol_Set = set(_All_Symbols)

_Allowed_Single_Letter_Set = set(_Allowed_Single_Letters)

_Disallowed_End_Symbol_Set = set(_Disallowed_End_Symbols)


# -- Word content tests -------------------------------------------------------


def is_symbols_only(s):
    """
    Is string composed exclusively of symbols?
    """
    result = True
    for c in s:
        if (c not in _All_Symbol_Set):
            result = False
            break
    return result


def is_all_upper_case(s):
    """
    Are all characters in a string uppercase letters?
    """
    result = True
    for c in s:
        if (c in _Lowercase_Char_Set):
            result = False
            break
    return result


# -- Display formatting -------------------------------------------------------


def format_word_one(word_in):
    """
    Format the first word of a trigram phrase.
    """
    word_out = word_in
    if (not is_all_upper_case(word_in)):
        word_out = word_in.capitalize()
    return word_out


def format_word_one_plus(word_in):
    """
    Format the second or third word of a trigram phrase.
    """
    word_out = word_in
    if (not is_all_upper_case(word_in)):
        word_out = word_in.lower()
    return word_out


def replace_substrings(line_in):
    """
    Replace substrings found in the replacement sequence.
    """
    # Rule: Certain strings identifiable as decorative in any context
    #       are replaced.
    line_out = line_in
    for fi, re in _Replacement_Symbols:
        line_out = line_out.replace(fi, re)
    return line_out


# -- Word editing -------------------------------------------------------------


def trim_disallowed_end_chars(word_in):
    """
    Remove disallowed characters from the ends of a word.
    """
    # Rule: Certain chars are removed from beginning or ending of words
    #       as extraneous.
    word_out = word_in
    n = 0
    for i in range(0, len(word_out)):
        c = word_out[i]
        if (c in _Disallowed_End_Symbol_Set):
            n = i + 1
        else:
            break
    word_out = word_out[n:]
    n = len(word_out)
    for i in range((len(word_out)-1), 0, -1):
        c = word_out[i]
        if (c in _Disallowed_End_Symbol_Set):
            n += -1
        else:
            break
    return word_out[:n]


def scrub_word(word_in):
    """
    Remove characters not allowed for the trigrammatron from a word.
    Returns a word.
    """
    #
    # Rule: Certain chars are not allowed on the ends of words.
    #
    word_out = trim_disallowed_end_chars(word_in)
    if (is_symbols_only(word_out)):
        #
        # Rule: Symbol chars alone do not constitute a word.
        #
        word_out = ""
    else:
        if (len(word_out) == 1):
            #
            # Rule: Single chars do not constitute a word.
            #
            if (word_out not in _Allowed_Single_Letter_Set):
                word_out = ""
    return word_out


def scrub_excluded_line(line_in):
    """
    Null out entire line if it starts or ends with a diallowed string.
    """
    # Rule: Lines beginning or ending in certain characters are entirely
    #       excluded from the construction set.
    line_out = line_in
    for lend in _Disallowed_Line_Ends:
        if (line_in.startswith(lend)):
            line_out = ""
            break
        elif (line_in.endswith(lend)):
            line_out = ""
            break
        else:
            continue
    return line_out


# -- Line editing -------------------------------------------------------------


def scrub_line(line_in):
    """
    Remove unsupported and unnecessary chars from a line of words.
    Returns a list of words.
    """
    words_out = []
    line = scrub_excluded_line(clean_string(line_in, " "))
    line = replace_substrings(line)
    if (not is_blank(line)):
        for word in line.split(" "):
            word = scrub_word(word)
            if (not is_blank(word)):
                words_out.append(word)
    return words_out


# -- Trigram driver -----------------------------------------------------------


def build_trigrams(source_pathname):
    """
    Build a trigram dictionary from a list of words [word1,
    word2, word3, wordN] where the key is (word|i|, word|i+1|)
    and the value is [word|i+2|]. The list tracks multiple
    third words mapped to the key.
    """
    trigrams = defaultdict(list)
    with open(source_pathname, 'r') as source_file:
        while True:
            line_in = source_file.readline()
            if (not line_in):
                break
            else:
                words = scrub_line(line_in)
                for i in range(0, len(words)-2):
                    key = (words[i].lower(), words[i+1].lower())
                    values = trigrams[key]
                    value = words[i+2]
                    if (value not in values):
                        trigrams[key].append(value)
    return trigrams


# -- Demo functions ----------------------------------------------------------


def show_contents_of_trigrams_a2z(trigrams):
    """
    Show sorted 3-word phrases built from trigrams.
    """
    for key in sorted(trigrams.keys()):
        values = trigrams[key]
        for value in sorted(values):
            print("({} {}) => {}"
                  .format(key[0], key[1], value))


def show_trigrams_haiku(trigrams):
    """
    Show 3-word phrases built from trigrams composed of the two
    elements the tuple forming the key for the third word. The
    first key is chosen randomly and the remaining phrases are
    found thus:

    phraseN:    = wordN1, wordN2, r-trigrams[(wordN1 wordN2)]
                = wordN1, wordN2, wordN3
    phraseN+1   = wordN2, wordN3, r-trigrams[(wordN2 wordN3)]

    where r-trigrams retrieves a random element from the list of
    words mapped to (wordN1 wordN2).

    Shows 3-word phrases until the next key does not map to a
    value and displays 'No word keyed on {key}' OR the number
    of allowed values is reached (to avoid user boredom.)

    Allowing the function to terminate when no key is reached is
    why data was processed on a per-line basis and does not chain
    the entire file's word list together.
    """
    random.seed()
    #
    # A counting mechanism is included because a user will probably get
    # bored with this after 3000 nonsense phrases.
    #
    n = 1
    max_n = 3000
    msg = ""
    keys = tuple(trigrams.keys())
    key = random.choice(keys)
    values = trigrams[key]
    msg = (f"No word keyed on {key}" if (not values) else "")
    while (values):
        value = random.choice(values)
        phrase = "{} {} {}".format(format_word_one(key[0]),
                                   format_word_one_plus(key[1]),
                                   format_word_one_plus(value))
        print(phrase)
        n += 1
        key = (key[1], value.lower())
        values = trigrams[key]
        if (n > max_n):
            #
            # The threshold of user patience has been reached.
            #
            msg = f"Max iteration count ({max_n}) reached"
            break
        elif (not values):
            #
            # Phrase keychain broken.
            #
            msg = f"No word keyed on {key}"
        else:
            #
            # Phrase keychain unbroken.
            #
            msg = ""
    print(msg)


def show_trigrams_phrase_from_random_key(trigrams):
    """
    Show 3-word phrase based on a random key and value from the
    key's mapped value sequence in the trigrams dictionary.
    One phrase is generated for each key in the trigrams structure.
    """
    random.seed()
    keys = tuple(trigrams.keys())
    key_count = len(keys)
    for n in range(0, key_count):
        key = keys[random.randrange(0, key_count)]
        values = trigrams[key]
        if (values):
            value = random.choice(values)
            print("{} {} {}."
                  .format(format_word_one(key[0]),
                          format_word_one_plus(key[1]),
                          format_word_one_plus(value)))
        else:
            print("No word keyed on {}".format(key))


# -- Demo user interface -----------------------------------------------------


_CMD_HAIKU = ":HAIKU"         # Command to generate chained 3-word phrases.
_CMD_RANDKEY = ":RANDKEY"     # Command to generate random 3-word phrases.
_CMD_A2Z = ":A2Z"             # Command to generate key-value pairs.
_CMD_EXIT = ":EXIT"           # Command to exit app.


def choice_to_cmd(choice):
    """
    Convert user input to specific command name.
    """
    choice = choice.strip(" ")
    cmd = None
    if (choice.isnumeric()):
        choice = int(choice)
        if (choice == 1):
            cmd = _CMD_HAIKU
        elif (choice == 2):
            cmd = _CMD_RANDKEY
        elif (choice == 3):
            cmd = _CMD_A2Z
        else:
            cmd = None
    else:
        choice = choice.upper()
        if (choice[0:2] == ":X"):
            cmd = _CMD_EXIT
    return cmd


def run_trigrammatron_demo_ui():
    """
    User interface for testing 'trigrammatron', a data structure for
    storing condition trigram words from the text file
    'a-prefects-uncle.txt'. User is presented with four choices:

    [1]  Haiku: The trigram is used to generate what looks like a
         crazy haiku of chained 3-word phrases with the first word
         capitalized.

    [2]  Random Key: Generates random 3-word phrases.

    [3]  A-to-Z: Pairs of key and each value in alphabetical order.

    [:X] Exit for user interface.
    """
    print("\nTrigrammatron Demo\n")
    prompt = "Enter text document filename > "
    source_pathname = input(prompt)
    source_path = pathlib.Path(source_pathname)
    if (source_path.exists()):
        source_pathname = str(source_path)
        trigrams = build_trigrams(source_pathname)
        prompt = "[1] Haiku, [2] Random Key, [3] A-to-Z, e[:X]it > "
        cmd = None
        while (cmd != _CMD_EXIT):
            print("\n{}".format(("-" * 80)))
            choice = input(prompt)
            print("")
            cmd = choice_to_cmd(choice)
            if (cmd == _CMD_HAIKU):
                show_trigrams_haiku(trigrams)
            elif (cmd == _CMD_RANDKEY):
                show_trigrams_phrase_from_random_key(trigrams)
            elif (cmd == _CMD_A2Z):
                show_contents_of_trigrams_a2z(trigrams)
            else:
                continue
        print("\nExiting Triagrammatron Demo")
    else:
        source_pathname = str(source_path)
        fmt = "\nMissing text document {} from local source folder."
        print(fmt.format(source_pathname))
        print("\nRestart script and provide valid document name.\n")


if __name__ == "__main__":
    run_trigrammatron_demo_ui()
