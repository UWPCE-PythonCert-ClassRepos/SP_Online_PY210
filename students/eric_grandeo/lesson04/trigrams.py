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

        trigrams.setdefault(pair,[]).append(follower)

    return trigrams

def rand_choice(trigram_dict):
    return random.choice(list(trigram_dict.keys()))


#function to create the new text
def build_text(trigram_dict, words):
    #create empty list
    new_text = []
    #randomly select key
    rand_start = rand_choice(trigram_dict)
    print(rand_start)
    #add randomly selected key to new list
    for i in rand_start:
        new_text.append(i)



    while len(new_text) < 200:
    #while len(new_text) <= words:
        new_word = trigram_dict.get(tuple(new_text[len(new_text)-2:]),[])

        #if not in trigram dict, then select a new random key
        if new_word == []:
            rand_start = rand_choice(trigram_dict)
            for i in rand_start:
                new_text.append(i)
                continue
        #if the new_word has more than one value, randomly choose one          
        elif len(new_word)>1:
            select_word = random.choice(new_word)
            new_text.append(select_word)
        else:
            new_text.extend(new_word)


    return " ".join(new_text)

'''
To generate new text from this analysis, choose an arbitrary word pair
as a starting point. Use this pair of words to look up a random next word
(using the table above) and append this new word to the text so far.
This now gives you three words with a new word pair (second and third words)
at the end of the three-word text. Look up a potential next word based
on this pair. This generates another pair to add to the list, and so on.
'''


if __name__ == "__main__":
    trigrams = build_trigrams(test_words)
    #print(trigrams)
    rand_start = rand_choice(trigrams)
    new_text = build_text(trigrams, 200)
    #print()
    print(new_text)
