import random
import os.path as path

def data_to_words():
    #Convert text from file to series of words
    input_text_file = input('What is the file address of the source text?')
    words_lst = [ ]

    #Set bool to identify header
    has_seen = False
    with open(input_text_file,'r') as f_read:
        for line in f_read:
            if '***' in line:
                has_seen = True
                continue
            #Only reads in after header
            if has_seen:
                #Eliminate punctuation, does not address parentheses/single quotes
                no_dashes = line.replace('--',' ')
                no_commas = no_dashes.replace(',','')
                no_open_paren = no_commas.replace('(','')
                no_closed_paren = no_open_paren.replace(')','')
                no_period = no_closed_paren.replace('.','')
                no_exclamation = no_period.replace('!', '')
                no_question = no_exclamation.replace('?', '')
                no_quotes = no_question.replace('"', '')
                clean_string = no_quotes.lower()

                # Divide sample text into individual words
                words_lst.extend(clean_string.split())

    return words_lst

def build_trigrams(words_lst):
    #Create dictionary of trigrams
    trigrams = dict()
    # Loop until reaching the second to last entry, since this does not have 2 words following
    i = 0
    #First pair recorded to use to seed the story start
    first_pair = words_lst[0:2]
    while i < len(words_lst) - 2:
        word_pair = words_lst[i:i + 2]
        key_tup = tuple(word_pair)
        if key_tup not in trigrams:
            trigrams[key_tup] = []
        trigrams[key_tup].append(words_lst[i + 2])
        i += 1
    return trigrams, first_pair

def build_text(trigrams,first_pair):
    #Write story based on trigrams

    #Feed starting pair
    story = first_pair[:]
    first_pair_copy = first_pair[:]
    #Generate a 100 word story
    j=0
    while j < 100:
        key_pair = story[j:j+2]
        key_pair_tup= tuple(key_pair)
        #Protect against a key combination without a value
        if key_pair_tup not in trigrams:
            next_word = random.choice(story)
        else:
            next_word = random.choice(trigrams[key_pair_tup])
        story.append(next_word)
        j += 1
    return story

def write_to_file(story):
    #Write story to file
    directory = input('Where do you want the text output?')
    story_name = input('What is the file name of the story?')
    full_file = path.join(directory,story_name)
    story_string = ' '.join(story)
    with open(full_file,'w') as f:
        f.write(story_string)

if __name__ == "__main__":
    word_lst = data_to_words()
    trigram, first_pair = build_trigrams(word_lst)
    story_text = build_text(trigram,first_pair)
    write_to_file(story_text)

