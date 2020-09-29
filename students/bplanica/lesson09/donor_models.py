#!/usr/bin/env python3

# ------------------------------ #
# Lesson 9 (Mailroom OO) for Python 210
#   Donor and Donor Collection class models
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 10/23/2019, Created module - refactor from mailroom4.py
# ------------------------------ #
from operator import attrgetter, itemgetter

# Donor Model #
###############

class Donor():
    """Class"""

    def __init__(self, donor_id, name):
        self.id = int(donor_id) #primary key for donor databases
        self.name = name
        self._donations = []

    def add_donation(self, *args):
        """add/append a donation amount to a Donor obj"""
        for amt in args:
            self._donations.append(amt) 

    def __repr__(self):
        """only print donor name"""
        return self.name


# DonorCollection Model#
########################

class DonorCollection():
    """class to store and manage Donor objects"""

    def __init__(self, donors=[]):
        self.collection = donors


    def append_collection(self, donor_obj):
        """append a new donor to the collection"""
        self.collection.append(donor_obj)


    def __repr__(self):
        """print the donor id, donor name, and the list of donations"""
        for obj in self.collection:
            print(obj.id, obj.name, obj._donations)
        return ""


    def list_current(self):
        """list the current working donors"""
        header = "\nDonorID, DonorName\n------------------\n"
        data = ""
        self.collection.sort(key = attrgetter('id'), reverse=False) #sort by donor id
        for obj in self.collection:
            data = data + f"{obj.id}, {obj.name}\n"
        return header + data


    def create_obj(self, name):
        """create a new donor and append it to the collection"""
        donor = Donor(self.next_id(), name) #create donor obj
        self.append_collection(donor) #append to collection


    def next_id(self):
        """determine the next donor id"""
        try:
            self.collection.sort(key = attrgetter('id'), reverse=False) #sort by donor id
            last = self.collection[-1].id + 1 #find last id and add 1
        except IndexError:
            last = 1 #no existing objects, id should be 1
        return last


    def save_changes(self):
        """save changes made to the collection to the databases"""
        obj_file_name = "./DonorNamesDB.txt"
        with open(obj_file_name, "w") as outfile:
            outfile.write("DonorID, DonorName\n") #add header line
            for obj in self.collection:
                outfile.write(f"{obj.id}, {obj.name}\n") #save changes by overwriting

        obj_file_name = "./DonationsDB.txt"
        with open(obj_file_name, "w") as outfile:
            outfile.write("DonorID, DonationAmt\n") #add header line
            for obj in self.collection:
                for item in obj._donations:
                    outfile.write(f"{obj.id}, {item}\n") #save changes by overwriting


    def send_one(self, donor_id):
        """write a thank you letter to be sent to the donor"""
        for obj in self.collection:
            if donor_id == obj.id:
                name = obj.name
            try:
                donation = obj._donations[-1] #get the most recent donation
            except:
                donation = 0
                frequency = self.ordinal_freq(len(obj._donations)) #find the ordinal frequency
                total = self.total_given(obj._donations) #find the sum - total amount given
        
        obj_file_name = f"./{obj.name}_Thank You.txt" #save in the working directory
        with open(obj_file_name, "w") as outfile:
            outfile.write(f"""Dear {name},

    We are reaching out to thank you for your {frequency} donation. We appreciate your 
    continued support. You have donated a total of {total:.02f} USD. Your recent docation 
    of {donation:.02f} USD will go towards clean food and water for your local citizens 
    in need.

    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team""") #write the letter to the donor and save the file


    def ordinal_freq(self, fq):
        """convert the number of times donated to an ordinal number"""
        if fq == 1 or (fq % 10 == 1 and fq != 11):
            fq = (f"{fq}st") #format with 'st'
        elif fq == 2 or (fq % 10 == 2 and fq != 12):
            fq = (f"{fq}nd") #format with 'nd'
        elif fq == 3 or (fq % 10 == 3 and fq != 13):
            fq = (f"{fq}rd") #format with 'rd'
        else:
            fq = (f"{fq}th") #format with 'th'
        return fq


    def total_given(self, donations):
        """calculates the total amount donated by a donor"""
        total_sum = sum(donations) #sum all entries in the obj._donation list
        return total_sum


    def send_all(self):
        """write a thank you letter to all donors - mailer"""
        for obj in self.collection:
            switch = ""
            name = obj.name
            try:
                donation = obj._donations[-1] #get the most recent donation
            except IndexError:
                switch = "Found"
            total = self.total_given(obj._donations) # find the sum for the total amount given
            if switch != "Found":
                obj_file_name = f"./{obj.name}_Mailer.txt" #save in the working directory
                with open(obj_file_name, "w") as outfile:
                    outfile.write(f"""Dear {name},

    We are reaching out to thank you for your continued support.

    You have donated a total of {total:.02f} USD. Your recent docation 
    of {donation:.02f} USD will go towards clean food and water for your local citizens 
    in need.

    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team""") #write the letter to the donor in a txt file and save the file


    def create_report(self):
        """create a summarized report"""
        report_items = [] #define/empty list
        for obj in self.collection:
            name = obj.name #get the name
            total = round(self.total_given(obj._donations), 2) #get the total donation amount
            count = len(obj._donations) #find the number of donations
            if count == 0:
                avg = 0
            else:
                avg = round(total/count, 2) #take the average
            report_items.append((name, total, count, avg)) #create a new list with summation information

        header = "\nDonor Name                    |Total Given    |Num Gifts |Average Gift   "
        header2 = "\n-------------------------------------------------------------------------\n"
        data = ""
        for row in sorted(report_items, key=itemgetter(1), reverse=True): #sort by highest total
            total_format = f"{row[1]:.02f}" #format total as float
            avg_format = f"{row[3]:.02f}" #format avg as float
            data = data + ("{:<30}|{:>15}|{:>10}|{:>15}\n".format(row[0], total_format, row[2], avg_format))
            #compile all info into string to return/print
        return header + header2 + data

