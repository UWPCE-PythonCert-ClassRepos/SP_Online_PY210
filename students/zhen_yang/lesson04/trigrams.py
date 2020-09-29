############
# Trigrams #
############
import os
import random
import sys

text_len = 8000
cur_dir = os.getcwd()
input_source = cur_dir + '\\sherlock.txt'
output_source = cur_dir + '\\sherlock_output.txt'

# build the trigrams dict from the list of words
def build_trigrams_dic(words):
    trigrams_dic = {}
    for i in range(len(words) - 2):
        ##############################################
        # Note: Only hashable type can be keys of dic
        # hashable types are: string, tuple, number
        ##############################################
        # get pair of words and save it in a tuple
        pairwords = tuple(words[i:i + 2])
        follower = words[i + 2] # get the following word
        if pairwords in trigrams_dic:# existig key
            trigrams_dic[pairwords].append(follower)
        else:# new key
            trigrams_dic[pairwords] = [follower]
    return trigrams_dic

# cleaning up the unwanted punctutaions before
# break it into words
def clean_up(line):
    import string
    import re
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_line = line.translate(table)

    # skip the Roman Numbers for the beginng of each chapter
    if re.search('^XI{0,2}|IX|IV|I{2,3}|VI{0,3}$', new_line):
        #print(f"found a Roman Numbers {new_line}")
        return -1
    if re.search('^End', new_line):# the end of the book
        print(f"The End of the book. {new_line}")
        return -2
    return new_line

# output the newly generate text into a text file
def output_new_text_file(new_text):
    import textwrap
    print(f" New text is generated in file: {output_source}")
    with open(output_source, "w") as out_file:
        #out_file.write(new_text)
        out_file.write("\n".join(textwrap.wrap(new_text, 65)))

# build the text by adding the last word of
# three_words_list to the text.
def buildup_text(newwords_list, new_word):
    new_text = " ".join(newwords_list)
    if len(new_text) < text_len:
        newwords_list.append(new_word)
    else:
        print(f"-- Exceed the pre-defined text length ({text_len}) --")
        output_new_text_file(new_text)
        sys.exit()

# generate a random key of trigrams_dic
def random_key():
    key_list = list(trigrams_dic.keys())
    return random.choice(key_list)


# if a word pair isn't in the original text
# we add the word pair as a new key and also random Pick
# a key from trigrams_dic and randomly assign one of its
# value to the new key.
def add_newkey(new_key):
    the_key = random_key()
    rand_num = random.randint(1, len(trigrams_dic[the_key])) - 1
    trigrams_dic[new_key] = [trigrams_dic[the_key][rand_num]]
    print(f"-- Adding New key {new_key}:{trigrams_dic[the_key][rand_num]} --")


#################
# Main part
#################
if __name__ == "__main__":
    # 1. read in the txt file for build trigrams dic
    word_list = []
    start_flag = 0 # for skip the header
    with open(input_source, "r") as in_file:
        for line in in_file:# read in each line
            line = line.rstrip("\n")
            if len(line) == 0:# skip empty line
                continue
            if start_flag == 0: # found the begining of the book
                w = line.split()
                if len(w) == 1 and w[0] == 'I.': # the first chap of the book
                    start_flag = 1
                    #print(f"-- Begin --")
                    continue
            # skip the empty lines and Title part
            if len(line) != 0 and start_flag == 1:
                line = clean_up(line)
                if line == -1:# skip the charpter line
                    continue
                elif line == -2:# finish reading the input file
                    break
                else:
                    # put all words of the file into a single words list
                    for word in line.split():
                        word_list.append(word)
    #print(f"--word list :{word_list}")
    # 2. build the trigrams dic based on the word_list
    trigrams_dic = build_trigrams_dic(word_list)
    # display the dictionary
    #for key, val in trigrams_dic.items():
    #    print(f"{key} => {val}")
    # 3. generate a new text based on the dictinoary
    newwords_list = []
    # 3.1 Picking a random key from the trigrams_dic
    the_key = random_key()
    newwords_list = list(the_key)
    print(f"-- Random Start Key:{the_key} --")
    while True:
        if the_key in trigrams_dic:
            # generate a random number between 1 to
            # the length of the dictionary
            rand_num = random.randint(1, len(trigrams_dic[the_key])) - 1
            third_word = trigrams_dic[the_key][rand_num]
            three_words_list = list(the_key)
            three_words_list.append(third_word)
            # get the last two words as new key
            last_two_words = three_words_list[-2:]
            buildup_text(newwords_list, three_words_list[2])
            # dictionary key can only be the hashable types (string,set,tuple)
            # so convert the list to tuple for searching through the dictionary.
            the_key = tuple(last_two_words)
        else:
            print(f"-- Can't find the key {the_key} --")
            # if a word pair isn't in the original text
            # we add the word pair as a new key and also random Pick
            # a value for it.
            add_newkey(the_key)
