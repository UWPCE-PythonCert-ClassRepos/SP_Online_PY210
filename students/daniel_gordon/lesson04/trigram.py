import random

def read_data(filename = ""):
    """Processes data from a text file and returns a list of all words it contains"""
    if filename == "":
        return "I wish I may I wish I might".split()
    
    
def build_trigrams(words):
    """Builds a trigram from a list of words"""
    """Trigram is a dictionary of lists, using a word pair tuple as a key"""
    trigram = {}
    for i in range(len(words)-2):
        trigram.setdefault((words[i], words[i+1]), []).append(words[i+2])
    return trigram

if __name__ == "__main__":
    words = read_data()
    trigram = build_trigrams()
    key = random.choice(list(trigram))
    new_text = list(key)
    for i in range(20):
        next_word = random.choice(trigram[key])
        key = (key[1], next_word)
        new_text.append(next_word)
        if key not in trigram: break
        
    print(" ".join(new_text))