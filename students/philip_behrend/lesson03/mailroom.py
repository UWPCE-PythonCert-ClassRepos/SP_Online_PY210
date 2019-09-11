# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:18:06 2019

@author: Philip Behrend
"""
import numpy as np

class Donors:
    def __init__(self,donor,amt_list):
        self.donor = donor
        self.amt_list = amt_list

donor_list = Donors(['Marge','Harold','Henry','Myrtle','Mitchell'],
                    [[50,40],[100,1000,10000],
                     [2],[5,0.5,.05],[3,6,9]])

def send_thanks(donor_list):
    name_response = input("Type full name: ")
    while True:
        if name_response == "list":
            print(donor_list.donor)
        elif name_response in donor_list.donor:
            donor_index = donor_list.donor.index(name_response)
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_list.amt_list[donor_index].append(donation_response)      
            break
        else:
            donor_list.donor.append(name_response)
            donation_response = round(float(input("Type donation amount: ")),2)
            assert donation_response >= 0
            donor_list.amt_list.append([donation_response])
            break
    print("Esteemed {}, thank you for your generous donation".format(name_response))


def create_report(donor_list):
    sum_donations = [sum(i) for i in donor_list.amt_list]
    avg_donations = [np.mean(i) for i in donor_list.amt_list]
    total_donations = [len(i) for i in donor_list.amt_list]
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    
    print('{:<16}| {:^14}|{:^14}| {:^14}'.format(*headers))
    print('-'*65)
    for i, donor in enumerate(donor_list.donor):
        print('{:<18} ${:>12,.2f} {:>14}   ${:>12,.2f}'.format(donor,sum_donations[i],total_donations[i],avg_donations[i]))
   

    
    
if __name__ == "__main__":
    while True:
        response = 0   
        while response not in [1,2,3]:
            response = int(input("1. Send a thank-you\n2. Create a report\n3. Quit\n"))
                  
        if response == 1:
            send_thanks(donor_list)
        elif response == 2: 
            create_report(donor_list)
        else:
            break
        












