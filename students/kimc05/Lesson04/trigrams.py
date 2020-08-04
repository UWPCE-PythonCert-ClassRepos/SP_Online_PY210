#!/usr/bin/env python3
#Trigrams - Simple Text Manipulation
#Christine Kim
import random
import string

remove = '!#"$%&()*+,\-./:;<=>?@[]^_`{|}~'
cap = set(["i", "i'll", "i've", "mr.", "mrs.", "ms."])

#Take in reference file and remove all punctuation except apostrophe
def file_read():
    f_name = input("Enter File name: ")
    with open(f"{f_name}", "r") as f:
    return f.read().translate(str.maketrans(remove, " " * len(remove)))

#Separate words
def reference(f_in):
    return f_in.split()

#Create dictionary of triagram keys and populate it
#{String: [list or tuple]}
def populate_dict(words):
    length = len(words)
    triagram = {}
    #iterate through read file
    for i in range (length-2):
        #read key
        key = (words[i], words[i+1])
        #new key
        if key not in triagram:
            #add item to dict
            triagram[key] = [words[i+2]]
        else:
            #add to existing item in dict
            triagram[key] = triagram.get(key) + [words[i+2]]
    return triagram

#generate a random text paragraph based on dict
def paragraph_write(triagram):
    #create paragraph list
    paragraph = []    
    #decide length of a paragraph. average number of sentences in paragraph 6
    for j in range(random.randint(1,7)):
        
        #initiate random sentence start
        line = list(random.choice(list(triagram)))
        
        #decide length of a sentence. average number of words in sentence 20
        for i in range (random.randint(2, 21)):
            #terminate printing if last pair of words is not in dict
            if (line[-2], line[-1]) not in triagram:
                i = 22
            else:
                #add randomized value to list of words
                line += [random.choice(triagram.get((line[-2], line[-1])))]
        
        #add sentences to paragraph
        paragraph += [punctuate(" ".join(line))]   
    print(" ".join(paragraph))
    print("\n")

#add punctuation to end of the sentence
def punctuate(line):
    end = ("?", "!", ".")
    return "{}{}".format(line, random.choice(end)).capitalize()

if __name__ == "__main__":
    f_data = file_read()
    words = reference(f_data)
    #print(words)
    triagram = populate_dict(words)
    #print(triagram)
    paragraph_write(triagram)