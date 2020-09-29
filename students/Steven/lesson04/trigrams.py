#! bin/user/env python3
import random

words = "I wish I may I wish I might".split()  # a list

filename = r"C:\Users\smar8\PycharmProjects\Python210\lesson04\sherlock_small.txt"

def build_trigrams(words):
    trigrams = {}
    # build up the dict here!
    for word in range(len(words)-2):  # stops with the last two words in the list
        pair = (words[word], words[word+1])  # Pair of words stored in a tuple
        follower = words[word+2]  # set the 3 word
        trigrams.setdefault(pair, []).append(follower)
        # print(trigrams)
    return trigrams

#  creating the words list from a file
def make_words(file):
    with open(file, 'r') as fh:
        # for line in fh:
        text = fh.read()
    punc = ('.', ',', '!', '?', '-', "'", '(', ')')
    for word in text:
        if word in punc:
            text = text.replace(word, ' ')  # remove punctuation from the file
    text = text.split()
    # print(text)
    return text

def build_text(db, n):  # params of word list and number of words to read
    book = ""
    key = random.choice(list(db.keys()))  # select a random key from the sequence
    temp = list(key)
    for number in range(n):
        nextWord = (db[key][random.randint(0, (len(db[key]) - 1))])  # select the value of the key pair from a random number based on the length of the keys of input seq
        temp.append(nextWord)
        key = tuple(temp[-2:])
    story = " ".join(temp)  # combine all the words
    story = story.split(".")  # Split each line when there is a period
    for item in story:
        book += (item[0].capitalize() + item[1:] + ".")  # Make each sentence start with a capital letter and end with a period
    return book

if __name__ == "__main__":
    filename = r"C:\Users\smar8\PycharmProjects\Python210\lesson04\sherlock_small.txt"
    n = 10  # number of key pairs of words to read from the file
    words = make_words(filename)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams, n)
    print(new_text)