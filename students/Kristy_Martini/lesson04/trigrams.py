import os
import random
import string
import sys
sys.setrecursionlimit(1000)

def load_file(file, header=False): 
    with open(file, 'r', newline='', encoding='UTF-8') as f: 
        words = list()
        if header is None:
            header = True
        for line in f.readlines():
            if True:
                if(line != '\r\n'):
                    line_words = line.split()
                    for word in line_words:
                        words.append(word)
            if line.startswith("***"):
                header = not header
        return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    exceptions = ["I", "God"]
    exclude = set(string.punctuation)
    for word in words:
        if word not in exceptions or not word.istitle():
            word.lower()
        word = ''.join(ch for ch in word if ch not in exclude)

    trigrams = dict()
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = list()
            trigrams[pair].append(follower)
    return trigrams

def create_book(trigrams):
    book = " ".join(random.choice(list(trigrams.keys())))
    add_to_book(trigrams, book)

def add_to_book(trigrams, book):
    book_split = book.split()
    book_length = len(book_split)
    if book_length > 500:
        print(book)
        return book
    else:
        pair = (book_split[len(book_split)-2], book_split[len(book_split)-1])
        if pair in trigrams:
            if len(trigrams[pair]) == 1:
                addition = trigrams[pair][0]
            else:
                addition = random.choice(list(trigrams[pair]))
            book = book + " " + addition
            add_to_book(trigrams, book)
        else:
            print(book)
            return book

if __name__ == "__main__":
    #words = "I wish I may I wish I might".split()
    filepath = os.path.join(os.getcwd(), "sherlock.txt")
    words = load_file(filepath, header=True)
    trigrams = build_trigrams(words)
    create_book(trigrams)
