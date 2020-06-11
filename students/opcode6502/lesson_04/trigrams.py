# trigrams.py
# opcode6502: SP_Online_PY210


import random
import re
import sys
import string


sample_text = 'I wish I may I wish I might'


def get_random_pair(word_pairs):
    random_line = random.choice(list(word_pairs))
    return random_line


def build_text(word_pairs):

    def create_random_entry(word_pairs):
        random_entry = random.choice(list(word_pairs.keys()))
        return random_entry

    def create_random_list(word_pairs):
        random_list = create_random_entry(word_pairs)
        text_append(random_list)

    def get_last_db_entry(text):
        # We need to grab the last entry in the database.
        #
        # [ TO-DO ]: Add notes to code locker: Helpful documentation on slicing here:
        # https://stackoverflow.com/questions/509211/understanding-slice-notation
        return (text[-2:][0], text[-2:][1])

    def get_next_db_entry(last_db_entry):
        next_db_entry = random.choice(word_pairs[last_db_entry])
        return next_db_entry

    def text_append(random_list):
        text.append(random_list[0])
        text.append(random_list[1])
        return text

    # Create a new text list object.
    text = []

    # Kick everything off with a seed.
    create_random_list(word_pairs)

    # We have to wrap this is a try / except block as we will eventually
    # get a KeyError which we need to handle.
    try:
        # [ TO-DO ]: Improve this by moving away from a for loop.
        # [ TO-DO ]: Improve this by checking input / output of these methods.
        # [ TO-DO ]: Additional exception handling?
        for i in range(100):
            last_db_entry = get_last_db_entry(text)
            next_db_entry = get_next_db_entry(last_db_entry)
            text.append(next_db_entry)
    except KeyError:
        # Do nothing here.
        pass

    return text


def build_trigram(words):

    trigrams = {}

    # [ TO-DO ]: Research why -2.
    for i in range(len(words) - 2):
        #
        # Cast to tuple.
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        #
        # Check and append.
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams


def make_words(in_data):

    output = ''

    for data in in_data:
        # Remove punctuation.
        #
        # [ TO-DO ]: Add notes to code locker:
        # Found a helpful article online that applies here.
        # Review regex StackOverflow article
        # to get enhanced punctuation coverage here.
        #
        # [ TO-DO ]: Also: input sanitization?
        data = re.sub(r'[^\w\s]','',data)
        output += data

    output_split = output.split()

    return output_split


def read_in_data(filename):

    # [ TO-DO ]: Add exception handling.
    with open(filename, 'r') as file:
        data = file.read()
    file.close()

    return data


if __name__ == '__main__':

    # UW: Get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print('[ ERROR ]: Please input a file name: [ \'your_file.txt\' ]')
        sys.exit(1)

    # Run with the sample text.
    print('[ DEBUG ]: Sample text: ')
    words = make_words(sample_text)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)
    for item in new_text:
        print(item + ' ', end='')
    # Add some spacing.
    print()
    print()

    # Run with a larger text sample.
    # Please specify 'c.txt' to load in Voltaire sample.
    print('[ DEBUG ]: Larger text: ')
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs_02 = build_trigram(words)
    new_text_02 = build_text(word_pairs_02)
    for item_02 in new_text_02:
        print(item_02 + ' ', end='')
    print()
