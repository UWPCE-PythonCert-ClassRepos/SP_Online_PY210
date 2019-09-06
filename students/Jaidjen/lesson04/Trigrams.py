s= 'I wish I may I wish I might'
words = 'I wish I may I wish I might'.split()

def build_trigrams(words):

    trigrams = dict()
    trigrams['I wish'] = ['I']
    trigrams['wish I'] = ['may']
    trigrams['I may'] = ['I']
    trigrams['may I'] = ['wish']
    trigrams['I wish'].append('I')
    trigrams['wish I'].append('might')

    print("This is a trigrams")
    return trigrams


def word_pair():
    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        print("This is a pair")
        print(pair)
        print("This is the follower")
        print(follower)
        if pair == trigrams:
            print("WORDS")
            print(words[i])
            pair = pair + follower
            words.append(pair)
            print("This is a new set")
            print(words)
        else:
            words.append(pair)
            print("Adding to dic")
            print(words)


def new_words():

    import random
    trigrams = build_trigrams(words)
    new_text=[]
    start_key=random.choice(list(trigrams))
    new_text.append(start_key)
    print("This is the new text")
    print(new_text)
    print("This is the start key")
    print(start_key)
    for i in range(len(trigrams)):
        random.choice(list(trigrams))



if __name__== "__main__":
      trigrams = build_trigrams(words)
      print(trigrams)
      make_words = word_pair()
      print(words)
      new_words()