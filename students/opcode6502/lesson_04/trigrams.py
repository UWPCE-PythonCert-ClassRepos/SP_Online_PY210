# trigrams.py
# opcode6502: SP_Online_PY210


import sys


def build_text(word_pairs):
    print("build_text(word_pairs)")


def build_trigram(words):
    print("build_trigram(words)")


def make_words(in_data):
    print("make_words(in_data)")


def read_in_data(filename):
    print("read_in_data(filename)")


if __name__ == "__main__":
    #
    # UW: Get the filename from the command line
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
