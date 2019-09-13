import random


words = "I wish I may I wish I might".split()

def read_book():
    f = open('sherlock.txt')
    secret_data = f.read()
    secret_data = secret_data.split()
    #find where to start reading text
    if 'START OF THIS PROJECT GUTENBERG EBOOK' in secret_data: 
        find_line_of_text = start_of_text.index('START OF THIS PROJECT GUTENBERG EBOOK')
        remove_previous = start_of_text[find_line_of_text + 1::]
        return remove_previous
    else:
        return secret_data
    f.close()


def build_trigrams(words):
    #Build up trigram dictionary
    trigrams = {}
    for i in range(len(words)-2): 
        pair = words[i:i + 2]
        follower = [words[i + 2]]
        if tuple(pair) not in trigrams:
            trigrams[tuple(pair)] = follower
        else:
            trigrams[tuple(pair)].extend(follower)           
    return trigrams


def build_text():
    # turn trigram dictionary into text
    h = 0
    x = random.choice(list(trigrams))
    i = random.randint(0, len(trigrams[x]) - 1)
    y = str(trigrams[x][i])
    x = list(x)
    x.append(y)
    b = x
    sentence = x[-2:]
    while h < 100:
        pair = sentence[h:h+2]
        tuple_key = tuple(pair)
        if tuple_key not in trigrams:
            word = random.choice(sentence)
        else:
            word = random.choice(trigrams[tuple_key])
        sentence.append(word)
        h += 1
    return ' '.join(sentence)
      
     

if __name__ == "__main__":

    trigrams = build_trigrams(read_book())
    #print(trigrams)
    build_text()
    print(build_text())
    #print(secret_data)



