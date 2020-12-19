#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/13/2020 - csimmons
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