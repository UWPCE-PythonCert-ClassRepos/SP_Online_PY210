#!/usr/bin/env python3
# PY210 Lesson 04 Trigrams - Chase Dullinger
import sys
import random

words = "I wish I may I wish I might I could I would".split()
words = "I wish I may I wish I might".split()


def read_in_data(filename, header_line=None, end_of_file_line=None):
    """Reads in filename and returns a list of the lines it contained.
    :param filename: filename to read in.
    :param header_line: line that signifies start of data.
    :param end_of_file_line: line that signifies no further data of use in file
    :returns lines: List of cleaned up lines from the read in file
    """
    lines = []

    in_text_section = False if header_line else True

    with open(filename, "r") as fn:
        for line in fn.readlines():
            print(line)
            if line.startswith(end_of_file_line):
                break
            if in_text_section:
                tmp_line = line.rstrip()  # Clean up end of line characters
                if tmp_line:  # No need to include empty lines
                    lines.append(tmp_line)
            if not header_line or line.startswith(header_line):
                in_text_section = True
                continue
    return lines


def make_words(lines):
    """Split a bunch of lines in individual words
    :param lines: list of strings to split into words
    :returns words: list of words"""
    words = []

    for line in lines:
        words.extend(line.split())
    return words


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):  # -2 so we don't overrun the end of the list
        pair = words[i:i + 2]
        follower = words[i + 2]
        trigrams.setdefault(tuple(pair), [])
        trigrams[tuple(pair)].append(follower)

    return trigrams


def get_random_word_pair(trigrams):
    """Select a random key in the trigram and return it's value (word pair)
    :param trigram: trigrams dictionary
    :returns words: list of words from the trigram
    """
    words = random.choice(list(trigrams.keys()))
    return words

def get_random_percentage(percentage=50):
    """Return true X% of the time"""
    return random.randrange(100) < percentage

def make_sentence(trigrams, max_length=100, min_length=3):
    """build up a sentence from the trigrams
    :param trigrams: trigrams dictionary
    :param max_length: int max number of words in a sentence
    :param min_length: int min number of words in a sentence
    :returns sentence: str sentence
    """

    sentence_words = []

    seed_words = get_random_word_pair(trigrams)

    sentence_length = random.randint(min_length, max_length)

    while len(sentence_words) < sentence_length:
        if seed_words in trigrams:
            sentence_words.extend(trigrams[seed_words])
            if get_random_percentage(10) \
            and not sentence_words[-1].endswith(","):
                sentence_words.append(",")
            seed_words = tuple(sentence_words[-2:])
        else:
            seed_words = get_random_word_pair(trigrams)

    sentence = " ".join(sentence_words)
    sentence[0].capitalize()  # Always need to capitalize the first word

    if sentence.endswith((",", ".","?","!")):
        sentence = sentence[:-1]
    # Choose how to end the sentence (i.e. period, ?, or !)
    if get_random_percentage(80):
        sentence += "."
    elif get_random_percentage(50):
        sentence += "?"
    else:
        sentence += "!"

    return sentence.replace(" ,", ",")  # strip off the space ahead of commas

def build_text(trigrams, max_sentences=1000, min_sentences=100):
    """build up a text from sentences created with trigrams
    :param trigrams: trigrams dictionary (passed to next function)
    :param max_sentences: int max number of sentences in text
    :param min_sentences: int min number of sentences in text
    :returns text: str output text
    """
    sentences = []
    text_length = random.randint(min_sentences, max_sentences)

    while len(sentences) < text_length:
        sentences.append(make_sentence(trigrams))
        if get_random_percentage(20):  # Start new paragraph 20% of the time
            sentences.append("\n")

    return " ".join(sentences)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    header_line = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    header_line = None
    end_of_file_line = "End of the Project Gutenberg EBook"
    in_data = read_in_data(filename, header_line, end_of_file_line)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    #
    print(new_text)
