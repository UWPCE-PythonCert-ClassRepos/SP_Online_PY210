#!/usr/bin/env python3
#Lesson 4-Trigrams Excercise
import random
import sys

def read_in_data(filename):
    '''
    Reads in file and returns either basic text back or cleaned
    Up text if it is a more complex file
    '''
    line_by_line = []
    with open(filename,'r') as f:
        #checks to see if its a basic txt doc or something more complex
        text = f.read()
        if 'Gutenberg' not in text:
            return text
        else:
            f.seek(0,0)
            for line in f:
                line = line.strip(',\n *' )
                if 'START OF THIS PROJECT GUTENBERG' in line:
                    line_by_line.append(line)
                elif 'End of the Project Gutenberg' in line:
                    line_by_line.append(line)
                elif 'Gutenberg' in line:
                    continue
                elif line.isspace() == True:
                    continue
                elif line.startswith(('I','V','X')):
                    continue
                elif line.isupper():
                    continue
                elif not line:
                    continue
                line = line.replace('.','')
                line_by_line.append(line)

            for i, elem in enumerate(line_by_line):
                if 'START OF THIS PROJECT GUTENBERG' in elem:
                    start = i
                elif 'End of the Project Gutenberg' in elem:
                    end = i

            line_by_line = line_by_line[start + 1:end]
            line_by_line = " ".join(line_by_line)

            return line_by_line

def clean_words(data):
    '''
    Splits cleaned text into a list to be used in trigrams dictionary
    '''
    cleaned_data = data.split()

    return cleaned_data

def build_dict(words):
    '''
    Creates the needed dictionary for trigrams text
    '''
    tri_dict = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        f_list = []
        f_list.append(follower)

        if pair in tri_dict:
            value = tri_dict.get(pair).extend(f_list)
        else:
            tri_dict[pair] = f_list

    return tri_dict

def build_trigram(tri_dict):
    '''
    Builds up the trigrams text using the trigrams dictionary
    '''
    #Creates first trigram of sequence
    num_of_keys = len(tri_dict.keys()) - 1
    ran_num = random.randint(0,num_of_keys)
    first_key = list(tri_dict.keys())[ran_num]
    next_word = tri_dict.get(first_key)[0]
    trigram_list = []
    trigram_list.append(first_key[0])
    trigram_list.append(first_key[1])
    trigram_list.append(next_word)

    #builds random trigram text
    for i in range(100):
        new_seq = tuple(trigram_list[-2:])
        if len(trigram_list) >= 250:
                break

        elif new_seq in tri_dict:
            next_word = random.choice(tri_dict.get(new_seq))
            trigram_list.append(next_word)

        else:
            break

    full_text = " ".join(trigram_list)
    print(full_text)

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Please Pass In An Available File')
        sys.exit(1)

    data = read_in_data(filename)
    words = clean_words(data)
    tri_dict = build_dict(words)
    build_trigram(tri_dict)
