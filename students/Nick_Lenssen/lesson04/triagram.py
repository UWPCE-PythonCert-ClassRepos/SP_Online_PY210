#!/usr/bin/env python3
import random
import sys

def read_in(my_file):
    start = False
    words = ''
    with open(my_file, 'r') as f:
        for line in f:
            if '***' in line: #start the reading after this symbol
                start = True
                continue
            if start:
                no_dashes = line.replace('--', ' ') #eliminate punctuations
                no_commas = no_dashes.replace(',', '')
                no_paren_1 = no_commas.replace('(', '')
                no_paren_2 = no_paren_1.replace(')', '')
                no_quotes = no_paren_2.replace('"', '')

                words += no_paren_2
    return words

def make_words(data):
    words_list = data.split() #make the string of words into a list
    return words_list

def build_triagram(words_list):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    triagram = {} #each pair will have a follower
    for i in range(len(words_list)-2):
        pair = tuple(words_list[i:i + 2])
        follower = words_list[i + 2]
        if pair not in triagram.keys(): #add a new if the pair is the first time being added to the triagram
            triagram[pair] = [follower]
        else:
            triagram[pair].append(follower)  #append to an existing
    return triagram

def build_text(triagram):
    new_text = []
    tri_keys = list(triagram.keys())
    word_pair = tri_keys[0]
    new_text.extend(word_pair)
    sent_count = 0
    while True:
        if word_pair in triagram:
            next_word = random.choice(triagram[word_pair])
            print (word_pair, next_word)
            new_text.append(next_word)
            if new_text[-1].endswith('.') and new_text[-1] not in ['Mr.', 'Mrs.', 'St.', 'Dr.']:
                
                if len(new_text)>500:
                    break
                word_pair = random.choice(tri_keys)
                new_text.extend(word_pair)
                new_text[-2] = new_text[-2].capitalize()
                #word_pair = tuple(new_text[-2:])
                print (new_text[-2:],word_pair)
                sent_count = sent_count +1

            word_pair = tuple(new_text[-2:])
        else:
            word_pair = random.choice(tri_keys)

        #word_pair = tuple(new_text[-2:])
    text = ' '.join(new_text)
    return text

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = 'sherlock.txt'                  #sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in(filename)
    words = make_words(in_data)
    triagram = build_triagram(words)
    print (build_text(triagram))

    #print(new_text)