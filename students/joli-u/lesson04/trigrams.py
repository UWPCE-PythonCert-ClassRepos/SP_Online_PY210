#!/usr/bin/env python

import random
import string 

# words = "I wish I may I wish I might".split()

def read_in_data(filename):
    with open(filename, 'r') as f:
        text = f.readlines()
    # remove lines before/after actual book (body) text
    for i, ln in enumerate(text):
        if ln.startswith("*** START OF THIS PROJECT"):
            start = i + 1
        elif ln.startswith("*** END OF THIS PROJECT"):
            end = i
        else: pass
        
    return text[start:end]


def make_words(in_data):
    words = []
    in_tab = string.punctuation
    out_tab = (len(in_tab))*" "
    tran_tab = str.maketrans(in_tab, out_tab)
    
    for line in in_data:
        line = line.rstrip() # remove trailing whitespace in line
        line = line.translate(tran_tab) # remove all punctuation 
        line_words = line.split() # create list of words in the line
        for word in line_words:
            words.append(word.lower())
            
    return words


def build_trigram(words):
    """
    - builds trigramms dict from given text/list of words
    returns: dict with word pairs as keys; follower words as values
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        if pair in trigrams.keys():
            (trigrams[pair]).append(follower)
        else: trigrams[tuple(pair)] = [follower]
    return trigrams
    
def build_text(word_pairs):
    # choose random starting word pair
    start = random.choice(list(word_pairs.keys()))
    begin = " ".join(start)
    body_words = []
    
    while len(body_words) < 20:
        if start not in word_pairs.keys():
            break
        else:
            first, second = start
            # get values corresponding to selected key
            third_vals = word_pairs[(first, second)]
            if len(third_vals) > 1:
                third = random.choice(third_vals)
            else: third = third_vals[0]
            # add the three words to the collection of words
            body_words.append(third)
            start = (second, third)
    body = " ".join(body_words)
    text = " ".join([begin, body])
    text_frmt = (text[0]).title() + text[1:]
    sentence = f"{text_frmt}."
    return sentence

if __name__ == "__main__":
    # get the filename from the command line
    filename = input("Enter filename: ") + ".txt"    
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)