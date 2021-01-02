
import random
import sys

#'I wish I may I wish I might '.split()


def read_in_data(filename):
    in_data = ''
    with open(filename, 'r') as f:
        for i in f:
            in_data += i
        # print(in_data)
        in_data = in_data.lower()
        in_data = in_data.split()
    return in_data


def make_words(in_data):
    punctuations = ['-', '--', ',', '(', ')', '.', '"', '~', '@', '#', '$', '%']
    words = []
    for i in in_data:
        i.split(',')
        for j in punctuations:
            if j in i:
                i = i.replace(j, ' ')
                i = i.strip()
        words.append(i)
    return words


def build_trigram(words):
    trigrams = {}
    for i in range(0, len(words) - 2):
        keys = tuple(words[i: i + 2])
        values = words[i + 2]
        if keys not in trigrams:
            trigrams[keys] = [values]
        else:
            trigrams[keys].append(values)
    return trigrams


def build_text(word_pairs):
    new_text = []
    pair = random.choice(list(word_pairs.keys()))
    for i in pair:
        new_text.append(i)
    third = random.choice(word_pairs[pair])
    new_text.append(third)
    for x in range(25):
        new_pair = tuple(new_text[-2:])
        if new_pair in word_pairs.keys():
            new_text.append(random.choice(word_pairs[new_pair]))
        else:
            return ' '.join(new_text)
    return ' '.join(new_text)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
