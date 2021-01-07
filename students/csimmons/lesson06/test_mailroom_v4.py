#!/usr/bin/env python

import mailroom_v4 as mail
import pathlib
import os


test_info = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

file_info = [
        ['Count_Dracula.txt','Count Dracula', 10000 ],
        ['Count_Chocula.txt','Count Chocula', 50000 ],
        ['Mr_Nosferatu.txt','Mr Nosferatu', 30000 ],
        ['Count_Yorga.txt','Count Yorga', 45000 ]
            ]

def test_create_dir():
    directory = 'letters'
    dir_exists = os.path.isdir(directory)
    mail.create_dir()
    assert dir_exists == True

def test_write_files():
    mail.write_files('Jane_Doe.txt', 'Jane Doe', 1000)
    assert os.path.exists('Jane_Doe.txt') == True
    
def test_batch_thanks():
    file_names = ['Mary_Newcomer.txt', 'Christine_Ruotolo.txt', 'Martin_Acevedo.txt', 'Sutton_Keaney.txt', 'David_Basilio.txt', 'Andrew_Laughlin.txt', 'Hussein_Saffouri.txt']
    mail.batch_thanks()
    for file in file_names:
        file = 'letters/' + file
        print(file)
        assert os.path.exists(file)

def test_find_donor():
    found = 'Christine Ruotolo'
    lost = 'Craig Simmons'
    assert found in test_info.keys()
    assert lost not in test_info.keys()

def test_list_donors():
    mail.list_donors()
    list1 = list(test_info.keys())
    list2 = list(mail.donorlist_dict.keys())
    assert list1.sort() == list2.sort()



