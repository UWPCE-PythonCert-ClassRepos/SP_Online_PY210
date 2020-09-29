#!/usr/bin/env python
# PY210 Lesson 4 Trigram Assignment
# Jonathan Vu
#
import random
import string

from pygments.lexer import words


def read_in_data(file):
    with open(file, 'r') as f:
        story = f.read()
    f.close()
    story = story.lower()
    whitespace = dict.fromkeys('\r\n\t', ' ')
    punctuation = dict.fromkeys(string.punctuation, ' ')
    story = story.translate(story.maketrans(whitespace))
    story = story.translate(story.maketrans(punctuation))
    story = story.split()
    return story


def build_trigrams(words):
    # Builds a trigram from a word breakdown input
    trigram = {}
    # Loop through words
    for i in range(len(words) - 2):
        # Range -2 for index since we want to check the 3rd word from i
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        # See if the trigram already has a pair (key)
        if pair in trigram:
            trigram[pair].append(follower)
        else:
            trigram.setdefault(pair, [follower])
    return trigram


def build_text(trigram, word_breakdown):
    rand_int = random.randint(0, len(word_breakdown) - 2)
    key = word_breakdown[rand_int:rand_int + 2]
    choice = tuple(key)
    random_text = random.choice(trigram.get(choice))
    while len(key) < 250:
        while choice == (word_breakdown[-2], word_breakdown[-1]):
            key.pop()
            choice = (key[-2], key[-1])
            while len(trigram.get(choice)) == 1:
                if len(key) == 2:
                    key.pop()
                    rand_int = random.randint(0, len(words) - 3)
                    key.extend(words[rand_int:rand_int + 2])
                    choice = tuple(key)
                    break
                else:
                    key.pop()
                    choice = (key[-2], key[-1])
        random_text = random.choice(trigram.get(choice))
        key.append(random_text)
        choice = (choice[-1], random_text)
    return " ".join(key)


if __name__ == '__main__':
    list_of_words = read_in_data('sherlock_small.txt')
    grams = build_trigrams(list_of_words)
    final = build_text(grams, list_of_words)
    print(final)
