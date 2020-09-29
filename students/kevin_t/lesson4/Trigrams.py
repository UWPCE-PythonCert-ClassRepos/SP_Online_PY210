#!/usr/bin/env python3
import random

#Function to open the file
def read_in_data(filename):
    return open(filename, 'r')

#Function to return words in order
def make_words(in_data):
    lines = in_data.readlines()
    in_replace = '-,().!?"'
    out_replace = '        '
    #Declare a list to add words to
    words = []
    for line in lines:
        #Remove carriage returns
        line = line.strip('\n')
        #Replace punctuation with spaces
        line = (str(line)).translate(str.maketrans(in_replace,out_replace))
        #Split strings by spaces
        line = line.split()
        #Add each word into one long list
        for word in line:
            words.append(word)
    return words

def build_trigram(words):
    #Declare a dictionary
    tridict = {}

    #Iterate across all available words (minus 2)
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        #Set the two key words to result in the following word as a value
        #If key already exists, add the value as an option.
        if pair in tridict.keys():
            tridict[pair].append(follower)
        else:
            tridict[pair] = [follower]

    return tridict

def build_text(word_pairs):
    #Declare a new list
    new_text = []
    #Each item in the list will be a list of lists that represents sentences
    for sentence in range(100):
        #Randomly select the first two words from keys in the dictionary
        first = random.choice(list(word_pairs.keys()))
        new_text.append([first[0], first[1]])
        i = 0
        while True:
            #Randomly select a value from the given keys.
            #Loop until there is no matching key in the dictionary
            #Or the sentence is 30 words long.
            if (new_text[sentence][i], new_text[sentence][i+1]) in word_pairs.keys() and i <= 30:
                new_text[sentence].append(random.choice(word_pairs[(new_text[sentence][i], new_text[sentence][i+1])]))
                i = i + 1
            else:
                #If no matching key or longer than 30 words, end the sentence.
                #Add a carriage return for formatting.
                new_text[sentence].append('.\n')
                new_text[sentence] = ' '.join(new_text[sentence])
                break

    return new_text

def write_txt(new_text):
    #Write the story into a new file.
    new_filename = input('What is the file name?')
    with open(new_filename + '.txt', 'w') as f:
        f.write(' '.join(new_text))

if __name__ == "__main__":
    # get the filename from the command line
    filename = input('What is the filename of the source text?') + '.txt'
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)
    write_txt(new_text)