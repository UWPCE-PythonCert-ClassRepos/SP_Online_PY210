#!/usr/bin/env python3

words = "I wish I may I wish I might".split()

print(words)
print()

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

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
