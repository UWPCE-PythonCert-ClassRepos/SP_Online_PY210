import random
import sys
import os
"""
trigrams.py

Zach Meves
Python 210
Lesson 04
Trigrams
"""


def make_trigrams(txt: str) -> dict:
    """Generate a trigrams mapping based on an input text.

    Parameters
    ----------
    txt : str
        Text to parse

    Returns
    -------
    dict
        Trigrams mapping, tuple of two strings -> list of strings"""

    tgram = dict()
    words = txt.split()
    for i in range(1, len(words) - 1):
        key = tuple(words[i-1: i+1])
        value = words[i + 1]
        tgram.setdefault(key, []).append(value)

    return tgram


def generate_text(trigram: dict, words: int = 100) -> str:
    """Generate a string from a trigrams mapping.

    Parameters
    ----------
    trigram : dict
        Trigram mapping
    words : int, optional
        Maximum number of words to generate"""

    i = 0
    seed = random.randint(0, len(trigram))
    keys = list(trigram.keys())

    output = list(keys[seed])  # Initial two words
    k1, k2 = output[0], output[1]

    while i < words:
        if (k1, k2) in trigram:
            new_word = random.choice(trigram[(k1, k2)])
            k1, k2 = k2, new_word
            output.append(new_word)
            i += 1
        else:
            break

    return ' '.join(output)


def read_file(file: str) -> str:
    """Read the text in a file.

    Parameters
    ----------
    file : str
        Name of file

    Returns
    -------
    str
        Text from file with DOS endings removed"""

    with open(file) as f:
        txt = f.readlines()

    # Check for any Gutenberg headers
    for i, line in enumerate(txt):
        if line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK'):
            txt = txt[i+1:]
            break

    return '\n'.join(txt)


if __name__ == '__main__':
    """Main program.
    
    Usage:
        > python trigrams.py filename [word_limit]
        
        * filename : name of text file to read
        * word_limit : optional, maximum number of words to print"""

    args = sys.argv
    if len(args) < 2:
        raise RuntimeError("Please provide a file to read")
    file = args[1]
    kw = {}
    if not os.path.exists(file):
        raise FileExistsError(f"{file} does not exist!")
    if len(args) > 2:
        try:
            kw['words'] = int(args[2])
        except ValueError:
            raise RuntimeError(f"Argument {args[1]} cannot be interpreted as a number")
    else:
        words = None

    txt = read_file(file)
    tgrams = make_trigrams(txt)
    output = generate_text(tgrams, **kw)

    print('')
    print(output)
