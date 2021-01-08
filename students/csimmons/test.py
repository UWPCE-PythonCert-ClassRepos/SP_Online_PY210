#!/usr/bin/env python3
# Craig Simmons
import os

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

def test_create_report():
    all_info = [
                ['Hussein Saffouri', 66100.00, 5, 13220.00],
                ['Andrew Laughlin', 43050.00, 4, 10762.50],
                ['Sutton Keaney', 34000.00, 5, 6800.00],
                ['Christine Ruotolo', 29750.00, 4, 7437.50],
                ['Mary Newcomer', 12800.00, 3, 4266],
                ['David Basilio', 9500.00, 7, 1357.14],
                ['Martin Acevedo', 7000.00, 2, 3500],
                ]
    test_info = [
                ['Hussein Saffouri', 66100.00, 5, 13220.00],
                ['Andrew Laughlin', 43050.00, 4, 10762.50],
                ['Sutton Keaney', 34000.00, 5, 6800.00],
                ['Christine Ruotolo', 29750.00, 4, 7437.50],
                ['Mary Newcomer', 12800.00, 3, 4266.67],
                ['David Basilio', 9500.00, 7, 1357.14],
                ['Martin Acevedo', 7000.00, 2, 3500],
                ]
    for i in range(len(test_info)):
        expected = list(test_info[i])
        created = list(all_info[i])
        if expected == created:
            print(True)
        print(expected)
        print(created)
test_create_report()


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

def test_batch_thanks():
    file_names = ['Mary_Newcomer.txt', 'Christine_Ruotolo.txt', 'Martin_Acevedo.txt', 'Sutton_Keaney.txt', 'David_Basilio.txt', 'Andrew_Laughlin.txt', 'Hussein_Saffouri.txt']
    for file in file_names:
        new_file = 'letters/' + file
        print(new_file)
        print(file)
        print(os.path.exists(file))

#test_batch_thanks()

def test_create_report():
    test_info = [
                ['Hussein Saffouri', 66100.00, 5, 13220.00],
                ['Andrew Laughlin', 43050.00, 4, 10762.50],
                ['Sutton Keaney', 34000.00, 5, 6800.00],
                ['Christine Ruotolo', 29750.00, 4, 7437.50],
                ['Mary Newcomer', 12800.00, 3, 4266.67],
                ['David Basilio', 9500.00, 7, 1357.14],
                ['Martin Acevedo', 7000.00, 2, 3500],
                ]
    all_info = mail.create_report()
    for i in range(len(test_info)):
        expected = list(test_info[i])
        created = list(all_info[i])
        created[2] = created[2]
        created[4] = created[4]
        assert expected == created
        
   def fake_input(prompts):
        user_data = {'donor' : 'Craig Simmons',
                    'gift': 100
                }
    values = user_data[prompts]
    return values
   
   
   