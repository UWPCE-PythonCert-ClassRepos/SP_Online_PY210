#Trigram part
import sys, random, string

def build_trigram(words):
    #Start an empty dictionary
    Trigrams = {}
    #Iterate through every word and create 2 word pair keys
    for i in range(len(words)-2):
        #2 word pair key
        Key = (words[i], words[i+1])
        #value is the follower word
        Value = words[i+2]
        #If key exists, append the list of values, otherwise start a new list and append with value
        Trigrams.setdefault(Key,[]).append(Value)
    #print(Trigrams)
    return Trigrams

def read_in_data(book):
    #read input book and format it for use in trigrams   
    with open(book, 'r') as f:
        #create a list containing the text lines of the input file
        Lines = f.readlines()
        
        #define the header and footer
        header = '*** START OF THIS PROJECT GUTENBERG EBOOK MATCHMAKER ***'
        footer = 'End of the Project Gutenberg EBook'
        #set start and end as full book if header, footer aren't present
        start = 0
        finish = len(Lines)
        for i in range(len(Lines)):
            #define the first line after the header
            if Lines[i] is header:
                start = i + 1
            #define the last line before the footer    
            elif Lines[i].startswith(footer):
                finish = i
            else: pass       
    return Lines[start:finish]


def make_words(lines):
    #set map for each punctuation to ""
    trans = str.maketrans(string.punctuation,len(string.punctuation)*" ")
    #open an empty list
    words = []
    for line in lines:
        #strip punctuation from input text
        line = line.translate(trans)
        #remove trailing whitespace on the right of the string
        line = line.rstrip()
        #create a list of words from the line
        word_list = line.split()
        for word in word_list:
            if word is "I":
                words.append(word)
            else:
                words.append(word.lower())
    return words    

def build_text(trigrams):
    #pick a random word pair to start with
    word_pair = random.choice(list(trigrams.keys()))
    print(word_pair)
    #create an empty list to dump new text into
    new_text = []
    first,second = word_pair
    new_text.append(first.title())
    new_text.append(second)
    while len(new_text) < 100:
        if word_pair in list(trigrams.keys()):
            first, second = word_pair
            new_word = trigrams[word_pair]
            new_text.append(new_word[0])
            word_pair = (second,new_word[0])
        else:
            new_text.append(".")
            word_pair = random.choice(list(trigrams.keys()))
    writing = " ".join(new_text)
    return writing

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)