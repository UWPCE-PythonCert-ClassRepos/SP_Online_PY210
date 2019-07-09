#!/usr/bin/env python3

import random
import string

test_words = 'I wish I may I wish I might'.split()

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
        keys: word pairs
        values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        pair_key = (pair[0], pair[1])
        if pair_key in trigrams:
            trigrams[pair_key].append(follower)
        else:
            trigrams[pair_key] = [follower]
    return trigrams

trigram = build_trigrams(test_words)
# pick a random item from a sequence
#print(trigram.keys())
#print(trigram[('wish','I')][1])
test = random.choice(list(trigram.keys()))
#print(trigram)

def build_text(word_dict):
    text = []
    start_key = random.choice(list(word_dict.keys()))
    text.append(start_key[0])
    text.append(start_key[1])
    if len(word_dict[start_key]) > 1:
        text.append(word_dict[start_key][random.randint(0,1)])
    else:
        text.append(str(word_dict[start_key][0]))
    for i in range(10):
        key = (text[i+ 1], text[i + 2])
        if key not in word_dict:
            break
        elif len(word_dict[key]) > 1:
            text.append(word_dict[key][random.randint(0,1)])
        else:
            text.append(word_dict[key][0])
        i += 1
    return " ".join(text)

#build_text(trigram)
print(build_text(trigram))

#if __name__ == "__main__":
#    trigram = build_trigrams(test_words)
#    print(trigram)
