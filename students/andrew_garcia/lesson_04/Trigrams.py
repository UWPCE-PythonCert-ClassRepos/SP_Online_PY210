import random
import string

words = "when I sing and dance I walk around the room a lot when I smile the room turns upside down when I frown I go and sit down".split()

def build_pairs(text):
    word_pairs = {}

    for i in range(len(words)-2):
        pair = ' '.join(words[i:i + 2])
        follower = words[i + 2]

        if pair not in word_pairs:
            word_pairs[pair] = [follower]
        elif pair in word_pairs:
            word_pairs[pair] += [follower]
    return word_pairs


def build_text(word_pairs):
    building_text = []

    #gets a random pair to start
    pair_choice = random.choice(list(word_pairs))
    building_text += pair_choice.split()

    #gets key value
    pair_follower = random.choice(list(word_pairs[pair_choice]))
    building_text.append(pair_follower)

    #gets new pair
    if len(building_text) < 100:
        new_pair = ' '.join(building_text[-2:])
        while True:
            if new_pair in word_pairs:
                building_text.append(random.choice(list(word_pairs[new_pair])))
                new_pair = ' '.join(building_text[-2:])
            else:
                break
    print(' '.join(building_text))

build_text(build_pairs(words))