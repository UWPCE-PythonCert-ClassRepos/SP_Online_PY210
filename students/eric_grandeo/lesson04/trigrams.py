#!/usr/bin/env python3

import random
import string


test_list = []

with open('sherlock.txt', 'r') as f:
    count = 0
    story = False

    for line in f:
        #print(line)

        #make start and end sentences a variable
        if "*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***" in line:
            story = True
        elif "*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***" in line:
            story = False

        if story is True:
            test_list.extend(line.split())

new_text = " ".join(test_list)

def strip_punc(words):
    #excluding apostrophes from the punctuation removal
    updated_punc = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
    new_words = words.replace('-', ' ')
    new_words = new_words.translate(str.maketrans('', '', updated_punc)).replace('\n',' ')
    return new_words



def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    # build up the dict here!
    trigrams = {}
    for word in range(len(words)-2):
        pair = tuple(words[word:word+2])
        follower = words[word+2]
        #print(pair,follower)

        trigrams.setdefault(pair,[]).append(follower)

    return trigrams

def rand_choice(trigram_dict):
    #random selection from the trigram dict to start the generated text
    return random.choice(list(trigram_dict.keys()))

def rand_num_sent():
    #randomly choose the number of sentences in a paragraph
    return random.randrange(5, 10)

def num_words_sent():
    #randomly choose the number of words in a sentence
    return random.randrange(10, 20)

def make_sent_para(text_list):
    #using num_words_sent and rand_num_sent, create paragraphs from the generated text
    new_word_list = []
    temp_list = []
    words = num_words_sent()
    #create a list of sentences with rand number of words in it
    for i in range(len(text_list)):
        temp_list.append(text_list[i])
        if i == words:
            new_word_list.append(temp_list)
            temp_list = []
            words = num_words_sent() + i

    another_list = []
    another_temp_list = []

    #create a random list of paragraphs from the previous list
    sentences = rand_num_sent()
    for i in range(len(new_word_list)):
        line = " ".join(new_word_list[i]).capitalize() + "."
        another_temp_list.append(line)
        if i == sentences:
            another_list.append(another_temp_list)
            another_temp_list = []
            sentences = rand_num_sent() + i

    the_final_list = []
    for j in another_list:
        the_final_list.append(" ".join(j))

    return "\r\n\r\n".join(the_final_list)

#function to create the new text
def build_text(trigram_dict, words):
    #create empty list
    new_text = []

    #randomly select key
    rand_start = rand_choice(trigram_dict)

    #add randomly selected key to new list
    for i in rand_start:
        new_text.append(i)

    #create text based on number of max words
    while len(new_text) < words:
        new_word = trigram_dict.get(tuple(new_text[len(new_text)-2:]),[])

        #if not in trigram dict, then select a new random key
        if new_word == []:
            rand_start = rand_choice(trigram_dict)
            for i in rand_start:
                new_text.append(i)
                continue

        #if the new_word has more than one value, randomly choose one
        elif len(new_word)>1:
            select_word = random.choice(new_word)
            new_text.append(select_word)
        else:
            new_text.extend(new_word)

    return make_sent_para(new_text)

'''
To generate new text from this analysis, choose an arbitrary word pair
as a starting point. Use this pair of words to look up a random next word
(using the table above) and append this new word to the text so far.
This now gives you three words with a new word pair (second and third words)
at the end of the three-word text. Look up a potential next word based
on this pair. This generates another pair to add to the list, and so on.
'''


if __name__ == "__main__":
    strip_text = strip_punc(new_text)
    trigrams = build_trigrams(strip_text.split())
    rand_start = rand_choice(trigrams)
    new_text = build_text(trigrams, 2000)
    print(new_text)
