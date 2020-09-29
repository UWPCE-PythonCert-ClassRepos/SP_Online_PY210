# ------------------------------------------#
# !/usr/bin/env python3
# Title: Trigrams.py
# Desc: Trigrams – Simple Text Manipulation
# Tian Xie, 2020-04-12, Created File
# ------------------------------------------#

import random

#words = "I wish I may I wish I might".split()


def read_in_data(filename):
    """Read the file and remove common punctuations and lower case it.
    """
    with open(filename, 'r') as f:
        words = f.read().replace("-", " ").replace("!", " ").replace(".", " ").replace(",", " ").replace('"', " ").\
            replace("'", " ").replace("?", " ").replace("@", " ").replace(':', " ").replace(';', " ").split()
        words = [each_word.lower() for each_word in words]
    return words


def build_trigram(words):
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
        #If key is in the dictionary, return its value. If not, insert key with a list and return list.
        trigrams.setdefault(pair, []).append(follower)
    return trigrams

def build_text(word_pairs):
    """ Build text length from 5 to 15 words.
    :param word_pairs
    :return:" ".join(sentence).capitalize()+". "

    """
    sentence = []
    sentence_length = random.randint(5, 15)
    first_word_pair = random.choice(list(word_pairs.keys()))
    for word in first_word_pair:
        sentence.append(word)
    # next pair is the last two words in that three-word text.
    while len(sentence) < sentence_length:
        next_pair = tuple(sentence[-2:])
        if next_pair in word_pairs:
            sentence.append(random.choice(word_pairs[next_pair]))
        #If you end up with a word pair that isn’t in the original text, start another new_pair with a random choice from word_pairs.
        else:
            new_pair = random.choice(list(word_pairs))
            sentence.append(random.choice(word_pairs[new_pair]))
    return " ".join(sentence).capitalize()+". "


if __name__ == "__main__":
    filename = "sherlock.txt"
    words = read_in_data(filename)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs) + build_text(word_pairs) + build_text(word_pairs) + build_text(word_pairs) + build_text(word_pairs) + build_text(word_pairs)
    print(new_text)
