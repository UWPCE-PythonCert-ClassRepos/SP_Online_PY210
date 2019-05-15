'''Lesson 04 | Trigrams – Simple Text Manipulation'''

# Developing Your Solution
# This assignment has two parts: the key one is the trigrams exercise itself, but you also need to do some text processing to get a full book in shape for processing.
# I suggest you write the trigrams part first; it’s more interesting :-)
#
# trigrams
# Key to the trigrams problem is the selection of the data structure to use to hold the “trigrams” themselves. What do we need here?

#!/usr/bin/env python3
import random
import string

# words = "I wish I may I wish I might".split()
# print('words: ', words)

def clean_line(line):
    clean_line = line.replace('--', '  ')
    clean_line = clean_line.translate(str.maketrans({   '\r': None,
                                                        '\n': ' ',
                                                        ',': None,
                                                        '"': None,
                                                        "'": None,
                                                        ';': None,
                                                        ':': None,
                                                        # '.': None,
                                                        '!': None,
                                                        '?': None}))

    # clean_line = clean_line.translate(str.maketrans({   '\r': None,
    #                                                     '\n': ' ',
    #                                                     }))

    # print ('clean_line: ', clean_line)
    return clean_line

def read_story(file):
    story_start = False

    with open(file, 'r') as full_story:
        for line in full_story:
            if 'To Sherlock Holmes she is always THE woman.' in line or story_start is False:
                story_start = True
                story = clean_line(line)
            elif not 'End of the Project' in line and story_start is True:
                story += clean_line(line)
            else:
                break
    return story

def build_trigram(story):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    story = story.split()

    for i in range(len(story)-2): # why -2 ?
        pair = story[i:i + 2]
        follower = story[i + 2]
        # print('pair: ',pair)
        # print('follower: ',follower)

        trigrams.setdefault(tuple(pair),[]).append(follower)

        # print('trigrams: ', trigrams)
    return trigrams

def create_trigram_story(trigram, trigram_story, starting_tuple):
    trigram_story_list = list(starting_tuple)

    while len(trigram_story_list) < 500:
        pair_match =  trigram_story_list[-2:]
        # print('match: ', pair_match, ' | ', follower_match)

        if tuple(pair_match) in trigram:
            follower_match = random.choice(trigram[tuple(pair_match)])
            trigram_story_list.append(follower_match)
        else:
            print('Tuple match does not exist: ', pair_match)
            break

    with open(trigram_story, 'w') as f:
        f.write(" ".join(trigram_story_list))


if __name__ == "__main__":
    # story = read_story('lesson04\\sherlock_small.txt')
    story = read_story('lesson04\\sherlock.txt')

    create_trigram = build_trigram(story)
    # print('create_trigram: ', create_trigram)

    # for k,v in create_trigram.items():
    #     print(f'{str(k):30} | {v}')

    create_trigram_story(create_trigram, 'lesson04\\sherlock_trigram.txt', ('it', 'was'))
    # create_trigram_story(create_trigram, 'lesson04\\sherlock_trigram.txt', random.choice(list(create_trigram)))
