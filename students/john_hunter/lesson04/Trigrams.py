#!/usr/bin/env python3
"""
Created on Sat Nov 28 15:56:27 2020

@author: johnh
"""

#trigrams

import random
import re


def read_in_data(filename):
    """
    Gets the file name from the user and returns the text in a list from the file
    """
    file = open(filename, "r")
    text = []
    for line in file:
        line = line.strip('\n')
        line = re.sub(r'[^\w\s]',' ', line)
        for word in line.split():
            text.append(word.lower())

    return text

def build_tri_dict(text):
    """
    Builds the dictionary of trigrams from the list of text
    """
    keys = list()
    values = list()
    for i in range(len(text)-2):
        keys.append(text[i] + ' ' + text[i+1])
        values.append(text[i+2])

    pairings = dict()
    i = 0

    for x in keys:
        if i == 0:
            pairings[x] = [values[0]]
        elif x in keys[0:i-1]:
            pairings[x].append(values[i])
        else:
            pairings[x] = [values[i]]
        i = i + 1

    return pairings

def build_new_text(list_of_para, text):
    """
    Uses the trigrams dictionary and builds a new set of text based on a random start
    """
    new_list_of_para = list()
    list_of_keys = list(list_of_para.keys())
    new_list_of_words = str()
    total_length = 0
    extracted = text[-2] + ' ' + text[-1]
    i = 0

    for key in list_of_para:
        total_length = total_length + len(list_of_para[key])

    while i < total_length:
        if i == 0:
            rand_key = random.choice(list_of_keys)
            staging = rand_key.split()
            new_list_of_words = rand_key + ' ' + random.choice(list_of_para[rand_key])
        else:
            staging = new_list_of_words.split()
            last_words = staging[-2] + ' ' + staging[-1]
            if last_words == extracted:
                i = i - 1
                continue
            elif last_words not in list_of_keys:
                new_list_of_words = new_list_of_words + '.'
                rand_key = random.choice(list_of_keys)
                staging = rand_key.split()
                new_list_of_words = rand_key + ' ' + random.choice(list_of_para[rand_key])
                continue
                #if last words is not a key get a random word from staging
            new_list_of_words = new_list_of_words + ' ' + random.choice(list_of_para[last_words])
        i = i + 1
    new_list_of_para.append(new_list_of_words)
    return new_list_of_para[0]

"""#these two functions were made obsolete by the regular expression
def remove_punc(text):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for element in text:  
        if element in punc:  
            text = text.replace(element, "")
    return text


    
def handle_capitalization(text):
    return text.lower()
"""

"""#these three methods were attempts at creating a more structured output
def paragraphs(text):
    listOfPara=[]
    last = 0
    temp = list()
    s= ' '
    for elem in text:
        if elem is '\n':
            temp = s.join(text[last:elem])
            listOfPara.append(temp)
            last = elem
    #after and before carrige return
    return listOfPara

def add_punc(listOfPara):
    #newListOfPara = list()
    temp = list()
    dict_of_contractions = {'ill': 'i\'ll', 'theyve': 'they\'ve', 'hes': 'he\'s',\
                            'cant':'can\'t','wont':'won\'t', 'youre':'you\'re',\
                            'shell':'she\'ll', 'shes':'she\'s', 'whos':'who\'s',\
                            'theres':'there\'s', 'id':'i\'d', }
    #could be  along list and won't handle ill or id well if sick or identification is intended
    for elem in listOfPara:
        temp = elem.split()
        for item in temp:
            if item in dict_of_contractions:
                item = dict_of_contractions[item]()
            else:
                continue
    return listOfPara

def add_caps_join(new_with_punc):
    temp = new_with_punc.split()
    i=0
    for item in temp:
        if item == '.':
            temp[i+1].capitalize()
        i=i+1
"""
def main():
    """
    Main
    """
    filename = input('Please enter the filename: ')


    """#I was unable to get this try except block to function correctly,
    the result was that the script never recognized a filename
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    """
    in_data = read_in_data(filename)
    #print(in_data)
    #words = remove_punc(in_data)
    #word_pairs = handle_capitalization(words)
    #new_textS = #paragraphs(word_pairs)
    new_tries = build_tri_dict(in_data)
    #print(new_tries)
    new_text = build_new_text(new_tries, in_data)
    #new_with_punc = add_punc(new_text)
    #new_with_caps = add_caps_join(new_with_punc)

    print(new_text)

if __name__ == "__main__":
    main()
