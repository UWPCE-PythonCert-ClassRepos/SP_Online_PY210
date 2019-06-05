#!/usr/bin/env python3

# Russell Felts
# Assignment 4 - Trigram Kata

import re
import random

def read_file(file_name):
    """
    Read the specified file and seperate it into words.
    :param file_name - String representing the file to open
    """
    with open(file_name) as temp_file:

        # Feed the file text into findall() it returns a list of all the found strings
        word_list = re.findall(r'[\w+]+', temp_file.read(), re.IGNORECASE)

    return word_list


def create_trigram_dict(word_list):
    """
    Take a list of strings and input it into a dictionary using two successive words as a key and the trailing word
    as the value.
    :param word_list - String list containing the words/strings to use for the trigram
    :return trigram_dict - Dict containing a list of individual words that can follow a two word sequence
    """

    trigram_dict = {}
    for item in range(len(word_list)-2):

        # Check to see if the keys are already in the dictionary. Might want to add a try catch for index out of bounds
        if (word_list[item], word_list[item+1]) not in trigram_dict:
            trigram_dict[word_list[item], word_list[item+1]] = [word_list[item+2]]
        else:
            trigram_dict[(word_list[item], word_list[item+1])].append(word_list[item+2])

    return trigram_dict


def create_story(trigram_dict):
    """
    Build the story using starting with a random key from the dict. Then continue getting values from the dict and
    adding them to the story
    :param trigram_dict - Dict containing a list of individual words that can follow a two word sequence
    :return story - List of strings representing the story
    """

    # Start the story by getting a random key and converting it to a string
    story = list(random.choice(list(trigram_dict.keys())))
    # print("Story: ", story)

    # Generate the initial key from the story
    key = tuple(story[-2:])
    # print("Key: ", key)

    while key in trigram_dict:
        # print("Values: ", trigram_dict[key])

        value = random.choice(trigram_dict[key])
        # print("Value: ", value)

        story.append(value)
        # print("Story:", story)

        key = tuple(story[-2:])
        # print("New Key:", key)

        if len(story) > 500:
            break

    return story


def printStory(story):
    """
    Print the story
    :param story: List of strings containing the story text
    """

    book = ' '.join(story)
    print(book)


if __name__ == '__main__':

    word_list = read_file("sherlock.txt")
    trigram_dict = create_trigram_dict(word_list)

    # for key, value in trigram_dict.items():
    #    print("Key: ", key, " Value: ", value)

    story = create_story(trigram_dict)
    printStory(story)
