#!/usr/bin/env python3
import sys, string, random

# Overall program flow
# 1. Read text
# 2. Process text into individual words and clean up (remove punctuation)
#    Be careful about contractions and proper nouns
# 3. Generate trigrams from text
# 4. Generate new text
#    Randomly insert commas and periods? How often should a quote occur?
#    When to create a new paragraph? Randomly after some number of words generated?
#    When to stop? After some predefined number of words?

def read_data(filename, start_line=None, end_line=None):
    """ Read file and return a sequence of lines with newline characters removed
    Arguments:
    filename -- File to read

    Keyword Arguments:
    start_line -- Optional line to indicate when to start reading lines (default = None)
    end_line -- Optional line to indicate when to stop reading lines (default = None)
    """
    print('Reading \'{}\''.format(filename))
    lines = []
    # Create translator to replace puncuation with whitespace
    translator = str.maketrans('','','\'\"')
    # If start_line supplied, set don't start processing lines until header seen
    process = False if start_line else True
    with open(filename, 'r') as f:
        for line in f:
            # Processing lines
            if process:
                # If end_line supplied, check and break if found
                if end_line and line.startswith(end_line):
                    break
                # Otherwise, remove trailing whitespace/newline characters
                line = line.rstrip()#.translate(translator)
                if line:
                    lines.append(line)
            else:
                # If not processing lines yet, check for start_line
                if line.startswith(start_line):
                    process = True
                    continue
    print('{:d} lines read.'.format(len(lines)))
    return lines

def make_words(lines):
    """ Process sequence of lines from a file, return a sequence of individual words
    Arguments:
    lines -- Sequence of lines from a file (no newline characters)
    """
    words = []
    for line in lines:
        # Split each line by white space
        words.extend(line.split())
    print('{:d} words processed.'.format(len(words)))
    return words

def make_trigrams(words):
    """ Generate dictionary of trigrams given a list of words.
    Arguments:
    words -- Sequence of words from a body of text.
    """
    trigrams = {}
    for i in range(len(words)-2): # Stop processing two words from the end to form a proper trigram
        word_pair = tuple(words[i:i+2])
        next_word = words[i+2]
        # print(word_pair, next_word)
        sequence = trigrams.get(word_pair,[])
        sequence.append(next_word)
        trigrams[word_pair] = sequence
    return trigrams

def start_new_paragraph():
    # Start new paragraph with 25% probability
    return random.randint(1,4) == 1

def return_random_word_pair(word_pairs):
    seed = random.randint(0,len(word_pairs)-1)
    return word_pairs[seed]

def generate_text(trigrams, max_len=1000):
    """ Generate new text from trigram dictionary.
    Arguments:
    trigrams -- Dictionary of trigrams of form key=(word1,word2), value=[words that follow]

    Keyword Arguments:
    max_len -- Length of text (in words) to generate (default=1000)
    """
    new_text = []
    # Create list of keys to index into for cold start
    trigram_keys = list(trigrams.keys())
    # Create list of words to not consider for the end of a paragraph
    ignore_period = ['Mr.','Mrs.','St.','Dr.']
    # Start new text with random word pair
    word_pair = return_random_word_pair(trigram_keys)
    new_text.extend(word_pair)
    # Make sure first word is capitalized
    new_text[0] = new_text[0].capitalize()
    # Continue as long as new text is shorter than desired length
    # Stop once desired length is reached and a complete sentence is written
    while True:
        if word_pair in trigrams:
            # Choose random next word from sequence
            next_word = random.choice(trigrams[word_pair])
            new_text.append(next_word)
            # If last word ends in a period, stop if max length exceeded or
            # start a new paragraph with 25% probability
            if new_text[-1].endswith('.') and new_text[-1] not in ignore_period:
                # If we've exceeded length, stop now
                if len(new_text) >= max_len:
                    break
                else:
                    if start_new_paragraph():
                        new_text.extend(['\n\n'])
                        # Get new random word pair
                        word_pair = return_random_word_pair(trigram_keys)
                        new_text.extend(word_pair)
                        # Make sure first word of new paragraph is capitalized
                        new_text[-2] = new_text[-2].capitalize()
                    else:
                        # If not starting new paragraph, grab last two words for new pair
                        word_pair = tuple(new_text[-2:])
            else:
                # If not starting new paragraph, grab last two words for new pair
                word_pair = tuple(new_text[-2:])
        else:
            # Get new random seed for text
            word_pair = return_random_word_pair(trigram_keys)

    # Create single string from text
    text = ' '.join(new_text)
    # Watch out for cases where new paragraph has extra space
    text = text.replace('\n\n ','\n\n')
    return text

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("A valid file must be included!")
        sys.exit()
    # Process file
    start_line = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_line = "End of the Project Gutenberg EBook"
    # Set header to none while testing short file
    lines = read_data(filename, start_line=start_line, end_line=end_line)
    words = make_words(lines)
    trigrams = make_trigrams(words)
    text = generate_text(trigrams)
    print('\nNew Text:\n')
    print(text)
