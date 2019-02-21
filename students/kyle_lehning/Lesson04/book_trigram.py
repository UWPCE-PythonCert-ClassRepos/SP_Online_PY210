# !/usr/bin/env python3
import random
import re
import os


def build_trigrams(all_words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for idx, word in enumerate(all_words[:-2]):
        word_pair = word + " " + all_words[idx + 1]
        trigrams.setdefault(word_pair, [])
        trigrams[word_pair].append(all_words[idx + 2])
    return trigrams


def read_in_data(f_name):
    """
   read all text from Gutenburg book

   returns a string with all the words from the book
   """
    file_text = ""
    with open(f_name, "r") as file:
        for line in file:
            file_text += line.lower()
    updated_text = remove_punctuation(file_text)
    return updated_text


def remove_punctuation(p_string):
    """
   take an input string and remove punctuation, leaving in-word - and '
   """
    # (\b[-']\b) is a regular expression that captures intra-word ' and - in group(1)
    # the \b states that it is within a word, not at the end
    # |[\W_] is negated alpha num, same as [^a-zA-Z0-9], so captures all non alpha
    p = re.compile(r"(\b[-']\b)|[\W_]")
    # in the sub function check if it is captured in group(1) and if so restore it, else replace punctuation with " "
    updated_text = p.sub(lambda m: (m.group(1) if m.group(1) else " "), p_string)
    return updated_text


def make_words(input_string):
    """
   break a string of words into a list

   returns an ordered list of all words.
   """
    all_words = input_string.split()
    return all_words


def build_text(pairs):
    """
    take a dictionary trigram and make a story

    returns a string story.
    """
    first_key = random.choice(list(pairs.keys()))
    list_of_words = first_key.split()
    desired_sentence_length = random.randint(15, 20)  # Randomize how long to make the sentence
    sentence_length = 0
    while True:
        current_key = list_of_words[-2:]
        current_key_string = " ".join(map(str, current_key))
        if current_key_string in pairs.keys():
            next_word = random.choice(pairs[current_key_string])
            list_of_words.append(next_word)
            sentence_length += 1
        else:
            break
        if sentence_length == desired_sentence_length:
            break
    list_of_words[0] = list_of_words[0].capitalize()  # Make first letter capital
    list_with_cap = ["I" if x == "i" else x for x in list_of_words]  # Make I capital
    return (" ".join(list_with_cap)) + "."


if __name__ == "__main__":
    filename = (input("Enter the path of your file: ")).replace(r'"', '')  # remove quotes if copy as path used
    if os.path.exists(filename):
        in_data = read_in_data(filename)
        words = make_words(in_data)
        word_pairs = build_trigrams(words)
        new_text = build_text(word_pairs)
        print(new_text)
    else:
        print("I did not find the file at, "+str(filename))
