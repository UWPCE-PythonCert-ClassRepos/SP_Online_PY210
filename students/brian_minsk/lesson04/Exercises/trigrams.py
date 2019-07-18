# Author: Brian Minsk

import random
import pathlib

# This subclasses dict to make the logic simple if trying to add to the value list when the key doesn't already exist.
# To add a value for a key that does already exist in the simply state the new key with an 'append' with the value
# e.g. dt[("word1", "word2")].append("word3") will work even when the ("word1", "word2") key doesn't already exist.
class DictTrigram(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

def get_filename():
    # get the filename from the command line
    
    print("Files in the current directory:")
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(f)
    
    while True:
        filename = pathlib.Path(input("Type a file name: "))
        if filename.is_file():
            break
        else:
            print("Not a valid file path/name.")
    return filename

def get_text(filename):
    lines = []
    with open(filename, "r", encoding='utf8', errors='ignore') as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    return " ".join(lines)  

def parse_words(full_text):
    """
    Leave punctuation next to words with words for now as it usually denotes phrase and/or sentence ending.
    Future: Treat contiguous punctuation as seperate 'words'.
    """
    return full_text.split()    

def build_trigrams(words):
    trigrams = DictTrigram()
    #iterate the words but, since we are looking at three words at a time, make sure we don't go past the end
    words_len = len(words)
    for i, word1 in enumerate(words):
        if i == words_len - 2: #don't go further
            break
        word2 = words[i + 1]
        word3 = words[i + 2]
        trigrams[(word1, word2)].append(word3)
    return trigrams

def build_text(trigrams, num_iterations=100):
    new_text_list = []

    first_two = choose_start(trigrams)    
    first_word = first_two[0]
    new_text_list.append(first_word)
    second_word = first_two[1]
    new_text_list.append(second_word)
    
    chain_on_third_word(trigrams, first_word, second_word, new_text_list, 0, num_iterations)
    return " ".join(new_text_list)

def chain_on_third_word(trigrams, first_word, second_word, text_list, i=0, num_iterations=100):
    if i == num_iterations:
        return
    if not (first_word, second_word) in trigrams:
        first_two = choose_start(trigrams)
        first_word = first_two[0]
        text_list.append(first_word)
        second_word = first_two[1]
        text_list.append(second_word)
    i += 1
    third_word_list = trigrams[(first_word, second_word)]
    third_word = random.choice(third_word_list)
    text_list.append(third_word)
    chain_on_third_word(trigrams, second_word, third_word, text_list, i, num_iterations)

def choose_start(trigrams):
    return random.choice(list(trigrams.keys()))

if __name__ == "__main__":
    
    #filename = "sherlock.txt"

    filename = get_filename()
    full_text = get_text(filename)
    words = parse_words(full_text)
    trigrams = build_trigrams(words, get_num_iterations())
    new_text = build_text(trigrams)

    print(new_text)