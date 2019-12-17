#!usrbinenv python3
import random

in_file = "the_art_of_war.txt"

words = ""
line = ""

headder = True

with open(in_file, "r") as sample_text:
    while True:
        line = sample_text.readline()
        if headder == True:
            if line[:3] == "***":
                headder = False
        elif line[:3] == "***":
            break
        else:
            words += line.replace("\n", " ")
# print(words)
words = words.split()

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with
       keys word pairs
       values list of followers
    """ 
    trigrams = {}

    for i in range(len(words)-2):
        pair = words[i:i+2]
        pair = (pair[0], pair[1])
        follower = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower,]

    return trigrams

def write_text(trigrams):
    start = random.choice(list(trigrams.keys()))
    text = [start[0], start[1]]
    try:
        while True:
            last_pair = (text[-2:][0], text[-2:][1])
            next_word = random.choice(trigrams[last_pair])
            text.append(next_word)
            if next_word[-1] == ".":
                break
        print(" ".join(text))
    except KeyError:
        print(" ".join(text))

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    write_text(trigrams)
    