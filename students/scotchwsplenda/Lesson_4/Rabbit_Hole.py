import random

with open('Alice_In_Wonder.txt', 'r', encoding='utf8') as all_the_words:
    # https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/
    bad_punct=['.','*','(',')','!',',','?','--','[',']']
    all_the_words = all_the_words.read()
    for i in bad_punct:
        all_the_words=all_the_words.replace(i,'')
    # https://stackoverflow.com/questions/12572362/get-a-string-after-a-specific-substring/12572391
    # didn't work after the replace
    split_it = all_the_words.split()

dicty={}
for i in range(len(split_it)-2):
    pair=split_it[i:i+2]
    follower=[split_it[i+2]]
    if tuple(pair) not in dicty:
        dicty[tuple(pair)]=follower
    else:
        # https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
        dicty[tuple(pair)].extend(follower)


# started words
story_bory=['She','had']

# I don't know why this works even when the last two words might not be a key in dicty
j=0
while j < 100:
    last_two=story_bory[-2:]
    story_bory.append(random.choice(dicty.get(tuple(last_two))))
    j+=1


# insert punctuation every 13th word
good_punct=['. ','. ','. ','. ','! ','? ']
for x,z in enumerate(story_bory):
    if x%13==0:
        story_bory.insert(x,random.choice(good_punct))


# write it to a text file.
# don't know how to make punctuation not have a space in front
# don't know how to get rid of weird question mark things
with open('Bad_Alice.txt', 'w') as outfile:
    outfile.writelines(' '.join(story_bory))

'''
RANDOM NOTES A SCRIBBLES
# print(random.choice(dicty[tuple(fake_story[:2])]))

# # fake_story.append(random.choice(dicty[tuple(fake_story)]))
# fake_story.append(random.choice(dicty.get(tuple(fake_story[:2]))))
# print(fake_story)

# print(dicty[tuple(fake_story)]) '''why does this print the values from the dictionary and not the key or the pair'''

# print(list(dicty.keys())[0])
# print(random.randint(0,1100))
# print(dicty[tuple(fake_story)])

# ,dicty[random.randint(0, len(trigrams[x]) - 1]])
# look at last two words in the list
# see if thats a key in dicty
# if so pick a random item from the value and append to the list, retun to beginning of loop
# if not append a random word
# print(random.choice(list(dicty.items())))
# does the order of the key tuple matter?
# print(random.choice(list(dicty.keys())))
# print(random.choice(list(dicty.items())))
# print(random.choice(list(dicty.values())))
'''
