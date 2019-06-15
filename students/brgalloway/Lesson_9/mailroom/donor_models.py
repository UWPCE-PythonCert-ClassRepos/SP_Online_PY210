
class Donor(object):
   '''
   Donor class takes a fullname to initiate a single donor. 
   Each donor has three attributes: total donated, number of donations, and average donation
   '''
   def __init__(self, fullname):
      self.fullname = fullname
      self.donation_total = 0
      self.times_donated = 0
      self.average_donation = 0
      
   def __repr__(self):
      # Prints out the object in dictionary format
      # TODO output Donor object as dictionary to match representation
      return f"{{\"{self.fullname}\": {{\"donation_total\": {self.donation_total:.2f}, \"times_donated\": {self.times_donated}, \"average_donation\": {self.average_donation:.2f}}}"
       
   @property
   def donate(self):
      # returns the donation total amount
      return self.donation_total
   
   @donate.setter
   def donate(self, donation):
      # calculates all donor attribute actions
      self.donation_total = donation + self.donation_total
      self.times_donated+=1
      self.average_donation = self.donation_total / self.times_donated
      self.donor_attributes = [self.fullname, self.donation_total, self.times_donated, self.average_donation]

   # TODO Fix to properly function as an alternative constructor 
   @classmethod
   def from_donor(cls, fullname, donation_total, times_donated=1):
      # alternative constructor
      cls.fullname = fullname
      cls.donation_total = donation_total
      cls.times_donated = times_donated
      cls.average_donation = donation_total / cls.times_donated
      cls.donor_attributes = [fullname, donation_total, cls.times_donated, cls.average_donation]
   
      return  cls
   
   def __lt__(self, other):
      return self.donation_total < other.donation_total

   def send_thankyou(self):
      pass

class DonorCollection(object):
   '''
   A collection of donors and the donations contributed
   '''
   # TODO replace list with dictionary
   def __init__(self):
      self.donor_list = []

   def __iter__(self):
      return self.donor_list.__iter__()

   def append(self, donor):
      self.donor_list.append(donor)
   
   def search(self, fullname):
      self.fullname = fullname
      for i in self.donor_list:
         if i.fullname == fullname:
            print(i.fullname + " found in database.")   
         else:
            return print(fullname, "not in database")

   def sort_donors(a_list):
    return self.donor_list[0].donation_total

   def generate_report(self):
      '''
      Generate report based on menu choice
      and return user to the menu prompt  
      '''  
      print("{:<20}|{:^15}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
      print("-" * 70)

      # print(self.donor_list[0].donation_total)
      self.donor_list.sort(key=lambda x: self.donor_list.donation_total)
      print([item.donation_total for item in donor_list])

      for donors in self.sorted_list:
         name = donors.fullname 
         total = donors.donation_total
         times = donors.times_donated
         average = donors.average_donation
         print(f"{name:<20}${total:>14.2f}{times:^18}${average:>12.2f}".format())
         
      
   def __repr__(self):
      return self.donor_list

   def bulk_thankyou(self):
      pass


