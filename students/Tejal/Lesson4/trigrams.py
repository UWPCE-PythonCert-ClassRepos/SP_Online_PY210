#!/usr/bin/env python
import random
import sys


def read_filedata(filename):   

    lines = list()
    translate_chars = str.maketrans(',.?!;()', '       ')
    header = ('*** START OF THIS PROJECT GUTENBERG EBOOK')

    try:
        read_file = open(filename, 'r')
    except FileNotFoundError:
        print(filename, ': this file was not found.')
        sys.exit()

    # skip past the header of the file
    for line in read_file:
        if line.find(header) != -1:
            break

    # read until the end-of-book line is found
    for line in read_file:
        if line.isspace():
            continue
        elif line.find('End of the Project Gutenberg EBook') != -1:
            break
        else:
            line = line.translate(translate_chars)
            line = line.replace('"', '')
            line = line.replace('--', ' ')
            lines.append(line.lower())
    return lines


def wordMaking(lines):
   
    words = list()
    keep_capitalized = ['I', 'I\'m', 'I\'ll', 'I\'ve', 'I\'d']
    for line in lines:
        words.extend(line.split())
    for indx, word in enumerate(words):
        if word.capitalize() in keep_capitalized:
            words[indx] = word.capitalize()
    return words


def trigramsBuild(words):
 
    trigrams = {}

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pair)
        if key not in trigrams.keys():
            trigrams[key] = [follower]
        else:
            trigrams[key].append(follower)
    return trigrams


def textBuilding(trigrams, n=100, sent_length=10):
    

    try:
        key = random.choice(list(trigrams.keys()))
    except IndexError:
        print("Trigrams dictionary is empty.")
        print("Revise the header or use with a Project Gutenberg book file.")
        sys.exit()

    new_word_list = list(key)
    new_word_list[0] = new_word_list[0].capitalize()

    try:
        for i in range(n-2):
            next_follower = (trigrams[key][random.randint(0,
                             (len(trigrams[key]) - 1))])
            # add period to word after every 10 words
            if (i+3) % sent_length == 0:
                new_word_list.append(next_follower + '.')
                key = tuple([new_word_list[-2], next_follower])

            # capitalize word if it follows a period
            elif (i+3) % sent_length == 1:
                new_word_list.append(next_follower.capitalize())
                key = tuple([new_word_list[-2].strip('.'), next_follower])

            # redefine key while maintaining case sensitivity of trigrams
            elif (i+3) % sent_length == 2:
                new_word_list.append(next_follower)
                key = tuple([key[1], next_follower])

            else:
                new_word_list.append(next_follower)
                key = tuple(new_word_list[-2:])
    except KeyError:
        print('\nLast key not in dictionary of trigrams. Process aborted.\n')
    finally:
        new_text = " ".join(new_word_list)
        return new_text


if __name__ == '__main__':
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a file name.")
        sys.exit()

    lines =read_filedata(filename)
    words = wordMaking(lines)
    trigrams = trigramsBuild(words)
    new_text = textBuilding(trigrams)

    print(new_text)
