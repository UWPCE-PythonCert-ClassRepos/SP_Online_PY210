# !/usr/bin/env python3
import random
import re


def build_trigrams(all_words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!

    return trigrams


def read_in_data(f_name):
    """
   read all text from Gutenburg book

   returns a string with all the words from the book
   """
    file_text = ""
    with open(f_name, "r") as file:
        for line in file:
            file_text += line
    updated_text = remove_punctuation(file_text)
    return updated_text


def remove_punctuation(p_string):
    """
   take an input string and remove punctuation, leaving in-word - and '
   """
    # (\b[-']\b) is a regular expression that captures intra-word ' and - in group(1)
    # the \b states that it is within a word, not at the end
    # |[\W_] is negated alpha num, same as [^a-zA-Z0-9], so captures all non alpha
    p = re.compile(r"(\b[-']\b)|[\W_]")
    # in the sub function check if it is captured in group(1) and if so restore it, else replace punctuation with " "
    updated_text = p.sub(lambda m: (m.group(1) if m.group(1) else " "), p_string)
    return updated_text


def make_words(input_string):
    """
   break a string of words into a list

   returns an ordered list of all words.
   """
    all_words = input_string.split()
    return all_words


def build_text(pairs):
    """
    take a dictionary trigram and make a story

    returns a string story.
    """


if __name__ == "__main__":
    # get the filename from the command line
    # try:
        # filename = sys.argv[1]
    # except IndexError:
        # print("You must pass in a filename")
        # sys.exit(1)
    filename = r"C:\Users\lehni\Documents\Education\UW\PYTHON210\SP_Online_PY210\students\kyle_lehning\Lesson04\sherlock_small.txt"
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)
