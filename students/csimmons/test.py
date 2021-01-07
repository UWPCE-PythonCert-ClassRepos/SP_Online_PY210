#!/usr/bin/env python3
# Craig Simmons

def files():
    file_info = [
                ['Count_Dracula','Count Dracula', 10000 ],
                ['Count_Chocula','Count Chocula', 50000 ],
                ['Mr_Nosferatu','Mr Nosferatu', 30000 ],
                ['Count_Yorga','Count Yorga', 45000 ],
                ]

    for position in range(len(file_info)):
        a = file_info[position][0]
        b = file_info[position][1]
        c = file_info[position][2]
        print(a)
        print(b)
        print(c)
        print('\n')

files()