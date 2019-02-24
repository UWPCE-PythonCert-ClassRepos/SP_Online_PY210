import random

word_list = list()
trigram_dict = dict()

with open("sherlock_small.txt", 'r') as f:
    for line in f:
        for word in line.split():
            word_list.append(word) # build list of all words in text file

for i in range(len(word_list)-2): # loops through word list to build trigram
    word_key = "{} {}".format(word_list[i], word_list[i+1])
    word_value = word_list[i+2]
    if word_key in trigram_dict:
        trigram_dict[word_key].append(word_value)
    else:
        trigram_dict[word_key] = [word_value]

current_key = random.choice(list(trigram_dict.keys()))  # pick random key to start with
word_chain = current_key
last_two = ""

print("This is the starting key: {}".format(current_key))
while current_key in trigram_dict:
    word_chain = "{} {}".format(word_chain, trigram_dict[current_key][random.randint(0,len(trigram_dict[current_key])-1)])
    last_two = " ".join(word_chain.split()[-2:])    # last two words in word_chain
    current_key = last_two

with open("output_doc.txt", 'w') as file_dest:  # Write new text to new output text file
    file_dest.write(word_chain)