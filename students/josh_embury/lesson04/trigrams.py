#!/usr/bin/env python3
# ------------------------------------------------------------------------ #
# Title: Trigrams
# Description: Create text using trigrams

# ChangeLog (Who,When,What):
# JEmbury,12/13/2020,Created started script
# ------------------------------------------------------------------------ #
import random
#--------------------------------------------#
# Text processing
#--------------------------------------------#

def read_text(str_filename):
    # this method reads a file and generates a list of words
    # input a filename as string
    # ouput a list of words
    f = open(str_filename)
    flag = False
    text = ''
    while(True):
        current_line = f.readline()
        if current_line[:34] == 'End of the Project Gutenberg EBook':
            break
        if flag:
            text = text + current_line
        elif current_line[:41] == '*** START OF THIS PROJECT GUTENBERG EBOOK':
            flag = True

    #str_words = f.read()
    f.close()
    return text.split()
#--------------------------------------------#
# Trigram processing
#--------------------------------------------#
def build_trigrams(lst_input_words):
    # desc: create a dict of trigrams
    # assumption: list must be len()>2
    # input: a list of words as string objects
    # output: dictionary with:
        # keys: str - all adjacent word pairs in input list
        # values: lst - all 'third' adjacent word to given key in input list
    dict_trigrams = {}
    for i in range(2,len(lst_input_words)):
        current_pair = lst_input_words[i-2] + ' ' + lst_input_words[i-1]
        dict_trigrams.setdefault(current_pair, []) # set it or get it
        dict_trigrams[current_pair].append(lst_input_words[i])
    return dict_trigrams

def start_sentence(dic):
    # let's choose a random key in dict
    while(True):
        get_string = random.choice(list(dic.keys()))
        str_starting_point = get_string.capitalize()
        if '.' in str_starting_point:
            pass
        elif '-' in str_starting_point:
            pass
        elif '\'' in str_starting_point:
            pass
        elif str_starting_point not in dic:
            pass
        elif len(dic[str_starting_point]) < 1:
            pass
        else: break
    return str_starting_point # known key to test with

def build_sentence(dic):
    # pick random key from dict
    str_starter = start_sentence(dic)
    lst_new_sentence = str_starter.split()
    rough_num_of_words = 100
    while(True):
        current_pair = ' '.join(lst_new_sentence[-2:])
        if current_pair[-1] == '.' and len(lst_new_sentence) >= rough_num_of_words:
            break

        if current_pair in dic:
            current_tri = random.choice(dic[current_pair])
            lst_new_sentence.append(current_tri)
        else:
            #lst_new_sentence.append('. ')
            new_start = start_sentence(dic).split()
            lst_new_sentence.append(new_start[0])
            lst_new_sentence.append(new_start[1])
    return ' '.join(lst_new_sentence)
#-----------------------------------------------#
# Main
#-----------------------------------------------#
if __name__ == '__main__':
    words = read_text('sherlock.txt')
    print(build_sentence(build_trigrams(words)))
