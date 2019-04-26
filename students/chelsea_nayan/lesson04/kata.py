# chelsea_nayan, UWPCE Python 210, Lesson04: Kata Fourteen: Tom Swift Under Milk Wood
import string # to use string.punctuation
import random


with open('sherlock_small.txt', 'r') as infile, open('kataaa.txt', 'w') as outfile:

    # Creates a list of words from infile split by a white space, also /attempts/ to rm punctuation at the ends of words (had to look this up on Stack Overflow)
    lst = [word.lower().strip(string.punctuation) for line in infile for word in line.split()]

    # TO DO:--------------------------------------
    # Split words on '--''
    # Capitalize isolated 'i's
    # Check to see if range in for loop is OK
    # --------------------------------------------


    # The key is a string of two words, the value is a list of words that appear after those two words appear
    d = {}
    for elem in range(len(lst)-2):
        k = f"{lst[elem]} {lst[elem+1]}"
        if k in d.keys(): # Adds the next word to the value list
            d.get(k).append(lst[elem+2])
        else:
            d[k] = [lst[elem+2]] # Adds the new key and value (type list) to the dictionary


    two_words_list = ["was", "on"] # Chooses the first two words for the trigram
    two_words_string = f"{two_words_list[0]} {two_words_list[1]}"
    story = ""
    while two_words_string in d.keys():
        next_word = random.choice(d.get(two_words_string)) # Get the next word from the value
        story += f" {next_word}" # Update the story string
        two_words_list = [two_words_list[1], next_word] # Updates two_words_list
        two_words_string = f"{two_words_list[0]} {two_words_list[1]}"


    outfile.write(story)
