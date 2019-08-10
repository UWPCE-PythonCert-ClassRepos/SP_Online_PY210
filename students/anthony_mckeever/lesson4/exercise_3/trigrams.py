"""
Programming In Python - Lesson 4 Exercise 3: Trigrams
Code Poet: Anthony McKeever
Start Date: 08/07/2019
End Date: 08/09/2019
"""
import argparse
import os
import random
import sys


parser = argparse.ArgumentParser(description="Creates trigrams and outputs a new fun document.")
parser.add_argument("--in_file", metavar="in", type=str, help="The input file to read.")
parser.add_argument("--out_file", metavar="out", type=str, help="Where to save the output.  Do not include this to print the output to the console.")
parser.add_argument("--max_words", metavar="max", type=int, help="How many words the output should be.  Defaults to 200 if empty or less than 1")
parser.add_argument("--run_tests", action='store_true', help="Run unit tests and exit without running the rest of the app.")


punctuation = [".", "!", "?", "--", ":", ",", "(", ")", ";", "\"", "'", "\r", "\n"]


def get_file(file_name):
    """
    Return the contents of a text file.

    :file_name: The file to read from.
    """
    if not os.path.isfile(file_name):
        message_and_exit(f"No file exists at \"{file_name}\"")

    with open(file_name, "r") as f:
        content = f.read()
    return content


def get_words(content):
    """
    Return a list of words from a string.

    :content:   The string to break down into individual words.
    """
    for p in punctuation:
        content = content.replace(p, " ")
    return content.split()


def get_trigrams(content):
    """
    Return a dictionary of trigrams parsed from the content.

    :content:   The string to parse into trigrams.
    """
    words = get_words(content)
    trigrams = {}

    for i in range(len(words) - 2):
        pair = tuple(words[i:i+2])
        follower = words[i + 2]

        if pair not in trigrams.keys():
            entry = {pair : []}
            trigrams.update(entry)

        trigrams[pair].append(follower)
    
    return trigrams


def build_text(trigrams, max_words):
    """
    Return a string of words cobbled together from a trigram collection.

    :trigrams:  The dictionary of trigrams.
    :max_word:  Desired length in words of the string.
    """
    output = []
    
    starter = random.choice(list(trigrams))
    output.extend(starter)
    output[0] = output[0].capitalize()

    capitalize_next = True
    while len(output) <= max_words:
        next = random.randrange(0, len(output) - 1)
        next_pair = tuple(output[next : next + 1])

        word = ""
        if next_pair in trigrams.keys():
            word = random.choice(trigrams[next_pair])
        else:
            random_pair = random.choice(list(trigrams))
            word = random.choice(random_pair)
        
        puctuate = random.randrange(1, 101) % random.randrange(1, 26) == 0
        p = random.choice(punctuation[:-4]) 
        
        if puctuate:
            if p == '(' or p == ')':
                word = f"({word})"
            else: 
                word = word + p
                
        if capitalize_next:
            word = word.capitalize()
            capitalize_next = False
                    
        # If we select an period, question mark, or exclaimation point, capitalize the next word.
        capitalize_next = p in punctuation[:4] and puctuate

        output.append(word)
    
    return " ".join(output) + "."


def write_content(content, out_file):
    """
    Write content to a file.

    :content:   The content to write.
    :out_file:  The location to write the content to.
    """
    with open(out_file, "w") as write_file:
        write_file.write(content)


def run_tests():
    """
    Run unit tests and exit the script.
    """
    test_content = "Stuff in a box. Stuff in a bottle. Stuff in a can."
    test_list = ['Stuff', 'in', 'a', 'box', 'Stuff', 'in', 'a', 'bottle', 'Stuff', 'in', 'a', 'can']
    test_trigram = {('Stuff', 'in'): ['a', 'a', 'a'],
                    ('in', 'a'): ['box', 'bottle', 'can'],
                    ('a', 'box'): ['Stuff'],
                    ('box', 'Stuff'): ['in'],
                    ('a', 'bottle'): ['Stuff'],
                    ('bottle', 'Stuff'): ['in']}

    assert get_words(test_content) == test_list
    assert get_trigrams(test_content) == test_trigram
    assert len(build_text(test_trigram, 200)) >= 200

    message_and_exit("Tests passed!")


def message_and_exit(msg):
    """
    Log a message to the console then exit.

    :msg:   The message to log.
    """
    print(msg)
    sys.exit()


if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.run_tests:
        run_tests()

    if args.in_file is None or args.in_file == "":
        message_and_exit("You must provide an input file.  Use --help for a list of command line arguments.")
        
    max_words = args.max_words if args.max_words is not None and args.max_words > 0 else 200

    content = get_file(args.in_file)
    trigrams = get_trigrams(content)
    new_content = build_text(trigrams, max_words)
    
    if args.out_file is None or args.out_file == "":
        print(new_content)
    else:
        write_content(new_content, args.out_file)
