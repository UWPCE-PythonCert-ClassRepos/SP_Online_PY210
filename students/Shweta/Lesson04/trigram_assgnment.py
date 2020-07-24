#!/usr/bin/env python
import random
import sys
import string
import pathlib

#words = "I wish I may I wish I might".split()

#######build_text function###################

def build_text(word_pairs):
    nword=[]

    spair=random.choice(list(word_pairs))
    nword=(list(spair))
    nvalue=random.choice(word_pairs[spair])

    nword.append(nvalue)
    for x in range(20):
        npair=tuple(nword[-2:])
        if npair in word_pairs:
            nword.append(list(npair)[0])
            nword.append(list(npair)[1])
            nvalue=random.choice(word_pairs[npair])
            nword.append(nvalue)
        else:
            return " ".join(nword)
    return " ".join(nword)
        

####################Trigram Build##############
def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2): 
        pair = words[i:i + 2]
        follower = words[i + 2]
        tpair = tuple(pair)
        trigrams.setdefault(tpair,[]).append(follower)
    return trigrams

########Cleaning of the data#####################
### *** START OF THIS PROJECT GUTENBERG EBOOK
def make_words(in_data):
    words=[]
    for line in in_data:
            line=line.replace('--',' ')
            line=line.replace('-',' ')
            line=line.replace('<',' ')
            line=line.replace('>',' ')
            line=line.replace('!',' ')
            line=line.replace('@',' ')
            line=line.replace('#',' ')
            line=line.replace('"','')
            line=line.replace(',','')
            line=line.replace('(','')
            line=line.replace(')','')
            line=line.strip()
            for word in line.split():
                words.append(word.lower())
    #print(words)
    return words



################read_in_data function############

def read_in_data(filename):
    '''function to read lines for the file passed for trigram , this will convert all the words from file
       into lower case word'''
    nword=" "
    source=pathlib.Path.home() / filename
    with open(str(source),'r') as infile:
        for line in infile.readlines():
             for word in line.split():
                 nword+=" " + word
          #       nword=nword.translate({ord(i):None for i in '-.:<>!@#$%^&*()_+=,/?"'})##(this would have worked for make_words function
    return nword.lower().split()

#########if __name == "__main__" Block###########

if __name__ == "__main__":
     # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)  
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)

    
