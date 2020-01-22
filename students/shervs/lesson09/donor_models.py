class Donor(object):

    def __init__(self, name , donation=None):
        self.name = name
        self.donations =[]
        if donation:
            self.donations.append(donation)
       
    def add_donation(self, new_donation):
        self.donations.append(new_donation)
       
    def sum_donation(self):
        return sum(self.donations)
   
    def num_donation(self):
        return len(self.donations)
   
    def average_donation(self):
        return self.sum_donation()/self.num_donation()

    def __lt__(self, other):
        # compare sum of donations between two donors
        return self.sum_donation() < other.sum_donation()
   
    def __str__(self):
        return f"{self.name:26s} $ {self.sum_donation():10.2f} {self.num_donation():11d}  $ {self.average_donation():11.2f}"
       

class DonorCollection:
   
    def __init__(self):
        self.donors = []
       
    def add_donor(self , donor):
        self.donors.append(donor)
       
    def __str__(self):
        print_list = []
        for donor in self.donors:
            print_list.append(donor.name)
        return '\n'.join(print_list)
   
    def sort(self):
        """Sorts the donors based on donnor's sum of donations."""
        self.donors.sort()
   
shervin = Donor('shervin',23)
hamid = Donor('hamid',2)
print(shervin.name)
print(shervin.donations)
shervin.add_donation(15)
print(shervin.donations)
#print(shervin > hamid)
#d= Donor('shervin')
#d.donation =[]
#d2= Donor('hamid')
#d2.donation = [32,45,1]

#d.add_donation(12)
#d.add_donation(13)
#print(d.donation)
print(shervin.sum_donation())
print(shervin.num_donation())
print(shervin.average_donation(),'\n')
print(shervin)
doncol = DonorCollection()
doncol.add_donor(Donor('mina',456))
doncol.add_donor(Donor('sam',1000))
doncol.add_donor(Donor('moli',100))
print(doncol)
doncol.sort
print(doncol)
#coll = DonorCollection(d)
#print(coll.__dict__())

c= Donor('sam',10)
d= Donor('mina',400)
e= Donor('titi',100)
f= Donor('mo',30)

new_collection = DonorCollection()
print(new_collection.donors)
new_collection.add_donor(c)

new_collection.add_donor(d)
new_collection.add_donor(e)
print(new_collection)
new_collection.donors.sort(reverse=True)
print(new_collection)
