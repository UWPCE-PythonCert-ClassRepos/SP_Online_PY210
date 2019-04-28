import random
import re

trigram = 'I wish I may I wish I might'

words = trigram.split()

# builds list of words from txt file
def read_in_data(filename):
    fulltext = []
    with open(filename,'r') as text:
        for line in text:
            line = re.sub('--',' ',line)
            line = line.strip('(')
            line = line.strip(')')
            for word in line.split():
                fulltext.append(word.lower())
    return fulltext


# tests creation of a trigram
def build_trigram(words):
    trigrams = {}
    for i in range(len(words[:-2])):
        key = "{} {}".format(words[i],words[i+1])
        val = words[i+2]
        if key in trigrams:
            trigrams[key].append(val)
        else:
            trigrams[key] = [val]
    return trigrams


def write_story(word_pairs):
    
    story = ''
    start = random.choice(list(word_pairs.keys()))
    pairs = start
    while start in word_pairs:
        pairs = "{} {}".format(pairs,word_pairs[start][random.randint(0,len(word_pairs[start])-1)])
        story = ' '.join(pairs.split()[-2:])
        start = story
        # if len(story) >= 1000:
            # break
    return pairs

def write_file(story_text):
    with open("my_story.txt", "w+") as outfile:
        outfile.write(story_text)

if __name__ == "__main__":
    text = read_in_data('sherlock_small.txt')
    word_pairs = build_trigram(text)
    story_text = write_story(word_pairs)
    write_file(story_text)