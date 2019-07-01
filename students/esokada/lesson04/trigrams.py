import random

def processtext(filename):
    """Open the book file, strip it of header/footer, and return a list of words."""
    with open(filename, "r", encoding = "utf8") as f:
        trimmedlines = ""
        startpoint = False
        for line in f:
            #Eliminate everything above the Table of Contents, all the chapter headings, and the footer.
            if "Contents" in line:
                startpoint = True
                continue
            if "CHAPTER" in line:
                continue
            if "End of Project Gutenberg's" in line:
                break
            if startpoint == True:
                trimmedlines += line
    words = trimmedlines.split()
    return words


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = words[i:i+2]
        follower = words[i+2]
        #If the pair of words is already a key in the dictionary, add the follower to it. Otherwise, add a new key.
        if tuple(pair) in trigrams:
            trigrams[tuple(pair)].append(follower)
        else:
            trigrams.update({tuple(pair):[follower]})
    return trigrams

def generate_text(trigrams):
    """Use the trigrams dictionary to generate a string of random text."""
    text_list = []
    #Choose a random location to begin the text and add the first two words.
    first_word_location = random.randint(0, len(words)-2)
    text_list.append(words[first_word_location])
    text_list.append(words[first_word_location+1])
    #Add more words.
    while True:
        prevword = text_list[-2]
        currword = text_list[-1]
        options = []
        if (prevword, currword) in trigrams:
            options = trigrams[(prevword, currword)]
            selection = random.choice(options)
            text_list.append(selection)
        #If we end up with a pair that's not in the trigrams, we can just stop.
        else:
            break
        #Set a maximum length for the text.
        if len(text_list) >= 200:
            break
    finaltext = " ".join(text_list)
    #Add a final period on the end of the text if it's not already there.
    if finaltext[-1] != ".":
        finaltext += "."
    #Capitalize the first letter of the text.
    print(finaltext[0].upper()+finaltext[1:])

if __name__ == "__main__":
    words = processtext("styles.txt")
    trigrams = build_trigrams(words)
    generate_text(trigrams)