import random
import sys

DEBUG = False

#Notes on cleaning text:
#Punctuation informs grammer,
#leaving in capitalization, commas, and periods helps keep sentance structure
#to allow more randomness, i'm going to seperate commas and periods into their own words for the trigram and rejoin them at the end
#parentheses and quotes come in pairs, I don't want to deal with that so I'm going to remove them entirely
remove = str.maketrans("","",'(){}[]"'+"'")
add_space = str.maketrans({',' : ' ,', '.' : ' .'})            


def is_punctuation(string):
    """detects if a string is punctuation"""
    return len(string) <= 1 and not string.isalnum()

def read_data(filename = "", header = True):
    """Processes data from a text file and returns a list of all words it contains
    header : True if there is a header that needs skipping"""
    if filename == "":
        return "I wish I may I wish I might".split()
    with open(filename) as file:
        text = []
        for line in file:
            if header:
                #Find START OF PROJECT line, otherwise do nothing
                #I'm choosing to not hold myself responsible for the Table of Contents or similar
                if line.startswith('***'):
                    header = False
            else:
                line = line.translate(remove)
                line = line.translate(add_space)
                text.extend(line.split())
    if DEBUG: print(text)
    #if header is still True, no text has been captured.  Try again
    if header: text = read_data(filename, False)
    return text
    
def build_trigrams(words):
    """Builds a trigram from a list of words"""
    """Trigram is a dictionary of lists, using a word pair tuple as a key"""
    trigram = {}
    for i in range(len(words)-2):
        trigram.setdefault((words[i], words[i+1]), []).append(words[i+2])
    if DEBUG: print(trigram)
    return trigram

def generate_text(trigram):
    #Insure first key is capitalized, hope it's the begining of a sentance
    key = "a"
    while not key[0].istitle():
        key = random.choice(list(trigram))
    if is_punctuation(key[1]):
        new_text = [key[0] + key[1]]
    else:
        new_text = list(key)
    if DEBUG: print(f"starting key: {key}")
    #generate text
    for i in range(400):
        next_word = random.choice(trigram[key])
        key = (key[1], next_word)
        #rejoin punctuation into the text
        if is_punctuation(next_word):
            new_text[-1] = new_text[-1] + next_word
        else:
            new_text.append(next_word)
        #if the key is not in the trigram, it apears at the end of the sample
        #most likely it is the natural place to end the text
        if key not in trigram: break
    return new_text

if __name__ == "__main__":
    #get the filename from the command line, allow for default condition
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = ""
    #build the trigram
    if DEBUG: print(f"filename: {filename}")
    words = read_data(filename)
    trigram = build_trigrams(words)
    new_text = generate_text(trigram)        
    print(" ".join(new_text))