import sys
import string
import re
import random


def read_data(filename): 
    with open(filename, 'r') as f:
        output = f.read()
    f.close()
    output = output.lower()
    '''replaces tabs and indents'''
    whitespace = dict.fromkeys('\r\n\t', ' ')
    '''replaces the indentation'''
    punctuation = dict.fromkeys(string.punctuation, ' ')
    output = output.translate(output.maketrans(whitespace))
    output = output.translate(output.maketrans(punctuation))
    output = output.split()
    return output


def build_trigram(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i+2]
		if pair not in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair].append(follower)
    return trigrams



def build_text(dict_of_trigrams):
    new_text = []
    n = len(dict_of_trigrams.keys())
    for i in range(150):
        random_number = random.randint(0,n-1)
        key = list(dict_of_trigrams.keys())[random_number]
        new_text.append(" ".join(list(key)))
        new_text.append(" ".join(dict_of_trigrams[key]))
    return (" ".join(new_text))	

	
	


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_data(filename)
    word_pairs = build_trigram(in_data)
    new_text = build_text(word_pairs)

    print(new_text)