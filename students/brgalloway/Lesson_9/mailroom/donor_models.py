# from mailroom_oo import database as db
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
   def calculate_donations(self):
      # returns the donation total amount
      return self.donation_total
   
   @calculate_donations.setter
   def calculate_donations(self, donation):
      # calculates all donor attribute actions
      self.donation_total = donation + self.donation_total
      self.times_donated+=1
      self.average_donation = self.donation_total / self.times_donated
      self.donor_attributes = [self.fullname, self.donation_total, self.times_donated, self.average_donation]

   @classmethod
   def from_donor(cls, fullname, donation_total, times_donated=1):
      # alternative constructor
      cls.fullname = fullname
      cls.donation_total = donation_total
      cls.times_donated = times_donated
      cls.average_donation = donation_total / cls.times_donated
      cls.donor_attributes = [fullname, donation_total, cls.times_donated, cls.average_donation]
   
      return  Donor.donor_attributes

   def send_thankyou(self):
      pass

class DonorCollection(object):
   '''
   A collection of donors and the donations contributed
   '''
   def __init__(self, donor):
      self.donor = donor

   def new_donor(self):
      pass
   def existing_donor(self):
      pass



