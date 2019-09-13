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
donor_ls = [['Marge',[50,40]],['Harold',[100,1000,10000]],['Henry',[2]],['Myrtle',[5,0.5,.05]],['Mitchell',[3,6,9]]]        
    
donor_list = Donors(['Marge','Harold','Henry','Myrtle','Mitchell'],
                    [[50,40],[100,1000,10000],
                     [2],[5,0.5,.05],[3,6,9]])

# Avoided separate functions within else statements since there are nuanced differences
def send_thanks(donor_ls):
    name_response = input("Type full name: ")
    while True:
        donors = [item[0] for item in donor_ls]
        if name_response == "list":
            print([item[0] for item in donors])
        elif name_response in donors:
            donor_index = donors.index(name_response)
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_ls[donor_index][1].append(donation_response)      
            break
        else:
            donor_ls.append([name_response,[]])
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_ls[-1][1].append(donation_response)
            break
    print("Esteemed {}, thank you for your generous donation".format(name_response))


def create_report(donor_ls):
    for i in donor_ls:
        i.append(sum(i[1]))
        i.append(np.mean(i[1]))
        i.append(len(i[1]))
    sorted_donor = sorted(donor_ls,key = itemgetter(1),reverse=True)
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    
    print('{:<16}| {:^14}|{:^14}| {:^14}'.format(*headers))
    print('-'*65)
    for i in sorted_donor:
        print('{:<18} ${:>12,.2f} {:>14}   ${:>12,.2f}'.format(i[0],i[2],i[4],i[3]))
   

    
    
if __name__ == "__main__":
    while True:
        response = 0   
        while response not in [1,2,3]:
            response = int(input("1. Send a thank-you\n2. Create a report\n3. Quit\n"))
        
        if response == 1:
            send_thanks(donor_ls)
        elif response == 2: 
            create_report(donor_ls)
        else:
            break
        












