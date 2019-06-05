import sys
import random

# read from a filename given as the 
# second argument on the commandline
def read_in_data(filename):
    with open(filename, 'r') as file:
        in_data = file.read()

    return in_data

# clean up text sent into trigram application
def sanitize_text(in_data):
    # list of invalid characters to strip out
    invalid_chars = [",",".","-","(",")","[","]","--","#","!","+"]
    # split string on whitespace and create a list
    wall_of_text = in_data.split()
    count = 0
    # loop through the length of the text
    # and remove all invalid characters
    while count <= len(wall_of_text) - 1:
        for i in invalid_chars:
            # if invalid character found in string
            # replace that index with the new string
            if i in wall_of_text[count]:
                wall_of_text[count] = wall_of_text[count].replace(i, " ")
        count+=1

    # make a long string out of the list
    wall_of_text = " ".join(wall_of_text)
    # then split string based on whitespace and then 
    # dump it back into the original list created
    in_data = wall_of_text.split()

    return in_data

def trigram(words):
    # words parameter is a list to create matches from
    # trigrams empty dictionary to store key values in
    trigrams = {}
    
    for i in range(len(words) - 2):
        # dictionary keys
        pair = tuple(words[i:i + 2])
        # word after match for values
        follower = words[i + 2]
        # check if key is in dictionary and add it
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            # add list as value
            trigrams[pair] = [follower]
    
    return trigrams

def build_text(word_pairs):
    next_word_list = []
    list_pair = []
    new_text = []
    output_text = []
    count = 0
  
    # iterate through dicitonary keys and build two lists
    # a list of keys and a list of the values and randomize output 
    for i in word_pairs:
        list_pair.append(list(i))
        next_word_list.append(list(word_pairs[i]))
    
    # set a predefined number of loops and generate a new list
    # based on random keys followed by a random value
    while count < 20:
        output_text = random.choice(list_pair) + random.choice(next_word_list)
        new_text.append(" ".join(output_text))
        count+=1
    
    return " ".join(new_text)
    
    
    
if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = sanitize_text(in_data)
    word_pairs = trigram(words)
    new_text = build_text(word_pairs)
    print(new_text)
