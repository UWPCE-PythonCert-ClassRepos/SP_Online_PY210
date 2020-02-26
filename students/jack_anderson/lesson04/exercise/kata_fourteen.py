#!/usr/bin/env python3
"""
Jack Anderson
02/24/2020
UW PY210
Lesson 04
"""
import random
import sys



#words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):
        pairs = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pairs)
        if key not in trigrams.keys():
            trigrams[key] = [follower]
        else:
            trigrams[key].append(follower)
    return trigrams


def read_in_data(filename):
    start_of_text = get_doc_start()
    end_of_text = get_doc_end()
    in_data = list()
    invalid_chars = str.maketrans(".,()!?;", "       ")
    with open(filename, "r") as f:
        for num,line in enumerate(f, 1):
            if num > start_of_text and num < end_of_text:
                line = line.replace('"', ' ')
                line = line.replace('--', ' ')
                line = line.translate(invalid_chars)
                in_data.append(line)

        return in_data



def get_doc_start():
    start = "*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
    with open(filename, "r") as f:
        for num, line in enumerate(f, 1):
            if start in line:
                x = num
                start_line = 1 + x
                f.close()
                return start_line
            else:
                return 0

def get_doc_end():
    count = 0
    end = "*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
    with open(filename, "r") as f:
        for num, line in enumerate(f, 1):
            if end in line:
                x = num
                end_line = x - 1
                f.close()
                return end_line
            else:
                count += 1
        return count


def make_words(in_data):
    new_words = list()
    for line in in_data:
        line = line.split()
        for item in line:
            if item == "I":
                new_words.append(item)
            else:
                new_words.append(item.lower())
    return (new_words)



def get_sentance_start(word_pairs):
    sentence_start = random.choice(list(word_pairs.keys()))
    first_word = sentence_start[0]
    next_word = sentence_start[1]
    start_of_sentence = (first_word, next_word)
    return start_of_sentence


def create_sentence(word_pairs):
    sentence = list()
    start = random.choice(list(word_pairs.keys()))
    start_follower = word_pairs[start]
    sentence.append(start[0].title())
    sentence.append(start[1])
    sentence.append(start_follower[0])

    for i in range(random.randint(12, 20)):
        firstKey = sentence[-2]
        secondKey = sentence[-1]
        next_word = word_pairs[firstKey, secondKey]
        sentence.append(next_word[0])

        # try:
        #     next_word = word_pairs[sentence[]]
        #     next_set = word_pairs[firstKey, nextKey]
        #     sentence.append(next_set[0])
        #     i = i + 1
        # except KeyError:
        #     print("No Key matches made")
        #     sys.exit()

    a = " ".join(sentence)
    end = "."
    return (a + end)

def build_text(filename):
    story = " "
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    prompt = input("Please enter a number of sentences for the story: \n")
    line_start = 0

    if len(prompt) == 0:
        line_end = 100
    else:
        line_end = int(prompt)

    while line_start < line_end:
        new_text = create_sentence(word_pairs)
        if line_start % 7 == 0:
            story = (story + " " + new_text + '\n\n')
            line_start += 1

        else:
            story = (story + " " + new_text)
            line_start += 1

    return story



if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("you muster pass in a filename")
        sys.exit(1)

    story = build_text(filename)

    print(story)