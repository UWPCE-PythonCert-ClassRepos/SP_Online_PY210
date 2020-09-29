#!/usr/bin/env python3
import random
#Trigrams – Simple Text Manipulation

def write_txt(diff_text):
    #Write the story into a new file.
    new_fn = input('New File Name? ')
    with open(new_fn + '.txt', 'w') as f:
        f.write(' '.join(diff_text))

def trigram(w):
    trigrams = {}
    for i in range(len(w) - 2):
        pair = tuple(w[i:i + 2])
        follower = w[i + 2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams

def text(pairs):
    temp_list = []
    for key, value in pairs.items():
        temp_list.extend([key[0], key[1], value[0]])
    #create a list of random word pairs from the list
    new_list = []
    for i in range (len(temp_list)-1):
        first = random.choice(temp_list)
        second = random.choice(temp_list)
        third = random.choice(temp_list)
        if [second, third] not in new_list:
            new_list.append(first)
            new_list.append(second)
            new_list.append(third)
            diff_text = " ".join(new_list)
        else: 
            break
    return diff_text


def data(fn):

    #make alist of words from .txt file
    w = list()
    with open(fn, 'r') as f:
        for e in f:
            for word in e.split():
                w.append(word)

    return w


if __name__ == "__main__":

    # get the fn from the command line
    fn = input('Enter File Name: ')
    w = data(fn)
    pairs = trigram(w)
    diff_text = text(pairs)

    print(diff_text)
