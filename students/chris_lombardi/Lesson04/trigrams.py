#UWPCE, PY210
#Lesson04, Trigrams

import random
import string

def build_trigram(words):
    """Build a trigram association from a list of words and return
    the trigram association as a dictionary"""
    trigrams = {}

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        trunc_pair = [remove_punctuation(pair[0]), remove_punctuation(pair[1])]
        follower = words[i + 2]
        trunc_follower = remove_punctuation(follower)
        key_pair = (trunc_pair[0], trunc_pair[1])

        trigrams.setdefault(key_pair,[])
        trigrams[key_pair].append(trunc_follower)

    return trigrams

def trigram_text(trigrams, length_string):
    """Create a new string based on the trigram association."""
    new_text = []
    first_pair = random.choice(list(trigrams.keys()))
    new_text.extend(first_pair)
    avail_words = trigrams.get(first_pair)
    new_text.append(random.choice(trigrams.get(first_pair)))

    for i in range(1,length_string-1):
        next_pair = tuple(new_text[i:i+2])
        #Test for a valid key in the trigram dictionary.
        if trigrams.get(next_pair):
            break
        new_text.append(random.choice(trigrams.get(next_pair)))

    return " ".join(new_text)

def read_data_file(filename):
    """Convert a *.txt file into a string"""
    data_file = ""
    with open(filename, 'r') as f:
        for line in f:
            data_file += line
    return data_file

def remove_punctuation(str1):
    """Remove punctuation from a string"""
    str2 = ''
    for ch in str1:
        if ch not in string.punctuation:
            str2 += ch
    return str2

def make_words(text_string):
    """Create a list of words with punctuation removed"""
    clean_text = remove_punctuation(text_string)
    wrd_grp = clean_text.split()
    return wrd_grp

if __name__ == '__main__':

    data_file = read_data_file('sherlock_small.txt')
    words = make_words(data_file)
    word_pairs = build_trigram(words)
    new_text = trigram_text(word_pairs, len(data_file))
    print(new_text)