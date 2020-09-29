#!/usr/bin/env python3

import sys
import random


def extract_file_words(filename):
    """
    Returns a list of each word of a passed local .txt file
    File should be a .txt downloaded from Project Gutenberg
    """
    word_list = []
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
                for line in f:
                    if "End of the Project Gutenberg EBook" in line:
                        break
                    else:
                        word_list.extend(line.split())
    return word_list


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


def create_new_text(trigrammed_dict, desired_length=50):
    """create a new string from a dict of trigrammed words """

    starting_pair = random.choice(list(trigrammed_dict.keys()))
    new_text = list(starting_pair)
    new_text.append(random.choice(trigrammed_dict[starting_pair]))
    for _ in range(desired_length):
        new_pair = tuple(new_text[-2:])
        if new_pair in trigrammed_dict:
            new_text.append(random.choice(trigrammed_dict[new_pair]))
    return " ".join(new_text).capitalize()


def make_sentences(unpunctuated_string):
    """
    capitalize the first word of each sentence and
    ensure the text ends with a period

    """
    sentences = unpunctuated_string.split('. ')
    trimmed_sentences = [sentence.strip() for sentence in sentences]
    uppercased_sentences = [sentence[0].upper() +
                            sentence[1:] for sentence in trimmed_sentences]
    rejoined_sentences = '. '.join(uppercased_sentences)
    rejoined_sentences = rejoined_sentences.replace(' i ', ' I ')
    if rejoined_sentences[-1:] != '.':
        return rejoined_sentences + '.'
    else:
        return rejoined_sentences


def exit_program():
    """Exits the interactive script"""
    print("Ok Bye!")
    sys.exit()


if __name__ == "__main__":

    prompt = "\n".join((">>>",
                        "Let's trigram some text!",
                        "Type the name of a text file located in "
                        "the same folder as this script.",
                        "Or type 'exit' to Quit",
                        ">>> "))
    response = input(prompt)
    if response == 'exit':
        exit_program()
    trigram_length = int(input("How longish should this be?\n"))
    words = extract_file_words(response)
    trigrams = build_trigrams(words)
    # print(trigrams)
    unpunctuated_new_text = create_new_text(trigrams, trigram_length)
    final_text = make_sentences(unpunctuated_new_text)
    print(final_text)
