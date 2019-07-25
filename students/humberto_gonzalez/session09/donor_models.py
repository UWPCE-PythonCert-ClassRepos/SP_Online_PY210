#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:23:00 2019

@author: Humberto Gonzalez
"""

import os
import pickle
import tempfile

class Donor:
    def __init__(self,name):
        """
        donor is initialized with a name and empty donations list
        """
        self.name = name
        self.donations = []
    
    def add_donation(self,donation):
        """
        adds donation to the donations list
        """
        try:
            donation = float(donation)
            self.donations.append(donation)
        except:
            print("Donation amount entered needs to be a number")
    
    def total_donations(self):
        """
        returns the sum of all the donor's donations
        """
        return sum(self.donations)
    
    def num_donations(self):
        """
        returns the total number of donations made by the donor
        """
        return len(self.donations)
    
    def avg_donation(self):
        """
        returns the average donation amount made by thr donor
        """
        return round(sum(self.donations)/len(self.donations),2)
    
    def generate_thank_you_note(self):
        """
        created the thank you note text for the donor
        """
        donor_name = self.name
        donation = self.donations[len(self.donations)-1]
        txt = f'Dear {donor_name},\n    Thank you for your generous donation of ${donation}'
        return txt
    
    def __lt__(self,other):
        return self.total_donations() > other.total_donations()
    
    def __eq__(self,other):
        return self.total_donations() == other.total_donations()
    

class donorCollection:
    def __init__(self):
        """
        initializes the donor collection as an empty list
        """
        self.donor_db = []
    
    def add_donor(self,donor):
        """
        adds a donor to the donor collection
        """
        self.donor_db.append(donor)
    
    def find_donor(self,name):
        """
        given a donor name, returns the corresponding donor object
        """
        for donor in self.donor_db:
            if donor.name == name:
                return donor
    
    def send_letters(self):
        """
        creates letters to all donors in the donor collection and saves them
        to the temp folder
        """
        path = tempfile.gettempdir()
        path = path + "/" + "Letters to Donors"
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        for donor in self.donor_db:
            donation = donor.donations[0]
            temp = path + "/" + donor.name.replace(' ','_') + '.txt'
            with open(temp,'w') as tfile:
                formatter = '''Dear {},\n    Thank you for your generous donation of ${}. \n    Your donation will be put to great use. \n         Sincerely, \n          -The Organization'''
                txt = formatter.format(donor.name,donation)
                tfile.write(txt)
        print('Letters have been created and saved to \n a new folder in your temp directory')
    
    def display_report(self):
        """
        prints out the report of the donor collection
        """
        print('{:20} | {:^10} | {:^10} | {:^10} |'.format("Donor Name",
              "Total Given","Num Gifts","Average Gift"))
        print('-'*64)
        formatter = "{:20}   ${:>10}   {:>10}   ${:>10}"
        self.donor_db.sort()
        for donor in self.donor_db:
            donor_name = donor.name
            total = donor.total_donations() 
            num = donor.num_donations()
            average = donor.avg_donation()
            print(formatter.format(donor_name,total,num,average))
    
    def save_data(self):
        """
        saves the donor collection to a pickle data file
        """
        directory = os.getcwd()
        with open(directory+"/"+"mailroom.dat", "wb") as f:
            pickle.dump(self.donor_db, f)
            print("Mailroom data has been saved")
    
    def load_data(self):
        """
        loads a donor collection from a pickle data file
        """
        directory = os.getcwd()
        try:
            os.path.exists(directory+"/"+"mailroom.dat")
            with open(directory+"/"+"mailroom.dat") as f:
                self.donor_db = pickle.load(f)
        except:
            print("There is no mailroom save data in the current working directory")
            
                
        
        
    