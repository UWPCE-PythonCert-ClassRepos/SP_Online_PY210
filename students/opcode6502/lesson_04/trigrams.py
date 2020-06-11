# trigrams.py
# opcode6502: SP_Online_PY210


import random
import sys
import string


def build_text(word_pairs):
    print('[ DEBUG ]: build_text(word_pairs)')
    #
    #
    random_int = random.randint(0, 100)
    print('[ DEBUG ]: random_int: ' + str(random_int))


def build_trigram(words):
    print('[ DEBUG ]: build_trigram(words)')
    # print('[ DEBUG ]: words: ' + str(words))
    # print('[ DEBUG ]: type(words): ' + str(type(words)))
    #
    #
    trigrams = {}
    #
    #
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
    #
    # Return statement.
    return trigrams


def make_words(in_data):
    #
    # Debug statement.
    # print('[ DEBUG ]: make_words(in_data)')
    # print('[ DEBUG ]: in_data: ' + str(in_data))
    #
    #
    output = ''
    #
    #
    for data in in_data:
        #
        # Remove punctuation.
        data.translate(str.maketrans('', '', string.punctuation))
        output += data
    #
    # Split each word.
    output_split = output.split()
    #
    # Debug statement.
    # print('[ DEBUG ]: output_split: ' + str(output_split))
    #
    # Return statement.
    return output_split


def read_in_data(filename):
    print('[ DEBUG ]: read_in_data(filename)')
    print('[ DEBUG ]: filename: ' + str(filename))
    #
    #
    with open(filename, 'r') as file:
        data = file.read()
    file.close()
    #
    # Debug statement.
    # print('[ DEBUG ]: data: ' + str(data))
    #
    # Return statement.
    return data


if __name__ == "__main__":
    #
    # UW: Get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print('[ ERROR ]: Please input a file name: [ \'your_file.txt\' ]')
        sys.exit(1)
    #
    #
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)
    #
    #
    print(new_text)
