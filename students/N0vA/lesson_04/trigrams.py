#!/usr/bin/env python3

# Import modules
import sys
import random
import re
import string

# Set up global items to run in functions
trigrams = {} # Key of trigrams will be two words with value as follower
lines = list() # This will be lines of the text file that is read in
words = [] # This will be a list of all words in the story
my_start = ('I', 'once') # start of the new story
story_length = 2000 # So story doesn't go on forever
story = ''
filename = 'sherlock.txt' # File to use


def read_in_file(filename): # Read in file to get lines -> word list

    # Read in and clean
    header = ('*** START OF THIS PROJECT GUTENBERG EBOOK')
    ending = ('End of the Project Gutenberg EBook')
    puncuation_marks = str.maketrans('.,?!();', '       ')
    with open(filename, 'r') as infile:

        # Skip past header
        for line in infile:
            if line.find(header) != -1:
                break

        # Remove punctuation
        for line in infile:
            if line.isspace():
                continue
            elif line.find(ending) != -1:
                break
            else:
                line = line.translate(puncuation_marks)
                line = line.replace('--', ' ')
                line = line.replace('"', '')
                line = line.strip()
                # can these two replace lines be written as one - I couldn't do it
                lines.append(line.lower())

        return lines


def make_words(lines): # Create list of words that will go into creating trigram

    # Split words
    for line in lines:
        line = line.split()
        for word in line:
            words.append(word)

    return words

def capital_i(words): # Make 'i' capital
    
    for x, y in enumerate(words):
        if y == "i":
            words[x] = "I"

    return words


def build_trigrams(words): # Build trigrams from words list
    
    # Make trigrams
    for w in range(len(words)-2):
        pair = words[w:w + 2]
        key = tuple(pair)
        follower = (words[w + 2])
        
        # Add new keys and append existing ones to create trigrams dictionary
        if key not in trigrams.keys():
            trigrams[key] = [follower]
        else:
            trigrams[key].append(follower)
        
    return trigrams


def write_story(trigrams): # Write a short story using the trigrams method
    
    line_break = 75
    word_count = 1

    # Open file to write
    with open('short_story.txt', 'w') as outfile:

        # Make strings to continuously add to the story
        paired_words = my_start
        story = paired_words[0] + ' ' + paired_words[1]

        while paired_words in trigrams.keys() and len(story) <  story_length:
            new_word = random.choice(trigrams[paired_words])
            
            # Add new word to the story
            story = story + ' ' + new_word

            # Reassign to overwrite and find next word
            paired_words = paired_words[1], new_word

        # Line breaks -- I had to look this up online to make carriage returns
        # Could not get it to not split words
        for word in story:
            if word_count == line_break:
                outfile.write(word.strip('\n') + "\n")
                word_count = 0
            else:
                outfile.write(word.strip('\n') + "")

            word_count += 1


# Run script
if __name__ == "__main__":

    lines = read_in_file(filename)
    words = make_words(lines)
    words = capital_i(words)
    trigrams = build_trigrams(words)
    story = write_story(trigrams)

    print(story)