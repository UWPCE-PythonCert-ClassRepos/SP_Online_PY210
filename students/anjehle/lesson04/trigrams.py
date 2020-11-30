# ----------------------------------------------- #
# Title: Trigrams
# Dev: Alex Jehle
# Desc: This script creates a trigram structure to
#       generate blocks of text
# Change Log: Jehle, Alex 11/19/2020 - created
# ----------------------------------------------- #
import random
import sys


def read_in_data(input_name):
    """
        opens file and reads in text
        returns data string
    """
    read_data = []
    with open(input_name, 'rt') as infile:
        while True:
            line = infile.readline()
            add_words = line.split()
            for word in add_words:
                endlist = ["!", "?", "."]
                exclist = ["_", "/", '\"']
                punctuation = ''.join(x for x in word if x in endlist)
                new_word = ''.join(x for x in word if x not in exclist)
                read_data.append(new_word.strip())
            if not line:
                return read_data, punctuation


def create_trigrams(wordls) -> dict:
    """
        create the trigrams dict from the list of words

        returns a dict with:
           keys: word pairs
           values: list of followers
    """
    trigram_dict = {}
    for i in range(len(wordls)-2):
        pair = (wordls[i], wordls[i + 1])
        follower = wordls[i + 2]
        trigram_dict.setdefault(pair, []).append(follower)
    return trigram_dict


def generate_text(trigram_dict):
    """
        generates text from the trigram dict
        returns a list with generated text
    """
    first_word = random.choice(list(trigram_dict.keys()))
    follower_list = trigram_dict[first_word]
    words = [first_word[0], first_word[1]]
    while len(words) < len(trigram_dict):
        words.append(random.choice(follower_list))
        pair = tuple(words[-2:])
        if pair in trigram_dict.keys():
            follower_list = trigram_dict[pair]
        else:
            follower_list = trigram_dict[random.choice(list(trigram_dict.keys()))]
    return words


def printer(words, cap, name_file, limit: int):
    if limit > len(words):
        print("Word limit exceeds text length. \nPlease try with a smaller word limit.")
    print(f'TRIGRAMS TEXT BASED ON {name_file}\n')
    words[0].capitalize()
    for i, word in enumerate(words):
        if word in cap:
            words[i + 1].capitalize()
    for i in range(0, limit, 10):
        print(f'{words[i]} {words[i+1]} {words[i+2]} {words[i+3]} {words[i+4]} {words[i+5]} {words[i+6]} {words[i+7]} '
              f'{words[i+8]} {words[i+9]}')
    return


if __name__ == '__main__':
    # get the filename from the command line

    try:
        filename = sys.argv[1]
        word_limit = int(sys.argv[2])

    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data, end_sent = read_in_data(filename)
    trigram = create_trigrams(in_data)
    words_generated = generate_text(trigram)
    printer(words_generated, end_sent, filename, word_limit)
