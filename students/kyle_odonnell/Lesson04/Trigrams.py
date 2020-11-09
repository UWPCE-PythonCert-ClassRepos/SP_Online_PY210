#!/usr/bin/env python3


import random

word_string = "Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?".split()

def build_trigrams(words):
    trigram= {}
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        try:
            trigram[pair].append(words[i+2])
        except KeyError:
            trigram.update({pair:[words[i+2]]})
    return trigram


def generate_text(trigrams, size):
    new_text = []
    random_key = random.choice(list(trigrams.keys()))
    for i in random_key:
        new_text.append(i)
    random_value = random.choice(trigrams[random_key])
    new_text.append(random_value)
    for num in range(int(size)):
        key = new_text[-2], new_text[-1]
        while True:
            try:
                new_word = random.choice(trigrams[key])
                new_text.append(new_word)
                break
            except KeyError:
                key = new_text[-4], new_text[-3]
    new_string = " ".join(new_text)
    return new_string



def read_file(file_name):
    objFile = open(file_name, "r")
    corpus = ""
    for i in objFile:
        corpus.append(i)
    objFile.close()
    return corpus


text_corpus = read_file("sherlock.txt")
tri = (build_trigrams(word_string))
print(generate_text(tri, 10))





#if __name__ == "__main__":
#    trigrams_dict = build_trigrams(word_string)
#    print(trigrams_dict)