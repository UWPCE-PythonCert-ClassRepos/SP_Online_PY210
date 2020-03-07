#!/usr/bin/env python3
"""
Jack Anderson
02/24/2020
UW PY210
Lesson 04
"""
import random
import sys



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
    """
    Action to open and read text file and filter out invalid characters
    :param filename: Name of text file
    :return: Filtered version of text file between file header and footer
    """
    start_of_text = get_doc_start()
    end_of_text = get_doc_end()
    in_data = list()
    invalid_chars = str.maketrans(".,()!?;", "       ")
    with open(filename, "r") as f:
        for num,line in enumerate(f, 1):
            if num > start_of_text and num < end_of_text:
                line = line.translate(invalid_chars)
                line = line.replace("I.", ' ')
                line = line.replace("II.", ' ')
                line = line.replace("III.", ' ')
                line = line.replace("IV.", ' ')
                line = line.replace("V.", ' ')
                line = line.replace("VI.", ' ')
                line = line.replace("VII.", ' ')
                line = line.replace("VIII.", ' ')
                line = line.replace("IX.", ' ')
                line = line.replace("XI.", ' ')
                line = line.replace("XII.", ' ')
                line = line.replace("XIII.", ' ')
                line = line.replace("XIV.", ' ')
                line = line.replace("XV.", ' ')
                line = line.replace("' ", ' ')
                line = line.replace(" ' ", ' ')
                line = line.replace(" '", ' ')
                line = line.replace('"', ' ')
                line = line.replace('--', ' ')
                line = line.replace('  ', ' ')
                line = line.replace('-', ' ')
                in_data.append(line)

        return in_data



def get_doc_start():
    """
    Action to check for when to start in the text file. Will start at line 1 if file is not Gutenberg ebook
    :return: Line number to start the trigrams dict.
    """
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
    """
    Action to check for when to end the text file. Will end at last line in text if file is not Gutenberg ebook.
    :return: Line number to end the trigrams dict
    """
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
    """
    Action to take all data from read_in_data function and spit up the words into seperate objects and make all words
    lower case unless the word is 'I'.
    :param in_data: String to split into seperate objects
    :return: new words list with each word as its own object
    """
    new_words = list()
    words_to_not_edit = ("I", "Mr", "Mrs", "Watsom", "Holmes", "St", "Sherlock")

    for line in in_data:
        line = line.split()
        for item in line:
            if item in words_to_not_edit:
                new_words.append(item)
            else:
                new_words.append(item.lower())

    return (new_words)



def create_sentence(word_pairs):
    """
    Action to grab a random key and value from the trigams dict to start a sentence and then add on to that sentence.
    Each sentence starts with a capital letter and ends with a period('.').
    :param word_pairs: The dict created by the trigrams function
    :return: Random sentence containing between 12 to 20 words.
    """
    sentence = list()
    start = random.choice(list(word_pairs.keys()))
    start_follower = word_pairs[start]
    sentence.append(start[0].title())
    sentence.append(start[1])
    sentence.append(start_follower[0])

    for i in range(random.randint(7, 15)):
        firstKey = sentence[-2]
        secondKey = sentence[-1]
        value = word_pairs[firstKey, secondKey]
        next_word = random.choice(value)
        sentence.append(next_word)

    end_check = sentence[-1]
    invalid_check = ("I", "the", 'am')
    if end_check in invalid_check:
        sentence.remove(end_check)

    full_sentence = " ".join(sentence)
    end_punctuation = (". ", "! ", "? ", ". ", ". ")
    end_of_sentence = random.choice(end_punctuation)


    return (full_sentence + end_of_sentence)




def build_text(filename):
    """
    Action to prompt user for number of sentences in story and then build story
    :param filename: File containg text for trigams dict
    :return: A number of generated story text sentences based on user input
    """
    story = ""
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    line_start = 1
    try:
        prompt = input("Please enter a number of sentences for the story: \n")

        if len(prompt) == 0:
            line_end = 25
        else:
            line_end = int(prompt) + 1

        while line_start < line_end:
            new_text = create_sentence(word_pairs)
            if line_start % 10 == 0:
                story = (story + " " + new_text + '\n\n')
                line_start += 1

            else:
                story = (story + new_text)
                line_start += 1

    except (TypeError, ValueError):
        print("You must enter a numerical value")
        sys.exit(1)

    finally:
        return story




if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("you muster pass in a filename")
        sys.exit(1)

    story = build_text(filename)

    print(story)
