# creating trigram
words = "I wish I may I wish I might".split()
import random

def build_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = [words[i+2]]
        if pair in trigrams:
            trigrams[pair] += follower
        else:
            trigrams[pair] = follower
    return (trigrams)

if __name__=="__main__":
    trigrams = build_trigrams(words)
    print(trigrams)


# generating random word combinations
first_word = words[0]+" "
sentence = ""
print(first_word+" ".join(trigrams[random.choice(list(trigrams.keys()))]))
for i in trigrams:
    sentence += " ".join(trigrams[random.choice(list(trigrams.keys()))])+" "
print(first_word+sentence)