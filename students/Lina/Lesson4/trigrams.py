#! python
#------------------------------------------------
# Lesson 4 - Assignment 3: Trigrams
#------------------------------------------------

import sys
import random
import string

def build_text(trigrams):
    #trigrams is a dict that contains word pairs in a tuple and their followers in a list
    #   returns a list with words
    words = []    #contains a list of words (followers) to build the text
    text = ""
    line = ""
    sentence = []

    #Build the words to be used in the text
    next_pair = random.choice(list(trigrams.keys()))          #get a random key (word pair) of a dict to start
    words.extend(next_pair)                                   #add first pair to the list, pair is a tuple
    while True:
        if next_pair not in trigrams:
            break
        words.append(random.choice(trigrams.get(next_pair)))  #get random value (follower) of a key (word pair)
        next_pair = tuple(words[-2:])                         #next pair is the last two words of the list
    #Now form a text:
    #  allow up to 60 characters per line (might be a little over)
    #  put a period to end a sentence in evey 6 to 12 words
    #  capitalize the first word of a sentence
    words_processed = 0
    start_pos = 0                                          #start_pos and end_pos are used to navigate the words[]
    end_pos = 0 
    while words_processed < len(words):
        words_per_sentence = random.randint(6, 12)         #randomly get number of words for next sentence
        end_pos += words_per_sentence
        sentence = words[start_pos].capitalize().split()+words[start_pos+1:end_pos]  #capitalize the first word of a sentence, use split() to put back to a list
        for word in sentence:
            if (len(word) + len(line)) > 60:               #check if this word may cause the line to exceed the max number of characters per line
                text += line+"\n"                          #end the current line
                line = ""                                  #start a new line
            line += word + " "
        line = line.rstrip() + ". "              #remove the space after the last word of a sentence before adding a period
        words_processed += words_per_sentence    #last set of words can be shorter than 'words_per_sentence' but it should not affect the looping
        start_pos = end_pos
    text += line       #last line
    return text

def build_trigrams(words):
    #words is a list of words, build up the trigrams dict from the words.
    #  returns a dict with:
    #   keys: a tuple of word pairs
    #   values: list of followers
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams

def clean_up_data(data):
    #data is a string, any special characters defined in the list and any punctuations
    #will be removed except apostrophe in word like "can't". All letters will be lower
    #case, except "I" if used a pronoun (or by itself).
    #  returns a string
    special_chars = {"\n" : " ", "\r" : " "}             #reserve a space so it does not combine with next word
    data = data.translate(str.maketrans(special_chars))  #replace characters in special_chars
    punct = string.punctuation
    punct = punct.replace("'", "")                       #exclude single quote here so that word like "can't" will not split inadvertenly
    data = data.translate(str.maketrans(punct, ' '*len(punct)))  #map punctuation to space
    data = data.lower()

    words = data.split()
    new_data = []
    for word in words:
        if word == "i": word = "I"
        if word.count("'") > 1:
            word = word.replace("'", "")
        new_data.append(word)
    return " ".join(new_data)

def make_words(data):
    #data is a string that contains many sentences.
    #  returns a list with words only
    return clean_up_data(data).split()


def read_in_lines(filename):
    #Read in a file and append each input line to a string.
    #  returns a string with lines in the input file
    in_data = ""
    with open(filename, 'r') as in_file:
         while True:
            line = in_file.readline()
            if not line:
                break
            in_data += (line)
    return in_data



if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_lines(filename)
    words = make_words(in_data)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)

    print(new_text)
