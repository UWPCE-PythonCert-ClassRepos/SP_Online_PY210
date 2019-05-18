import sys

# clean up text sent into trigram application
def sanitize_text(words):
    # list of invalid characters to strip out
    invalid_chars = [",",".","-","(",")","[","]","--","#","!","+"]
    # split string on whitespace and create a list
    wall_of_text = words.split()
    count = 0
    # loop through the length of the text
    # and remove all invalid characters
    while count <= len(wall_of_text) - 1:
        for i in invalid_chars:
            # if invalid character found in string
            # replace that index with the new string
            if i in wall_of_text[count]:
                wall_of_text[count] = wall_of_text[count].replace(i, " ")
        count+=1

    # make a long string out of the list
    wall_of_text = " ".join(wall_of_text)
    # then split string based on whitespace and then 
    # dump it back into the original list created
    words = wall_of_text.split()

    return words

words = '''One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own.'''

def get_word_pair():
    word_pair = []

    item1 = input("Enter first word: ")
    item2 = input("Enter second word: ")

    word_pair.insert(0, item1)
    word_pair.insert(1, item2)

    return word_pair

def auto_word_pair(words):
    auto_pair = []
    auto_pair.insert(0, words[0])
    auto_pair.insert(1, words[1])

    return auto_pair

def trigram(word_pair,words):
    word_after= []
    word_length = len(words)
    count = 0
    first_element = 0
    second_element = 1
    
    while count <= len(words) - 1:
        for i in range(word_length - 2):
            if i + 1 <= word_length:
                match = [words[first_element + i], words[second_element + i]]
                print("matchings: ",match)
            if match == word_pair:
                word_after.append(words[i +2])
                print("words after match: ", word_after)
        count+=1
        first_element+=1
        second_element+=1
    return word_after

if __name__ == '__main__':
    my_list = sanitize_text(words)
    pair_list = auto_word_pair(my_list)
    print(trigram(pair_list,my_list))