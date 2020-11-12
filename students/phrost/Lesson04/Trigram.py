###Lesson 4 - Trigram

import random


def import_text(file):
    with open(file=file, mode='r') as text:
        word_list = [word for word in text.read().split() if word.isalnum()]
    return word_list


def tri_dict(word_list):
    trigram = {}
    for index in range(len(word_list) - 2):
        word1 = word_list[index]
        word2 = word_list[index + 1]
        word3 = word_list[index + 2]
        pair = (word1, word2)
        if pair not in trigram:
            trigram[pair] = [word3]
        else:
            trigram[pair].append(word3)
    return trigram


def generate_sentence(trigram):
    sentence = []
    starting_key = random.choice(list(trigram.keys()))
    sentence.extend([word for word in starting_key])
    sentence.append(trigram[starting_key][random.choice(range(0, len(trigram[starting_key])))])

    while len(sentence) < 12:
        try:
            key1, key2 = sentence[-2:]
            sentence.append(trigram[(key1, key2)][random.choice(range(0, len(trigram[(key1, key2)])))])
        except KeyError:
            break

    sentence[0] = sentence[0].capitalize()
    if sentence[-1][-1] != '.':
        sentence[-1] = f'{sentence[-1]}.'
    return sentence


def generate_paragraph(trigram):
    new_paragraph = []
    while len(new_paragraph) <= 10:
        new_paragraph.append(generate_sentence(trigram))
    return new_paragraph


def generate_new_book(text):

    for paragraph in text:
        for sentence in paragraph:
            for word in sentence:
                print(word, end=' ')
            print()
        print()


def main():
    initial_text = import_text('sherlock_small.txt')
    trigram = (tri_dict(initial_text))

    new_text = []
    for _ in range(2):
        new_text.append(generate_paragraph(trigram))

    generate_new_book(new_text)


if __name__ == '__main__':
    main()
