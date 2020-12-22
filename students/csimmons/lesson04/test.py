#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
def write_text(my_dict):    
    first, second = random.choice(list(my_dict.keys()))
    list_of_words = [first, second] 
    sen_len = random.randint(5,(len(my_dict.keys())-3))
    while len(list_of_words) < sen_len:
        new_start = tuple(list_of_words[-2:])
        if new_start in my_dict.keys():
            list_of_words.append(random.choice(list(my_dict[(list_of_words[-2], list_of_words[-1])])))
        else:
            list_of_words.append(random.choice(list(my_dict.values())))

        
    return " ".join(list_of_words).capitalize()






input = 'small.txt'
def main(input):
    trigram ={}
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '')
            clean_line = line.split(' ')
            print(len(clean_line))
            print(clean_line, '\n')
            #for i in range(len(clean_line)-2):
            for i in range(10):
                pair = clean_line[i:i+2]
                follower = clean_line[i+2]
                trigram[tuple(pair)] = follower
                #print(clean_line)
                #print(pair)
                #print(follower)clear
            print(trigram)

               

        

if __name__ == '__main__':
    main(input)