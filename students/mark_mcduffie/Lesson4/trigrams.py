'''
Mark McDuffie
5/3/20
Lesson 4 Assignment 3
Trigrams
'''
import sys
import random
'''
Reads all the data in a file and returns a text that 
Trigrams can work with
'''
def read_in_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            text = f.read()
    f.close()
    text = text.lower()
    text = text.split()
    return text

words = "I wish I may I wish I might I wish I may".split()

def make_words(text):
    words_list = []
    with open(filename, 'r') as lines:
        for line in lines:
            # removes hyphens, quotes, commas,and apostrophes
            line = line.replace('-', ' ')
            line = line.replace('"', '')
            line = line.replace(',', '')
            line = line.replace("'", '')
            line = line.strip()
            for word in line.split():
                word = word.lower()
                # returns the lowercase string and adds it to our words list
                words_list.append(word)
    # return words list
    return words_list

'''
Builds the trigram dict
'''
def build_trigram(words):
    trigrams = {}
    for i in range(len(words)-2):
        wordPair = words[i:i+2]
        nextWord = words[i+2]
        key = tuple(wordPair)
        if(key in trigrams.keys()):
            trigrams[key].append(nextWord)
        else:
            trigrams[key] = [nextWord]
    return trigrams

'''
Builds a text based on what is stored in the dict
'''
def build_text(trigrams, n):
    final_story = ""
    key = random.choice(list(trigrams.keys()))
    new_text = list(key)
    try:
        for i in range(n):
            nextWord = (trigrams[key][random.randint(0,(len(trigrams[key]) - 1))])
            new_text.append(nextWord)
            key = tuple(new_text[-2:])
    except KeyError: #Happens when the new key does not have text to follow
        print("No new value stored")
    story = " ".join(new_text)
    story = story.split(".")
    for item in story:
        final_story += (item[0].capitalize() + item[1:] + ".")
    return final_story

#Main Method
if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = "sherlock.txt"
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    #constant for how many words the user wants
    n = 100
    text = read_in_data(filename)
    words = make_words(text)
    trigrams = build_trigram(words)
    new_text = build_text(trigrams, n)

    print(new_text)