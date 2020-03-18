#!/usr/bin/env python3

import random


###################################


def get_file_data(in_filename):

    with open(in_filename, 'r') as fil:
        out_data = fil.read()
    fil.close()
    out_data = out_data.lower()

    return out_data


def filter_data(in_data):

    # filter data non alpha
    out_data = in_data
    out_data = out_data.replace(',', '')
    out_data = out_data.replace('.', '')
    out_data = out_data.replace(')', '')
    out_data = out_data.replace('(', '')
    out_data = out_data.replace('--', ' ')

    return out_data


def make_words(in_data):

    lst_words = in_data.split()

    return lst_words


def build_trigram(in_lst_words):

    """
        des: create dictionary with key==word pair, value==next word
        in: list
        out: dict
    """
    trigram_dict = {}
    for i in range(len(in_lst_words) - 2):
        key = tuple(in_lst_words[i:i + 2])
        next_word = in_lst_words[i + 2]
        if key not in trigram_dict.keys():
            trigram_dict[key] = [next_word]
        else:
            # key already exists
            trigram_dict[key].append(next_word)
    return trigram_dict


def create_new_story_text(trigrams, in_word_lst):

    """ Des: create random story text from
        in: dict trigram, list of words
        out: random story text
    """

    max_story_size = 100
    words = in_word_lst
    story_lst = []

    # rand start point near beginning
    x_rand_start = random.randint(0, 15)
    story_lst.append(words[x_rand_start])
    story_lst.append(words[x_rand_start+1])

    flg_finished = False
    while flg_finished is not True:
        word_x = story_lst[-1]
        word_y = story_lst[-2]
        if (word_y, word_x) in trigrams:
            word_ary = trigrams[(word_y, word_x)]
            rand_word = random.choice(word_ary)
            story_lst.append(rand_word)
        else:
            # we are done
            break

        if len(story_lst) >= max_story_size:
            # we are done end of new story
            break

    out_story = " ".join(story_lst)

    return out_story

###################################

# main


if __name__ == "__main__":

    filename = "Sherlock_small.txt"
    data = get_file_data(filename)
    # print(f"Source story data:\n {data}\n")
    data = filter_data(data)
    word_lst = make_words(data)
    trigram = build_trigram(word_lst)
    new_story_text = create_new_story_text(trigram, word_lst)
    print(f"Created random story text from trigram:\n {new_story_text}\n")
