##!/usr/bin/env python3

#+----------------------------------------------+
#| Mailroom Part 5 (Object Oriented) - Lesson 9 |
#+----------------------------------------------+

import sys, os.path


def write_file(fname,text):
    try:                            # Catch File Open Exceptions
        file = open(fname,'w')
    except (OSError, IOError):
        print("File Open Error for: ",fname)
    
    try:                            # Catch File Write Exceptions
        file.write(text)
        file.close()
        # print("written: ", fname)
        return("written: "+fname)
    except (OSError, IOError):
        # print("File Write Error for: ",fname)
        return("File Write Error for: " + fname)


## === class donor replacing a database record
class Donor(object):
    name =""
    record = []
       
    # constructor to be called with non-empty arguments
    def __init__(self, name="", record = []):
        self.name = name.title()
        self.record =record
    
    # setter to change values
    def set(self, name="", record = []):
        self.name = name.title()
        self.record = record
    
    # return as dict
    def get(self):
        return {self.name: self.record}
    
    # add donation
    def add_donation(self, donation = 0.0):
        self.record.append(donation)
    
    def get_totals(self):
        return [sum(self.record), len(self.record), sum(self.record)/len(self.record)]    

    
    def get_donations_count(self):
        return len(self.record)

    
    def get_donations_total(self):
        return sum(self.record)
    
    
    def get_donations_average(self):
        return sum(self.record)/len(self.record)
        
    
    def gen_letter(self):
        template = "Dear {name},\n\n\tThank you for your very kind donation of ${amount}.\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t   -The Team."
        letter = template.format(name=self.name,amount=self.record[-1])
        return letter

    # return specific parameters, as property to get rid of ()
    @property  
    def donations_count(self):
        return len(self.record)

    @property  
    def donations_total(self):
        return sum(self.record)
    
    @property      
    def donations_average(self):
        return sum(self.record)/len(self.record)
        
    @property  
    def letter(self):
        # template = "Dear {name},\n\n\tThank you for your very kind donation of ${amount}.\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t   -The Team."
        # letter = template.format(name=self.name,amount=self.record[-1])
        return self.gen_letter()

    def save_letter(self):
        filename = "_".join(self.name.split())+".txt"
        return write_file(filename,self.letter)
# === Donor Class end ============


# === DonorCollection Class begin ===

class DonorCollection(object):
    donors = []
    
    def add(self, new_donor):
        self.donors.append(new_donor)
    
    #     list all donors using the print() function
    def __str__(self):
        res = ''
        for item in self.donors:
            res += str(item.get()) + "; \n"
        return res
    
    # find a Donor by name
    def find(self, name):
        for item in self.donors:
            if name in item.get():
                return(item)   # need to return an object to be able to use methods
                break
        return(None)
    
    def print_list(self):
        res = ''
        for item in self.donors:            
            res += f"\t{item.name}: {item.record}\n"
        return(res)

    # as attribute
    @property
    def list(self):
        return(self.print_list())

    def create_report(self):
        # Create header, divider, and formating strings
        headers = ("Donor Name","Total Given","Num Gifts","Average Gift")        
        hfmt = " {:<25s}|{:>15s}|{:^12s}|{:>15s}" # Header formatting
        valfmt = " {:<25s}|${:>14.2f}|{:^12n}|${:>14.2f}" # value records formatting
        slength = 70        
        headerstr = hfmt.format(*headers)
        divstr = " "+"-"*slength
        header = "\n" + divstr +"\n" + headerstr + "\n" + divstr
        
        # bild table as string
        tabstr = ''
        for item in self.donors: # each item is a donor object
            tabstr += valfmt.format(item.name,item.donations_total,item.donations_count,item.donations_average) + "\n" # as properties
            # tabstr += valfmt.format(item.name,item.get_donations_total(),item.get_donations_count(),item.get_donations_average()) + "\n" # as methods
        
        tabstr += divstr+"\n"
        tabstr = header + "\n" + tabstr
  
        return(tabstr)    

    # as attribute
    @property
    def report(self) :
        return(self.create_report())

   # getter of the 1st, last, and element by index and index overloading
    @property  
    def front(self) :        
        return self.donors[0].get()

    @property  
    def back(self) :
        return self.donors[-1].get()
    
    # returns dict
    def elem(self, idx = -1) :
        return self.donors[idx].get()

    # overload the [] indexing 
    # returns Donor object
    def __getitem__(self, key):
        return self.donors[key] 

    def send_letters(self):
        res = "Sending letters to all donors...\n"
        div = "===--------------------------------------"
        # print letters in sequence
        for item in self.donors:
            res += div + "\n" + item.letter + "\n" + item.save_letter() + "\n"
        return res            

    def add_donation(self, name = "John Doe", amount = 0):
        n_name = name.title()
        n_donor = self.find(name) # n_donor is the reference to the found object and is mutable
        if n_donor: # donor is in collection
            n_donor.add_donation(amount)
        else: # donor not in collection
            self.add(Donor(name, [amount]))              
        result = f"=== Thank You, {n_name}, for the ${amount:0.2f} donation! ==="        
        return result     

# === DonorCollection Class end ===
    

# ===== Sanity Checks ==================================
# Can be deleted before submission

# current directory for file operations
cur_dir = os.getcwd()

os.chdir(cur_dir) # change to my working directory


if __name__=="__main__":
    ndonor = Donor("Alfred N. Whitehead", [153, 139])
    print(ndonor.get())
    
    print(ndonor.name)
    print(ndonor.record)
    # ndonor.add_donation(700)
    ndonor.add_donation(32)
    print(ndonor.get())
    # print(ndonor.gen_letter()) # as methods
    print(ndonor.letter) # as property
    
# as methods    
    print(ndonor.get_totals())
    print(ndonor.get_donations_count())
    print(ndonor.get_donations_total())
    print(ndonor.get_donations_average())
    
# as properties        
    print(ndonor.donations_count)
    print(ndonor.donations_total)
    print(ndonor.donations_average)
    
    
    print("====== Donor Collections ======")
    ndonors = DonorCollection()
    ndonors.add(ndonor)   # adds the ndonor, but doesn't change it
       
    
    for item in ndonors.donors:
        print(item.get())
    
    ndonors.add(Donor("Ilya Prigogine", [10,15,20]))
    print("-->           +++")
    print(ndonors.donors[1].get())
    
    print(ndonors)
    
    
    ndonors.add(Donor("Aleksandr Kholmogorov", [7,11,13,3]))
    
    print(ndonors.front)
    print(ndonors.back)
    print(ndonors[1].get())
    print(ndonors.elem(1))
    
    print("=== Find ====\n")
    print(ndonors.find('Ilya Prigogine').get())
    print(ndonors.find('Aleksandr Kholmogorov').get_totals())
    print(ndonors.find('New Guy'))
    
    
    print("===Print List===")
    print(ndonors.print_list())
    print("------------")
    
    print(ndonors.list)
    
    
    print("===Print Report===")
    print(ndonors.create_report())
    print("---------------")
    print(ndonors.report)
    
    print("===Save Letter===")
    print(ndonor.save_letter());
    
    print("===Send Letters===")
    print(ndonors.send_letters())
    print("=============================================================")
    
    print(ndonors.list)
    print(ndonors.add_donation("Ilya Prigogine", 100))
    print(ndonors.add_donation("Donald Trump", 777000))
    print(ndonors.list)
    
    ndonor.set('jane doe', [1,2,3])
    print(ndonor.get())