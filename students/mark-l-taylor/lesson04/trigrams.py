#!/usr/bin/env python3

''' Trigram Assignment 3 from Lesson 04'''

import sys, random, string

#words = "I wish I may I wish I might".split()

def read_in_data(filename, start, end):
    '''Reads in data and returns the lines from the source'''
    lines = []
    with open(filename, 'r') as f:
        read_lines = False
        for line in f:
            if read_lines:
                if line.startswith(end):
                    #End line found, stop processing lines
                    break
                else:
                    #Otherwise add the line to the list, include rstrip to remove carriage returns
                    line = line.rstrip()
                    if line:
                        #Only add if line is not empty
                        lines.append(line)
            elif line.startswith(start):
                read_lines = True
    print(f'Read in {len(lines)} from {filename}')
    return lines            

def make_words(lines):
    '''Return a list of words from the lines'''
    words = []
    for line in lines:
        #Remove the punctuation characters from the line
        line = line.translate(str.maketrans('', '', string.punctuation))
        words.extend(line.split(' '))
    print(f'Processed {len(words)} words')
    return words

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
        follower = words[i + 2]
        seq = trigrams.get(pair,[])
        seq.append(follower)
        trigrams[pair] = seq
    return trigrams

def random_key(dictionary):
    '''Returns a random key from the dictionary'''
    return random.choice(list(dictionary.keys()))
      
def build_sentence(tri_dict, sent_len):
    ''' Return a sentance built from a trigram.  Sentance will be limited to length'''
    word_pair = random_key(tri_dict)
    print(sent_len)
    
    #begin by adding the random starting word_pair to new_sent
    new_sent = list(word_pair)
    
    #loop through adding words from trigram to build a sentence.
    while len(new_sent) < sent_len:
        if word_pair in tri_dict:
            #Get a random word from the value of the word_pair and append to new_sent
            new_sent.append(random.choice(tri_dict[word_pair]))
            #Determine the next word pair make into tuple to lookup in dictionary
            word_pair = tuple(new_sent[-2:])
        else:
            #new word pair is not in list, get a new word pair and continue looping.
            word_pair = random_key(tri_dict)
    
    #Return the sentance to the input length
    new_sent = new_sent[0:sent_len]
    #Capitalize the first word
    new_sent[0] = new_sent[0].capitalize()
    #Add period to last word
    new_sent[-1] = new_sent[-1] + '.  '
    
    return ' '.join(new_sent)

def build_text(tri_dict):
    ''' Create text based on the trigram dictionary'''
    new_text = []
    num_para = random.randint(3,6)
    for i in range(1, num_para):
        num_sent = random.randint(3,12)
        for j in range(1, num_sent):
            new_text.append(build_sentence(word_pairs, random.randint(8,30)))
            j =+ 1
        new_text.extend(['\n\n'])
        i =+ 1
    
    return ' '.join(new_text)
        
    

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    header = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    end_line = '*** END OF THIS PROJECT GUTENBERG EBOOK'
    in_data = read_in_data(filename, header, end_line)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)   
        
        
    