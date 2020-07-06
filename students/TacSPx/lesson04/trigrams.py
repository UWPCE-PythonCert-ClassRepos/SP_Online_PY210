# ---------------------------------------------------------------------------- #
# Title: trigrams
# Description: Trigram analysis looks at each set of three adjacent words in a document.
# Use the first two words of the set as a key, and remember the fact that the third word
# followed that key.
#
#
# <06/08/2020>, Created Script
# ---------------------------------------------------------------------------- #
# imports
#import sys
import random
import re
# Data ---------------------------------------------------------------------- #

file_name = "AdvofHuckleberryFinn.txt"  # The name of the story text file
#words = []
#format_story = []

# Processing  --------------------------------------------------------------- #
def read_file():
    '''
    Step #1
    Load in "AdvofHuckleberryFinn.txt", this will work with other text
    but it will need to start with CHAPTER I. and end with THE END, you can
    manually add that in or modify the code to your start and stop point
    :return: Formatted words to be sent to build_trigrams function
    '''

    words = []
    # file_name = "AdvofHuckleberryFinn.txt"  # The name of the story text file
    with open(file_name, "r", encoding="utf-8") as infile:  # file errors, without adding encoding
        data = False
        for row in infile:
            # User can change staring "CHAPTER I." to another keyword for other text
            if row.startswith("CHAPTER I."):
                data = True
                continue
            # User can change ending "THE END." to another keyword for other text
            if row.startswith("THE END."):
                data = False
                break
            if data:
                words.extend(row.rstrip().split())
            # Need to use extend here to get rid of the carriage returns, rstrip might help with extra formatting spaces
    #print(words) - for testing
    return words

def build_trigrams(words):
    """
    Step #2
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
       returns: dictionary with follower selection list - all unformatted
    """
    trigrams = {}
    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        # add tuple type to make it immutable / use append to add more options to the follower selections
        trigrams.setdefault(tuple(pair), []).append(follower)
    #print(trigrams) - for testing
    return trigrams

def new_text(trigrams, story_len=2000):
    '''
    Step #3
    Select a random starting locations in the text build the story text
    by randomly choosing the follower text and joining everything together
    :param trigrams: fed from build_trigrams
    :param story_len: Sample length of text
    :return: raw trigram text
    '''

    starting_pair = random.choice(list(trigrams.keys()))
    new_text = list(starting_pair)
    new_text.append(random.choice(trigrams[starting_pair]))
    for i in range(story_len):
        new_pair = tuple(new_text[-2:])
        if new_pair in trigrams:
            new_text.append(random.choice(trigrams[new_pair]))
    # print(" ".join(new_text) #- for testing
    format_story = " ".join(new_text)
    # Add capitals after punctuation use (re) module
    punc_filter = re.compile("([.!?]\s*)")
    split_with_punctuation = punc_filter.split(format_story)
    format_story = ''.join([i.capitalize() for i in split_with_punctuation])
    # Adding some additional formatting clean-up
    format_story = format_story.replace("(", "").replace(")", "") # removes all parenthesis
    format_story = format_story.replace('"', '') # removes all quotes
    format_story = format_story.replace("''", "")  # removes all double quotes
    format_story = format_story.replace('_', "")  # removes all under bars
    format_story = format_story.replace('--', "")  # removes all double dashes
    format_story = format_story.replace(" i ", " I ").replace("i'll", "I'll").replace("i'd", "I'd").replace("i,", "I,")
    format_story = format_story.replace("jim", "Jim").replace("tom", "Tom").replace("sawyer", "Sawyer")
    #print(format_story)- for testing
    return format_story


# Main Body of Script  ------------------------------------------------------ #
def main():
    words = read_file()
    trigrams = build_trigrams(words)
    new_text(trigrams)
    print("\nHere is a sample of your story text that has been applied with a 'trigrams' algorithm:\n\n",
          new_text(trigrams, story_len=2000))

main()











