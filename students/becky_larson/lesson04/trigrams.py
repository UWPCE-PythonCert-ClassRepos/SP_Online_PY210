#!/usr/bin/env python3
import sys
import random


def read_in_data(in_file):

    with open(in_file, 'r') as f:
        return f.read()


def make_words(data):
    return data.split()


def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):  # why -2 ?
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]

        if (pair in trigrams):
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    print(f'the trigrams are {trigrams}')
    return trigrams


def build_text(word_pairs):
    print("build_text")

    text_out = []
    loop_count = 1000

    # Create the start of the text
    first_two = random.choice(list(word_pairs.keys()))
    # print(f'first_two[0] {first_two[0]}')
    # print(f'first_two[1] {first_two[1]}')

    text_out.append(first_two[0])
    text_out.append(first_two[1])
    text_out.append(random.choice(word_pairs[first_two]))

    # Iterate to create a long text stream
    for i in range(loop_count):
        last_two = tuple(text_out[-2:])
        if last_two in word_pairs:
            text_out.append(random.choice(word_pairs[last_two]))
        # else:
            # print(f'last_two {last_two}')
            # print('NOT FOUND_________________-')

    return " ".join(text_out)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)

    words = make_words(in_data)

    word_pairs = build_trigram(words)

    new_text = build_text(word_pairs)

    print(new_text)
