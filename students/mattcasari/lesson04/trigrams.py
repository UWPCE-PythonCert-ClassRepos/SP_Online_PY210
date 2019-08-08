#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 4, Exercise 2

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/eiercises/kata_fourteen.html

"""
import sys
import string
import random
from pprint import pprint

words = "I wish I may I wish I might".split()
# words2 = "I wish I may I wish I might have the wish I wish tonight".split()

BOOK_START_STR = "*** START OF THIS PROJECT GUTENBERG EBOOK"
BOOK_END_STR = "*** END OF THIS PROJECT GUTENBERG EBOOK "
AVERAGE_SENTENCE_LENGTH = 20


def build_trigrams_old(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    num_words = len(words) - 1
    for i in range(len(words) - 2):
        pair = tuple(words[i : i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, [])
        trigrams[pair].append(follower)

    return trigrams


def find_start_of_text(in_data, start_str=""):
    """
    Finds the start  string in a block of text and returns
    the index of the text remaining.

    Args:
        in_data: String to search through
        start_str: String to search for (Case Sensitive!)
    Returns:
        Index of text remaining after start string or None
    """
    idx = in_data.find(start_str)
    if idx == -1:
        return None
    else:
        return idx


def find_end_of_text(in_data, end_str=""):
    """
    Finds the end string in a block of text and returns
    the index of the text remaining.

    Args:
        in_data: String to search through
        end_str: String to search for (Case Sensitive!)
    Returns:
        Index of text remaining after start string or None
    """
    idx = in_data.find(end_str)
    if idx == -1:
        return None
    else:
        return idx


def format_text(lines):
    """
    Remove punctuation and lowercase all words except for special cases.

    ToDo: 
        Allow contraction apostrophes to pass

    Args:
        lines: text lines to format.

    Returns:
        data: formatted text
    """
    data = []
    for line in lines.split():
        line = line.rstrip()
        line = line.translate(
            str.maketrans(string.punctuation, " " * len(string.punctuation))
        )
        line = remove_capitalization(line)
        if line:
            data.append(" ".join(line.split()))
    data = " ".join(data)
    data = data.replace("  ", " ")
    return data


def read_in_data(filename, start_str="", end_str=""):
    """
    Read in text from a file.  Looks for start string and returns all text 
    after with punctuation removed and lower case (except for I).

    Args:
        filename: Name of file to read in (with file extension)
        start_str: String which indicates start of actual text.
    
    Returns:
        Formatted text stripped from file

    """
    lines = []
    with open(filename, "r+") as infile:
        text = "".join(infile.readlines())
    return format_text(text)


def remove_capitalization(in_data):
    """
    Removes capitalization from string except for "I".

    Args:
        in_data: string to convert to lower case.
    Returns:
        Formatted string

    ToDo:
        Add ability to keep proper nouns capitalized.
    """
    return_data = []
    for data in in_data.split(" "):
        if data != "I":
            data = data.lower()
        return_data.extend("".join(data))
        return_data += " "
    return "".join(return_data[:-1])


def make_words(in_data):
    """
    Split string into words.

    Args: 
        in_data: string to split
    Returns:
        String split into words
    """
    words = in_data.split(" ")
    return words


def build_trigrams(words):
    trigrams = {}
    num_words = len(words) - 1
    for i in range(len(words) - 2):
        pair = tuple(words[i : i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, [])
        trigrams[pair].append(follower)

    return trigrams


def build_text(word_pairs, num_sentences=40):

    output_text = ['\t']

    for idx in range(num_sentences):
        # Start of Paragraph
        paragraph = []
        paragraph_length = random.randint(3, 8)
        # output_text.append('\n\t')

        for sentence_cnt in range(paragraph_length):
            # Start of sentence
            sentence_length = random.randint(15, 20)
            # print(sentence_length)
            sentence = []

            for word_cnt in range(sentence_length):
                # print(word_cnt)
                # Start of word
                word = []
                if word_cnt == 0:
                    word_pair = random.choice(list(word_pairs.keys()))
                    sentence.append(word_pair[0])
                    sentence.append(word_pair[1])
                else:
                    word_pair = tuple(sentence[-2:])
                    # print(word_pair)
                    # if word_pair not in word_pairs:
                    #     break
                    word_pair = word_pairs[word_pair]    
                    # print(word_pair)
                    if not word_pair:
                        break
                    sentence.append(random.choice(list(word_pair)))
                    # sentence.append(word_pair[1])
                    # print(sentence)

            sentence = " ".join(sentence)
            sentence += "."
            sentence = sentence.capitalize()
            paragraph.append(sentence)

        output_text.append("\n\n\t".join(paragraph))

    output_text = " ".join(output_text)
    # print("".join(output_text))

    return "".join(output_text)

if __name__ == "__main__":

    # Test Find Start String
    test_str = "I once found a shell\n *** Story Start\n Gooble Gobble says the Turkey"
    start_str1 = "*** Story Start"
    start_str2 = "*** story start"
    assert 22 == find_start_of_text(test_str, start_str1)
    assert None == find_start_of_text(test_str, start_str2)

    # Test Find End String
    test_str = "The end of the story\n proved to be too much\n for the young child.\n *** End of Story"
    end_str1 = "*** End of Story"
    end_str2 = "!!! this is the end"
    assert 67 == find_end_of_text(test_str, end_str1)
    assert None == find_end_of_text(test_str, end_str2)

    # Test Remove Capitalization Function
    test_str = "The story of how I wrote this program"
    remove_cap_string = remove_capitalization(test_str)
    assert "the story of how I wrote this program" == remove_cap_string

    # Test Format Text function
    test_str = "Welcome to another - chance to test my func() code!"
    formatted_str = format_text(test_str)
    assert "welcome to another chance to test my func code" == formatted_str

    # Test Format Text function with apostrophes
    # test_str = "He said 'Hello, this is Sam's' and left"
    # formatted_str = format_text(test_str)
    # print(formatted_str)
    # assert "he said hello this is sam's and left" == formatted_str

    # Test Make Words
    test_str = "one two three four five"
    make_words_words = make_words(test_str)
    assert ["one", "two", "three", "four", "five"] == make_words_words

    # Test build_trigrams
    test_words = "I wish I may I wish I might".split()
    build_tri_response = build_trigrams(test_words)
    tri_expected = {
        ("I", "may"): ["I"],
        ("I", "wish"): ["I", "I"],
        ("may", "I"): ["wish"],
        ("wish", "I"): ["may", "might"],
    }
    assert tri_expected == build_tri_response

    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename, BOOK_START_STR, BOOK_END_STR)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)
    with open('temp.txt', 'w') as f:
        f.write(new_text)
    # # trigrams = build_trigrams_old(words)
    # # pprint(trigrams)

    # # trigrams2 = build_trigrams(words2)
    # # pprint(trigrams2)
