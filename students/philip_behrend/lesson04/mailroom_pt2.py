# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:18:06 2019

@author: Philip Behrend
"""
import numpy as np
from operator import itemgetter

class Donors:
    def __init__(self,donor,amt_list):
        self.donor = donor
        self.amt_list = amt_list
        
    def __lt__(self,other):
        return self.amt_list < other.amt_list

# Used class to get practice with concept
donor_dict = {'Marge':[50,40],'Harold':[100,1000,10000],'Henry':[2],'Myrtle':[5,0.5,.05],'Mitchell':[3,6,9]}    
    
donor_list = Donors(['Marge','Harold','Henry','Myrtle','Mitchell'],
                    [[50,40],[100,1000,10000],
                     [2],[5,0.5,.05],[3,6,9]])

# Avoided separate functions within else statements since there are nuanced differences
def send_thanks(donor_dict):
    name_response = input("Type full name: ")
    while True:
        donors = donor_dict.keys()
        if name_response == "list":
            print(list(donors))
        elif name_response in donors:
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_dict[name_response].append(donation_response)      
            break
        else:
            donor_dict[name_response] = []
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_dict[name_response].append(donation_response)
            break
    print("Esteemed {}, thank you for your generous donation".format(name_response))


def create_report(donor_dict):
    metrics = dict.fromkeys(donor_dict.keys(),[])
    for i in metrics:
        temp = [sum(donor_dict[i]),np.mean(donor_dict[i]),len(donor_dict[i])]
        metrics[i] = temp
    sorted_donor = sorted(metrics.items(), key=lambda x: x[1],reverse=True)
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    
    print('{:<16}| {:^14}|{:^14}| {:^14}'.format(*headers))
    print('-'*65)
    for i in sorted_donor:
        print('{:<18} ${:>12,.2f} {:>14}   ${:>12,.2f}'.format(i[0],i[1][0],i[1][2],i[1][1]))
   
def send_all_letters(donor_dict):
    donors = donor_dict.keys()
    for i in donors:
        letter = "Esteemed {}, thank you for your generous donation".format(i)
        filename = '{}.txt'.format(i)
        with open(filename, 'w') as f:
            f.write(letter)
            
def quit_program(donor_dict):
    return "quit"
    
  
if __name__ == "__main__":
    response = 0
    while response != 'quit':
        while response not in [1,2,3,4]:
            response = int(input("1. Send a thank-you to single donor\n2. Create a report\n3. Send Letters\n4. Quit Program\n"))
        
        arg_dict = {1: send_thanks, 2: create_report, 3: send_all_letters, 4: quit_program}
        response = arg_dict.get(response)(donor_dict)
    
'''    
        if response == 1:
            send_thanks(donor_ls)
        elif response == 2: 
            create_report(donor_ls)
        elif response ==3:
            send_all_letters(donor_ls)
        else:
            break
'''       












