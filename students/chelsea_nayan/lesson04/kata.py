# chelsea_nayan, UWPCE Python 210, Lesson04: Kata Fourteen: Tom Swift Under Milk Wood
# This was difficult!

import random # Used to pick a random word from the dictionary value list
import re # Used to use findall()

story_limit = 10000 # Sets the character limit so the new_story can't go on forever...
text_file = 'sherlock_big.txt' # Chooses the text file to be read
first_two_words = ["One", "night"] # Chooses the first two words for the trigram

with open(text_file, 'r') as infile, open('new_story.txt', 'w') as outfile:

    text = infile.read() # Stores the txt file as a string
    lst = re.findall(r"[\w']+|[.,!?;]", text) # Creates a list of words, findall() separates the punctuation into their own 'words'

    for word in lst: # splits the words that are connected with '--'
        if "--" in word:
            sub = word.split("--")
            if sub[0] not in lst: # Add spliited words to lst if not there
                lst.append(sub[0])
            if sub[1] not in lst:
                lst.append(sub[1])
            lst.remove(word) # Removes the original word connected by '--'

    # The key is a string of two words, the value is a list of words that appear after those two words appear
    d = {}
    for elem in range(len(lst)-2):
        k = f"{lst[elem]} {lst[elem+1]}"
        if k in d.keys(): # Adds the next word to the value list
            d.get(k).append(lst[elem+2])
        else:
            d[k] = [lst[elem+2]] # Adds the new key and value (type list) to the dictionary

    two_words_list = first_two_words # Chooses the first two words for the trigram
    two_words_string = f"{two_words_list[0]} {two_words_list[1]}" # Makes the first two words into a string
    story = two_words_string
    while two_words_string in d.keys() and len(story)<story_limit: # Loops as long as the two word string is a key in the d and doesn't exceed the char story_limit
        next_word = random.choice(d.get(two_words_string)) # Get the next word from the value
        if next_word in "|[.,!?;]": # The case of the next 'word' is punctuation
            story += f"{next_word}"
        else: # The case where the next word is not punctuation
            story += f" {next_word}"
        two_words_list = [two_words_list[1], next_word]
        two_words_string = f"{two_words_list[0]} {two_words_list[1]}"

    # Makes sure the story ends with proper punctuation! Not the greatest way to simulate language...
    if two_words_list[1] not in "!?.":
        story += random.choice([".", "!", "?"])

    outfile.write(story)
