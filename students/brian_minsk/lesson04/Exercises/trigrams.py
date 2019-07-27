# Author: Brian Minsk

import random
import pathlib

class DictTrigram(dict):
    """ Subclasses dict to make the logic simple if trying to add to the value list when the key doesn't already exist.
    Allow an 'append' with the value for a key that does already exist.
    e.g. dt[("word1", "word2")].append("word3") works even when the ("word1", "word2") key doesn't already exist.
    """
    def __missing__(self, key):
        self[key] = []
        return self[key]

def get_filename():
    """ Show the files in the current directory and get file name from the command line
    """    
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

def get_num_iterations():
    while True:
        iteration_input = input("How many trigrams to use to build the text? ")
        num_iterations = 0
        try:
            num_iterations = int(iteration_input)
            return num_iterations
        except:
            print("Please type an integer.")

def get_text(filename):
    """ Open a text file, stripping out any whitespace/non-printing characters on the right of each line, append the lines to
    a list, and return a string with all the text. Also, test to see if text is from Project Gutenberg and, if so, remove the
    header and footer text.

    Keyword arguments:
    filename - name of the file to read
    """
    lines = []
    with open(filename, "r", encoding='utf8', errors='ignore') as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    cleaned_lines = degutenbergerator(lines)
    return " ".join(cleaned_lines)  

def degutenbergerator(lines):
    """ Remove the Gutenberg header and footer, if found, and return the result

    Keyword arguments:
    lines - a list of strings (lines from a text file)
    """
    for i, line in enumerate(lines):
        if "*** START OF THIS PROJECT GUTENBERG" in line:
            lines = lines[(i + 1):]
            break
    for i, line in enumerate(lines):
        if "*** END OF THIS PROJECT GUTENBERG" in line or "End of Project Gutenberg" in line:
            lines = lines[:i]
            break
    print(lines)
    return lines
            
def parse_words(full_text):
    """ Create a list from a string with each element a string seperated by whitespace.
    Leave punctuation next to words with words for now as it usually denotes a natural phrase and/or sentence ending.
    Future: Treat contiguous punctuation as seperate 'words'.

    Keyword arguments:
    full_text - string to parse
    """
    return full_text.split()    

def build_trigrams(words):
    """ Create all the trigram structures from a list of strings, with each structure as a tuple of the one word and the next
    word, followed by a list of the following word for everywhere the first two words appear next to each other (in the orginal order)
    from the input list. e.g. (word1, word2):[word3a, word3b, word3c, ...]. Put all these trigram structures in a dict and return the  dict.

    Keyword arguments:
    words - list of strings
    """
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
    """ Build text three words at a time from a dictionary of trigram structures 
    - e.g. (word1, word2):[word3a, word3b, word3c, ...] - by randomly choosing the first two words to start a recursive
    function that chooses the trigrams and adds to the text.
    Return the resulting text.

    Keyword arguments:
    trigrams - dictionary of trigrams of the form (word1, word2):[word3a, word3b, word3c, ...]
    num_iterations - number of times to recursively call the chain_on_third_word function. More iterations creates longer text.
    """
    new_text_list = []

    first_two = choose_start(trigrams)    
    first_word = first_two[0]
    new_text_list.append(first_word)
    second_word = first_two[1]
    new_text_list.append(second_word)
    
    chain_on_third_word(trigrams, first_word, second_word, new_text_list, 0, num_iterations)
    return " ".join(new_text_list)

def chain_on_third_word(trigrams, first_word, second_word, text_list, i=0, num_iterations=100):
    """ Randomly choose the third word from a trigram structure given two consecutive words in order. 
    If the two consecutive words are not found then get a randomly choosen pair to get the third word.
    Add the third word onto the string being built then recurse, but now with the second word as the first
    word and the third word as the second.

    Keyword arguments:
    trigrams - dictionary of trigrams of the form (word1, word2):[word3a, word3b, word3c, ...]
    first_word - string that is the first word of a trigram structure
    second_word - string that is the second word of a trigram structure
    text_list - list of the strings with the text that is being created
    i - tracks the number of times chain_on_third_word has been called.
    num_iterations - number of times to recursively call the chain_on_third_word function. More iterations creates longer text.
    """
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
    """ Return a random pair of the first & second word (i.e. the list that is a key in a trigram structure).
    Only return a pair where the first word is capatilized to try to make sure we start sentences with a capatital.
    """
    while True:
        first_two = random.choice(list(trigrams.keys()))
        if first_two[0].istitle():
            return first_two

if __name__ == "__main__":
    """ Create and print text from a text file using a trigram methodology explained at 
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/kata_fourteen.html
    """    
    filename = get_filename()
    full_text = get_text(filename)
    words = parse_words(full_text)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams, get_num_iterations())
    print(new_text)