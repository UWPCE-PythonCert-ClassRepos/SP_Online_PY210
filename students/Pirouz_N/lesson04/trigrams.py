#!/usr/bin/env python3
"""
Purpose: Trigrams Part 1 python certificate from UW
Author: Pirouz Naghavi
Date: 07/08/2020
"""

# imports
import string
import re
import sys
import random

trigrams_dict = {}


def build_trigrams(words):
    """"This function build up the trigrams dict from the list of words. And saves it in global trigrams_dict.

    Args:
        words: Is list of words that will be used in building the trigrams.
    """
    for i in range(len(words) - 2):
        trigrams_dict.setdefault(tuple(words[i: i + 2]), []).append(words[i + 2])


def split_sentences(st):
    """"This function split sentences using ending characters such as {. ! ?}

        Args:
            st: Is string that needs to be split.

        Returns:
            A list of all the sentences in the in st.
    """
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]


def build_trigrams_dict_from_file(path):
    """"This function  build up the trigrams dict from a txt file. And saves it in global trigrams_dict.

    Args:
        path: Is the file path of the file used to create trigrams.
    """
    try:
        with open(path, 'r') as input_file:
            for line in input_file:

                # Splitting sentences first to correct for start of the word capitals only the only downfall of this
                # approach is when sentence starts with a noun
                sentences = split_sentences(line)

                # Removing punctuation
                for sentence in sentences:
                    words_list = sentence.translate(
                        str.maketrans('', '', string.punctuation.replace('-', '').replace("\'", ""))).split()
                    if len(words_list) == 0:
                        continue

                    # I can be capitalized anywhere in the sentence
                    words_list[0] = words_list[0].lower() if words_list[0] != 'I' else words_list[0]

                    # Removing single quotes and double quotes and other non alphanumeric charters from the beginning
                    # and end of every word before sending them to trigrams dictionary generator to be added
                    build_trigrams([item[0].translate(str.maketrans('', '', string.punctuation)) +
                                    item[1:-1] + item[-1].translate(str.maketrans('', '', string.punctuation))
                                    if len(item) > 2 and
                                    item != item[0].translate(str.maketrans('', '', string.punctuation)) +
                                    item[1:-1] + item[-1].translate(str.maketrans('', '', string.punctuation)) else item
                                    for item in words_list])
    except ValueError:
        print('Provided path is None or incorrect.')
    except TypeError:
        print('Provided path in not a file path.')
    except IOError:
        print('Provided path does not exist.')
    except:
        print('Unknown error has occurred. Program will be shutting down.')
        sys.exit(1)


def build_text():
    """"This function  build up text from trigrams dict extracted from a txt file and prints it."""

    # Selecting a random number sentences
    sentence_count = random.randint(min(1, len(trigrams_dict.keys())), min(1000, len(trigrams_dict.keys())))
    final_text = ''
    for _ in range(sentence_count):
        text_list = []

        # Selecting a random number words in a sentences
        word_count_in_sentence = random.randint(1, min(len(trigrams_dict.keys()), 200))

        # Deciding if this sentence is the final sentence of the paragraph
        not_end_paragraph = random.randint(0, 10)

        # Correcting the start of the sentence
        starting_key = list(trigrams_dict.keys())[random.randint(0, len(trigrams_dict.keys()) - 1)]
        start_of_sentence = list(starting_key)
        start_of_sentence[0] = start_of_sentence[0][0].upper() + start_of_sentence[0][1:]
        text_list += start_of_sentence

        # Generating the rest of the sentence
        for _ in range(word_count_in_sentence):
            if (text_list[len(text_list) - 2].lower(), text_list[len(text_list) - 1]) not in trigrams_dict:
                break
            options = trigrams_dict[(text_list[len(text_list) - 2].lower(), text_list[len(text_list) - 1])]
            text_list.append(options[random.randint(0, len(options) - 1)])

        # Adding generated sentence to the rest of the output while correcting end of the sentence period and next line
        if not not_end_paragraph:
            text_list[len(text_list) - 1] = str(text_list[len(text_list) - 1]) + '.\n'
        else:
            text_list[len(text_list) - 1] = str(text_list[len(text_list) - 1]) + '. '
        final_text += " ".join(text_list)
    return final_text


if __name__ == "__main__":

    # obtaining file name from user
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename.")
        sys.exit(1)

    # Build trigrams dict from file
    build_trigrams_dict_from_file(filename)

    # Build text
    print(build_text())
