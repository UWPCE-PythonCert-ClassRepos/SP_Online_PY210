#!/usr/bin/env python3

# For this assignment, it wasn't clear exactly what I need to deliver. 
# I hope this is on point. If there's anything else you expected,
# please let me know!


import random

def get_file(filename):
# open file, then add space before and after all punctuation as mod_file
    with open(filename,'r') as f:
        mod_text = f.read()
    return(mod_text)

# split each word, treating all punctuation as an independent word
def split_text(mod_text):
    mod_text = mod_text.replace("."," .")
    mod_text = mod_text.replace("Mr .", "Mr.")
    mod_text = mod_text.replace(". . .","... ")
    mod_text = mod_text.replace("?"," ?")
    mod_text = mod_text.replace("!"," !")
    mod_text = mod_text.replace(","," ,")

    word_list = mod_text.split()
    return(word_list)

# convert words into dict with 2 word keys and 3rd words as values.
# 3rd words are allowed to repeat so common followers are more likely.
def make_dict(word_list):
    d = {}
    for i in range(len(word_list)-2):
        pair = (word_list[i], word_list[i+1])
        if pair not in d:
            d[pair] = [word_list[i+2]]
        else:
            d[pair].append(word_list[i+2])
    return(d)

def make_story(d):
    # find a word pair at the beginning of a sentence to start our story
    while True:
        start = random.choice(list(d.keys()))
        if ("." or "!" or "?") in start[0]:
            word = start[1]
            start_list = []
            for key in d:
                if key[0] == start[1]:
                    start_list.append(key)
            d_key = random.choice(start_list)
            break

    # generate the story
    story = " ".join(d_key)

    while len(story) < 2000 or d_key[1] is not ("." or "!" or "?"):
        next_word = d[d_key][random.randint(0,len(d[d_key])-1)]
        d_key = (d_key[1], next_word)
        story = "{} {}".format(story, next_word)

    # clean up the extra spaces, then print
    story = story.replace(" .",".")
    story = story.replace(" !","!")
    story = story.replace(" ?","?")
    story = story.replace(" ,",",")

    print("Fox in Socks, the remix\n\n"+story+"\n\nRemix complete!")

def main():
    mod_text = get_file('fox_in_socks.txt')
    word_list = split_text(mod_text)
    d = make_dict(word_list)
    make_story(d)

if __name__ == "__main__":
    main()
