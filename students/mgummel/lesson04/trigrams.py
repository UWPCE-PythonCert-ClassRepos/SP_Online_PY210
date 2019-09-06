#!/usr/bin/env python3
import random

HEADER = "*** START OF THIS PROJECT GUTENBERG EBOOK"
FOOTER = "End of the Project Gutenberg EBook"

def build_trigrams(words):
    """
    Builds up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # Builds up the trigram dictionary
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        # Checks to ensure the follower is not white space
        if follower:
            trigrams.setdefault(pair, list())
            trigrams[pair].append(follower)
    return trigrams


def read_in_data(file_to_parse):
    """
    Opens a file and parses through the entire document
    getting each line of text and storing it in a list.

    :param file_to_parse: the filename that needs to be opened
    :type file_to_parse: string
    """

    word = list()
    line =""
    with open(file_to_parse, mode='r', encoding='utf-8') as a_file:
        # Throws away all text that occurs in the document header
        while HEADER not in line:
            line = a_file.readline()

        # Stops parsing when the footer in the document is reached
        while FOOTER not in line:
            line = a_file.readline()
            line = line.replace("\n", "")
            word += line.split(" ")
    return word

def clean_words(clean_list):
    """
    Parses through the list of words and "cleans" all punctuation
    returns the same list void of many common punctiations.

    :param clean_list: a list of words needing punctuation clean up.
    :type clean_list: list
    """

    translate_map = {ord('\n'): None, ord("\""): None, ord(';'): None,
            ord(','): None, ord('!'): None, ord('?'): None, ord('.'): None}       
    index = len(clean_list) - 1

    while index >= 0:
        clean_list[index] = clean_list[index].translate(translate_map)
        clean_list[index] = clean_list[index].replace('.', '')
        clean_list[index] = clean_list[index].rstrip("\'")
        clean_list[index] = clean_list[index].rstrip(":")
        clean_list[index] = clean_list[index].lstrip("\'")

        index -= 1
    
    return clean_list

def build_text(word_pairs):
    """
    Using a dictionary, returns a list of random keys and their 
    respective random values, which are a list as well. If a key doesn't
    exist, the sentence will end and a new sentence will begin with
    a new random key and value

    :param word_pairs: dictionary key pairs to build the text
    :type file_to_parse: dictionary
    """
    word_list = list()
    random_key = tuple()

    # Gets random words and adds them to a list.
    while len(word_list) < 300:
        # Checks to make sure key exists in the trigams dictionary
        if random_key not in word_pairs:
            if len(word_list) > 0:
                word_list[-1] += "."
            random_key = list(word_pairs)[random.randint(0, len(word_pairs))]
            word_list.append(random_key[0].title())
            word_list.append(random_key[1])

        third_word = random.choice(word_pairs[random_key])
        word_list.append(third_word)
        random_key = (word_list[-2], word_list[-1])

    word_list[-1] += "."
    return " ".join(word_list)

if __name__ == "__main__":
    in_data = read_in_data('sherlock.txt')
    clean_text = clean_words(in_data)
    trigrams = build_trigrams(clean_text)
    new_text = build_text(trigrams)
    print(new_text)