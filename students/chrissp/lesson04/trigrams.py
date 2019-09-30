#!/usr/bin/env python3
import random
import string


def load_text(filename):
    """
    Open the file by the file name and return text.

    :param filename: name of file as a string with extension
    :return a string of file content
    """
    with open(filename, 'r') as file:
        read_data = file.read()
    file.close
    return read_data


def make_words(input_text):
    word_list = []
    keep_words = False

    lines = input_text.split("\n")
    for line in lines:
        if len(line) > 0:
            # Skip header starting on the line after ***
            if line.split(" ")[0] == "***":
                keep_words = True

            elif keep_words:
                if line.split(" ")[0] == "***":
                    break
                line_words = line.split(" ")
                for word in line_words:
                    if len(word) > 0:
                        word_list.append(word)
    return word_list


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
    word_list = [this_key[0].capitalize(), this_key[1], third_word]

    # Loop until word limit is reached
    while len(word_list) < word_limit:
        this_key = (word_list[-2], word_list[-1])
        if this_key in trigram_dict:
            third_word = trigram_dict.get(this_key)[random.randint(0, len(trigram_dict.get(this_key)) - 1)]

            if "." or "?" or "!" in word_list[-1]:
                third_word.capitalize()

            word_list.append(third_word)
        else:
            word_list.append("END")
            break
    if "." not in word_list[-1]:
        word_list[-1] = word_list[-1] + "."

    return word_list


def final_text(word_list):
    for word in word_list:
        if word[-1] == "\"":
            word = word + "\n\n"

    print(" ".join(word_list))


if __name__ == "__main__":
    file_data = load_text("sherlock.txt")
    words = make_words(file_data)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams, 25)
    final_text(new_text)

