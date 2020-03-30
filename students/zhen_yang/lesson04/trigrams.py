############
# Trigrams #
############
import os
import random


# split the sentence into words list
#words = 'I wish I may I wish I might'.split()







# build the trigrams dict from the list of words
def build_trigrams_dic(words):
    trigrams_dic = {}
    for i in range(len(words)-2):
        ##############################################
        # Note: Only hashable type can be keys of dic
        # hashable types are: string, tuple, number
        ##############################################
        # get pair of words and save it in a tuple  
        pairwords = tuple(words[i:i+2]) 
        follower = words[i+2] # get the following word
        if pairwords in trigrams_dic:
            trigrams_dic[pairwords].append(follower) 
        else:
            trigrams_dic[pairwords]=[follower]
    return trigrams_dic

def clean_up(line):
    import string
    import re
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_line = line.translate(table)

    # found a Roman Numbers for beginng of each chapter
    if re.search('^XI{0,2}|IX|IV|I{2,3}|VI{0,3}$',new_line):
        print(f"found a Roman Numbers {new_line}") 
        return -1
    if re.search('^End', new_line):
        print(f"The End of the book. {new_line}") 
        return -2 
    return new_line





#################
# Main part
#################
if __name__ == "__main__":

    ###########
    # start to build trigrams dictionary
    ###########

    # read in the txt file for build trigrams dic
    cur_dir = os.getcwd()
    source = cur_dir + '\sherlock.txt'  
    word_list = []
    start_flag = 0 
    # read in all the words from a file to a words_list
    with open(source,"r") as in_file:
        # read in each line
        for line in in_file:
            line = line.rstrip("\n")

            if len(line) == 0 :
                continue

            if start_flag == 0 :
                w = line.split()
                if len(w) ==1 and w[0] == 'I.': # the Begining of the book
                    start_flag = 1 
                    #print(f"-- Begin --")
                    continue
            """else:

                w = line.split()
                if w[0] == '***':# the End of the book
                    #print(f"-- End --")
                    break
            """
            # skip the empty lines and Title part
            if len(line)!=0 and start_flag == 1 :
                # cleaning up the unwanted punctutaions before break it into words
                #print(f"-- old lines :{line}")
                line = clean_up(line)
                if line== -1:
                    continue
                elif line == -2:
                    break
                else:
                    # put all words of the file into a single words list
                    for word in line.split():
                         word_list.append(word)

    #print(f"--word list :{word_list}")





    # build the trigrams dic based on the word_list
    trigrams_dic = build_trigrams_dic(word_list)
    # display the dictionary 
    #for key, val in trigrams_dic.items():
    #    print(f"{key} => {val}")

    ###########
    # start to generate text file by using the trigram dictionary
    ###########
    # generate a random number between 0 to the length of the dictinoary
    buildup_text = [] 
    # 3.1 Picking a random key from the trigrams_dic
    key_list = list(trigrams_dic.keys())
    random_key = random.choice(key_list)


    buildup_text=list(random_key) 
    print(f"-- Random Start Key:{random_key} --")
    while random_key in trigrams_dic:
          rand_num = random.randint(0,len(trigrams_dic[random_key]))-1
          third_word = trigrams_dic[random_key][rand_num]
          three_words_list = list(random_key)
          three_words_list.append(third_word)

          # get the last two words as new key
          last_two_words = three_words_list[-2:] 

          # build the text by adding the last word to the list.
          buildup_text.append(three_words_list[2])  

          # dictionary key can only be the hashable types (string,set,tuple)
          # so convert the list to tuple for the dictionary key
          random_key = tuple(last_two_words)

    print(f"-- Can't find the key {random_key}.--")
    #print(f"-- New text --")
    #print(f"{buildup_text}")

