#!/usr/bin/env python3
import string
import random
import sys

words = "I wish I may I wish I might"

tale = """It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity,
it was the season of Light, it was the season of Darkness,
it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us,
we were all going direct to Heaven,
we were all going direct the other way – in short,
the period was so far like the present period,
that some of its noisiest authorities insisted on its
being received, for good or for evil,
in the superlative degree of comparison only."""


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
        keys: word pairs
        values: list of followers
    """
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


def prep_words(words):
    """
    Takes in a string and prepares it for building a trigram by
    removing punctuation and lowering all cases.  Then
    it convers the string to a list of words.

    returns a list of lower case words with punctuation removed'
    """
    translator = str.maketrans('', '', string.punctuation)
    return words.translate(translator).lower().split()


def build_story(trigrams):
    """
    Takes in a dict of trigrams and generates
    a random story

    returns a string
    """
    story = []
    # Pick a random trigram to start with
    key_tuple = random.choice(list(trigrams.keys()))
    story.append(key_tuple[0].capitalize())
    story.append(key_tuple[1])
    for i in range(20):
        # Break down into random sentence lengths from 6-15 words
        for w in range(random.randint(6, 15)):
            word_choices = trigrams[key_tuple]
            next_word = random.choice(word_choices)
            if i != 0 and w == 0 or next_word == 'i':
                story.append(next_word.capitalize())
            else:
                story.append(next_word)
            key_tuple = (key_tuple[1], next_word)
            if key_tuple not in trigrams:
                key_tuple = random.choice(list(trigrams.keys()))
        # Period at the end of each sentence.
        story[-1] = story[-1] + '.'
    return " ".join(story)


def process_file(filename):
    """
    Processes a file and adds it to a string.
    """
    words = ''
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            words = words + str(line)
    return words


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = process_file(filename)
    words = prep_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_story(word_pairs)

    # Find interesting word pairs
    # for k in word_pairs:
    #    if len(word_pairs[k]) > 5:
    #        print(str(k) + ": " + str(word_pairs[k]))

    print(new_text)

