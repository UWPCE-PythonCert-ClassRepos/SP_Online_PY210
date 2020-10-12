#!/usr/bin/env python3
import os
import re
import random

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    i, j = 0, 3
    while j <= len(words):
        first_word, second_word, third_word = words[i].lower(), words[i+1].lower(), words[i+2].lower()
        key, value = (first_word, second_word), third_word
        # print(key, value)
        if first_word == '' or first_word == ' ' or (len(first_word) == 1 and first_word not in ('i','a')):
            pass
        elif second_word == '' or second_word == ' ' or (len(second_word) == 1 and second_word not in ('i','a')):
            pass
        else:
            if key not in trigrams:
                trigrams[key] = [value]
            else:
                trigrams[key].append(value)
        j += 1
        i += 1
    # remove all null values from trigram
    new_trigrams = {}
    for k,v in trigrams.items():
        if len(v) == 0 or v == [''] or (len(v) == 1 and v not in ('i','a')):
            continue
        else:
            new_trigrams[k] = v
    return new_trigrams


if __name__ == '__main__':
    # sourcing file from the local directory
    file_name = os.getcwd() + '/' + 'sherlock.txt'
    i = 0
    words_text = []
    with open(file_name,'r') as f1:
        for i in range(4): # Skipping the first four lines
            next(f1)  # skip first line
        for line in f1:
            if i <= 200: # reading the first 200 lines of the text
                line = re.sub(r'[--]', ' ', line) # remove '--'
                line = re.sub(r'[-]', ' ', line) # remove '-'
                words = line.split(' ')
                for w in words:
                    w = w.lower().strip()
                    w = re.sub(r'[^\w\s]','',w) # remove punctuation
                    words_text.append(w)
                i += 1

    trigram = build_trigrams(words_text)

    key_word_pair = [x for x in trigram.keys()]
    new_text = '' # new text
    # first text, picking the last key, value pair to form the first sentence
    new_text += ' '.join(key_word_pair[len(key_word_pair)-1]) # last key of the text
    new_text += ' '+ str(' '.join(trigram[key_word_pair[len(key_word_pair)-1]])) # value of that key added to the text
    for i in range(500):
        words = new_text.split(' ')
        l = len(words)
        t = (words[l-2], words[l-1])
        # print(t)
        if t in trigram: # checking if the tuple from last two words is in dict of words
            new_text += ' '.join(trigram[t])
            # print('here', trigram[t])
            # print(new_text)
        else:
            a, b = 0, len(key_word_pair)-2
            random_index = random.randint(a,b)
            key, value = key_word_pair[random_index], trigram[key_word_pair[random_index]]
            if len(key) == 1:
                word = '' + join(key)
                new_text = new_text + ' '+ word + ' '
            else:
                new_text += ' '
                new_text += ' '.join(key)
            if len(value) == 1:
                word = ''.join(value)
                new_text = new_text + ' '+ word + ' '
            else:
                new_text += ' '
                new_text += ' '.join(value)
            # print(key,value, random_index)
            # print(new_text)
    print(new_text)
