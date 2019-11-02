#!/usr/bin/env python3

import random

words = "I wish I may I wish I might".split()

test_words = '''One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own.'''.split()

print(words)
#print(test_words)

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    # build up the dict here!
    trigrams = {}
    for word in range(len(words)-2):
        pair = tuple(words[word:word+2])
        follower = words[word+2]
        #print(pair,follower)

        '''
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
        '''
        trigrams.setdefault(pair,[]).append(follower)

    return trigrams

#working on the below...need to figure out how to pull random dict key
def build_text(trigram_dict):
    print(random.choice(trigram_dict.keys()))
    new_text = ''
    return new_text

'''
To generate new text from this analysis, choose an arbitrary word pair
as a starting point. Use this pair of words to look up a random next word
(using the table above) and append this new word to the text so far.
This now gives you three words with a new word pair (second and third words)
at the end of the three-word text. Look up a potential next word based
on this pair. This generates another pair to add to the list, and so on.
'''


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)
    print(trigrams)
    print(new_text)
