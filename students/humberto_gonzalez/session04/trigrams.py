#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:12:44 2019

@author: humberto gonzalez
"""

import random
import sys
import requests




sherlock_small = "One night--it was on the twentieth of March, 1888--I was \
returning from a journey to a patient (for I had now returned to \
civil practice), when my way led me through Baker Street. As I \
passed the well-remembered door, which must always be associated \
in my mind with my wooing, and with the dark incidents of the \
Study in Scarlet, I was seized with a keen desire to see Holmes \
again, and to know how he was employing his extraordinary powers. \
His rooms were brilliantly lit, and, even as I looked up, I saw \
his tall, spare figure pass twice in a dark silhouette against \
the blind. He was pacing the room swiftly, eagerly, with his head \
sunk upon his chest and his hands clasped behind him. To me, who \
knew his every mood and habit, his attitude and manner told their \
own story. He was at work again. He had risen out of his \
drug-created dreams and was hot upon the scent of some new \
problem. I rang the bell and was shown up to the chamber which \
had formerly been in part my own."


def obtain_input():
    '''Obtains URL from user and returns the text from the link'''
    path = input("Link to text file from Project Gutenberg website: ")
    end = ['quit','Quit','cancel','exit','Exit']
    if path in end:
        sys.exit()
    try:
        response = requests.get(path)
        txt = response.text
    except:
        print('Please pass in a link to a text file from the Gutenberg website')
        return obtain_input()
    
    return txt


def clean_text(text):
    '''Takes in a raw string or text and cleans it be removing unwanted punctuation or other items'''
    '''We will assume the test is fro the Gutenberg website and also cut the text down'''
    text = text.split('***')[2]
    new_text = text.replace(", "," ")
    new_text = new_text.replace("txt"," ")
    out = ".,()?!:;-*[]_0123456789"
    inn = "                       "
    mapp = str.maketrans(out,inn)
    new_text = new_text.translate(mapp)
    new_text = new_text.lower()
    return new_text
    


def trigrams_dict(text):
    '''Takes in text and returns a trigrams dictionary'''
    text = text.split()
    tri_dict = {}
    for i in range(2,len(text)):
        word1 = text[i-2]
        word2 = text[i-1]
        key = (word1,word2)
        value = text[i]
        
        if key not in tri_dict:
            tri_dict[key] = [value]
        else:
            tri_dict[key].append(value)
    return tri_dict


def create_new_text(tri_dict,n):
    '''Takes in a trigrams dict as input and uses the Keys and Values\
       to create a new string or text
       
       n = desired length of new text'''
       
    first_choice = random.choice(list(tri_dict.keys()))
    new_text = []
    for i in first_choice:
        new_text.append(i)
    i = 0
    while len(new_text) < n:
        key = (new_text[i],new_text[i+1])
        if key in tri_dict:
            words = tri_dict[key]
            if len(words)>1:
                word = random.choice(words)
                new_text.append(word)
            else:
                new_text.append(words[0])
        else:
            key = random.choice(list(tri_dict.keys()))
            words = tri_dict[key]
            if len(words)>1:
                word = random.choice(words)
                new_text.append(word)
            else:
                new_text.append(words[0])
        i+=1
    return " ".join(new_text)


if __name__ == "__main__":
    text = obtain_input()
    text = clean_text(text)
    tri_dict = trigrams_dict(text)
    new_text = create_new_text(tri_dict,n=100)
    print()
    print()
    print(new_text)