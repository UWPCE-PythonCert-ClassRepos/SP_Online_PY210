#!/usr/bin/env python3
import random
import argparse
from collections import defaultdict


def main():
    """
    Read the filename given as an argument, build a dict of trigrams from it,
    and print a random sentence built from those trigrams.

    NOTE: This assumes that the inputted text has already been stripped to
    contain only words and sentences that should be parsed.
    """
    # get the filename and number of words from a CLI argument
    # (argparse is very handy because it does all the sanity checking for us)
    parser = argparse.ArgumentParser(
            description='Reads a text file for words and prints a sentence ' +
                        'mutated from those words.')
    parser.add_argument('file',
                        help='The text file to parse.')
    parser.add_argument('length',
                        nargs='?',
                        type=int,
                        default=20,
                        help='The number of words in the sentence.')
    args = parser.parse_args()

    # populate trigram
    trigrams = parse_trigrams(args.file)

    # build a random sentence
    print(build_sentence(trigrams, args.length))


def parse_trigrams(filename):
    """Parse trigrams from a given file."""
    # grab list of all words in file
    try:
        with open(filename, 'r') as f:
            words = f.read().replace('--', ' ').split()
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
        exit(1)
    except PermissionError:
        print(f"ERROR: Permission denied when reading '{filename}'!")
        exit(1)

    # parse words and populate trigram
    trigrams = defaultdict(list)
    for i, word in enumerate(words[2:], 2):
        pwords = parse_words([word, words[i-1], words[i-2]])
        key = (pwords[2], pwords[1])
        trigrams[key].append(pwords[0])

    return trigrams


def build_sentence(trigrams, length):
    """
    Build a sentence from a trigrams dict.

    :param trigrams: The trigram to build from.
    :param length: The number of words in the sentence. Must be positive.
    """
    # check that the length is positive
    if length < 1:
        print("ERROR: Length must be a positive number.")
        exit(1)

    # build list of words
    words = []
    for i in range(length):
        # grab a random word from the trigrams dict
        key = random.choice(list(trigrams))
        word = random.choice(trigrams[key])

        # if it's the first word, capitalize
        if i == 0:
            word = word.title()

        words.append(word)

    # format to string and put a period at the end
    sentence = " ".join(words) + "."
    return sentence


def parse_words(words):
    """
    Parse all given words to make them usable in a trigram and return them as
    a list.
    """
    out = []
    for word in words:
        out.append(parse_word(word))
    return out


def parse_word(word):
    """
    Parse a given word to make it usable in a trigram. This is very
    rudimentary.
    """
    # naive strip of punctuation
    stripchars = '.!?,():;"*'
    table = word.maketrans('', '', stripchars)
    word = word.translate(table)

    # strip apostrophes from start and end, as well as "'s"
    if word.startswith('\''):
        word = word[1:]
    if word.endswith('\''):
        word = word[:-1]
    if word.endswith('\'s'):
        word = word[:-2]

    # force to lowercase, except for "I" and associated contractions
    if not word == "I" and not word.startswith("I'"):
        word = word.lower()

    return word


if __name__ == "__main__":
    main()
