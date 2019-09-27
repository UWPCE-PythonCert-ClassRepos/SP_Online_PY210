#!/usr/bin/env python3
import random
import string

text_file = "sherlock.txt"
with open(text_file, 'r') as file:
    read_data = file.read()
file.close
words = read_data.split(" ")


def build_trigrams(words):
    """
    Build up the trigrams dict from the list of words.

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        key = (pair[0], pair[1])
        follower = words[i + 2]

        trigrams.setdefault(key, []).append(follower)

    return trigrams


def build_text(trigram_dict, word_limit):
    trigram_keys = list(trigram_dict.keys())

    # Initial seeding of words with random selection
    this_key = trigram_keys[random.randint(0, len(trigram_keys) - 1)]
    third_word = trigram_dict.get(this_key)[random.randint(0, len(trigram_dict.get(this_key)) - 1)]
    word_list = [this_key[0], this_key[1], third_word]

    # Loop until word limit is reached
    while len(word_list) < word_limit:
        this_key = (word_list[-2], word_list[-1])
        if this_key in trigram_dict:
            third_word = trigram_dict.get(this_key)[random.randint(0, len(trigram_dict.get(this_key)) - 1)]
            word_list.append(third_word)
        else:
            break

    return word_list


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams, 25)
    print(new_text)
    print(" ".join(new_text))

