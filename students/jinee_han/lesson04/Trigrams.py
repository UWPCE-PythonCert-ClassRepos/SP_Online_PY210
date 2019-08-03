import random, re, sys

def read_and_clean_text(filename):
    '''
    Read and clean text file of unwanted characters
    :param filename: the relative file name including .txt
    :return: a list of words
    '''
    file = open(filename, "r")
    word_collection = []
    for line in file:
        line = line.strip('\n')
        line = re.sub(r'[^\w\s]',' ',line)
        for word in line.split():
            word_collection.append(word.lower())
    return word_collection

def build_trigram_dict(words):
    '''
    Build the trigram dictionary from our word list
    :param words: the word list formed by the given text file
    :return: a dictionary where key = first two words, value = following word
    '''
    dict_text = dict()
    for i in range(len(words)-2):
        dict_key = tuple(words[i:i+2])
        follower = words[i + 2]
        if dict_key in dict_text.keys():
            # key and value present in dict
            val = dict_text[dict_key]
            val.append(follower)
        else:
            list = [follower]
            dict_element = {dict_key : list}
            dict_text.update(dict_element)

    return dict_text

def create_text(dict_text, max_length):
    '''
    Create a new corpus based on the dictionary trigram and max allowed length
    :param dict_text: the trigram dictionary
    :param max_length: the max allowed length of the story
    :return: a string of words forming the new story
    '''
    story_list = []
    random_key = random.choice(list(dict_text.keys()))
    story_list.extend([random_key[0], random_key[1]])
    val = dict_text[random_key]
    story_list.append(random.choice(val))
    while len(story_list) < max_length:
        key = tuple(story_list[-2:])
        if key in dict_text.keys():
            val = dict_text[key]
            story_list.append(random.choice(val))
        else:
            random_key = random.choice(list(dict_text.keys()))
            story_list.append(random.choice(dict_text[random_key]))

    return " ".join(story_list)

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename!")
        sys.exit(1)

    word_collection = read_and_clean_text(filename)
    dict_text = build_trigram_dict(word_collection)
    new_text = create_text(dict_text, max_length=250)
    print(new_text.capitalize())

