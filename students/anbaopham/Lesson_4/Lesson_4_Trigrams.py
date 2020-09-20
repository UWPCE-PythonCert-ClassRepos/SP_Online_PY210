import random

#words = ("I wish I may I wish I might").split()
import string
with open('sherlock_small.txt', 'r') as file:
    text_file = file.read().replace('\n', '')

symbols ='-.()--'

words = text_file.translate({ord("-"): " ",ord("("): "",
ord(")"): "",ord("."): "",ord(","): ""})
words = words.split()

def check_dictionary(trigrams, key):
    if key in trigrams:
        return True
    else:
        return False
def get_value(words, pair):
    value_list = []
    for i in range(len(words)-2):
        if words[i] == pair[0] and words[i:i+2] == pair:
            value_list.append(words[i+len(pair)])
    return value_list



def build_trigrams(words):
    trigrams = {}

    random_choice = random.choice(words)
    n = words.index(random_choice)
    for i in range(n,len(words)-2):
        pair = words[i:i+2]
        key = " ".join(pair)
        follower = words[i+2]

        if check_dictionary(trigrams, key) is False:
            trigrams[key] = follower
    for key in trigrams:
        pair = key.split()
        trigrams[key] = get_value(words, pair)
    print(random_choice)
    print(n)
    display_dictionary(trigrams)
    return trigrams


def display_dictionary(trigrams):
    for x, y in trigrams.items():
        print(x, y)



build_trigrams(words)
