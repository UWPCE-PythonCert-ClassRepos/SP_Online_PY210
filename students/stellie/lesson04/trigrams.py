#!/usr/bin/env python3

# Stella Kim
# Assignment 3: Kata Fourteen

import sys
import re
import random

def read_file(filename):
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

def make_words(data):
    clean_data = []
    for i in data:
        if i == ' ':
            pass
        else:
            clean_data.append(i.strip())
    num = random.randint(0, len(clean_data))
    words = clean_data[num].split(' ')
    # return(words)
    return(['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might'])

def build_trigram(words):
    print('Word list:', words)
    trigram = {}
    for item in range(len(words) - 2):
        pair = (words[item], words[item + 1])
        follower = words[item + 2]
        if pair not in trigram:
            trigram[(pair)] = [follower]
        else:
            trigram[(pair)].append(follower)
    return(trigram)

def create_story(trigram):
    story_list = []
    print('\nLength of dictionary:', len(trigram))
    print('\nTrigram:', trigram)
    print('\nKeys and Values:')
    for item in trigram.items():
        print(item)
    num = random.randint(0, len(trigram) - 1)
    print('\nRandomly chosen index number:', num)
    print('\nRandom set of keys from list (at index num):', list(trigram.keys())[num])
    for i in list(trigram.keys())[num]:
        story_list.append(i)
    # story_list.append(new_text)

    print('\nValues (at index num):', list(trigram.values())[num])
    print('\nLength of values (at index num):', len(list(trigram.values())[num]))
    val_num = random.randint(0, len(list(trigram.values())[num]) - 1)
    print('\nRandomly chosen value (at index num):', val_num)
    print('\nChosen value (at index num) to add to list:', list(trigram.values())[num][val_num])
    story_list.append(list(trigram.values())[num][val_num])

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
    print('New Trigram Story:', new_text)