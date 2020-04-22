#!/usr/bin/env python3

# Stella Kim
# Assignment 3: Kata Fourteen

"""
This program takes text from a book and chooses a random line to build a trigram.
"""

import sys
import re
import random

def read_file(filename):  # reads text from file
    with open(filename, 'r') as book_file:
        book_text = book_file.readlines()  # reads text file by line
        book_file.close()
    # print(book_text)
    state = 0
    data = []
    start_text = '*** START OF THIS PROJECT GUTENBERG EBOOK THE WAR OF THE WORLDS ***'
    end_text = '*** END OF THIS PROJECT GUTENBERG EBOOK THE WAR OF THE WORLDS ***'
    for line in book_text:
        if state == 0:
            if start_text in line:
                state = 1
            else:
                pass
        elif state == 1:
            if end_text in line:
                state = 0
            else:
                line = re.sub(r'\W+', ' ', line.lower())
                data.append(line)
    return(data)

def make_words(data):  # creates 'clean' words from book text
    clean_data = []
    for i in data:
        if i == ' ':
            pass
        else:
            clean_data.append(i.strip())
    num = random.randint(0, len(clean_data))
    words = clean_data[num].split(' ')
    return(words)

def build_trigram(words):  # builds a trigram (dictionary) using words
    print('Word list:', words)
    trigram = {}
    for item in range(len(words) - 2):
        pair = (words[item], words[item + 1])
        follower = words[item + 2]
        if pair not in trigram:
            trigram[(pair)] = [follower]  # creates a new key/value pair
        else:
            trigram[(pair)].append(follower)  # adds to trigram values if key already exists
    return(trigram)

def create_story(trigram):  # creates the final trigram
    story_list = []
    print('\nTrigram Keys and Values:')
    for item in trigram.items():
        print(item)
    
    """Randomly chooses a key from the dictionary to add to the story list"""
    num = random.randint(0, len(trigram) - 1)
    for key in list(trigram.keys())[num]:
        story_list.append(key)

    """Randomly chooses a value from the picked key from dictionary to add to the story list"""
    val_num = random.randint(0, len(list(trigram.values())[num]) - 1)
    story_list.append(list(trigram.values())[num][val_num])

    """Finds the last two words from the story list in the dictionary and adds 
    the keys/values to the story list until the story reaches a maximum length
    of 100 words"""
    print('\nStory list:', story_list)
    last_two_words = tuple(story_list[-2::])  # takes the last two words from the list to use as key
    while last_two_words in trigram.keys():  # appends values to list based on key
        key_values = trigram[last_two_words]
        random_val = random.randint(0, len(key_values) - 1)
        new_word = key_values[random_val]
        story_list.append(new_word)
        last_two_words = tuple(story_list[-2::])
        if len(story_list) > 100:  # breaks at a limit of 100 words
            break
    
    story_list = ' '.join(story_list)
    return(story_list)

if __name__ == '__main__':
    # try:
    #     filename = sys.argv[1]
    # except IndexError:
    #     print('Please pass in a filename')
    #     sys.exit(1)
    data = read_file('wotw.txt')
    words = make_words(data)
    word_pairs = build_trigram(words)
    new_text = create_story(word_pairs)
    print('New Trigram Story:', new_text.capitalize() + '.')