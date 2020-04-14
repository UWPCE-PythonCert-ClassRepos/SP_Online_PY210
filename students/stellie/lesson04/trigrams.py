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
    return(words)

def build_trigram(words):
    print(words)
    trigram = {}
    for item in range(len(words) - 2):
        pair = (words[item], words[item + 1])
        # print(pair)
        follower = words[item + 2]
        # print(follower)
        if pair not in trigram:
            trigram[(pair)] = [follower]
    return(trigram)

def create_story(trigram):
    print(trigram)

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
    # print(new_text)