# from mailroom_oo import database as db

class DonorCollection(object):
   '''
   A collection of donors and the donations contributed
   '''
   def __init__(self, fullname):
      pass

   def new_donor(self):
      pass
   def existing_donor(self):
      pass

class Donor(object):
   '''
   Donor class takes a fullname to initiate a single donor. 
   Each donor has three attributes: total donated, number of donations, and average donation
   '''
   def __init__(self, fullname, **kwargs):
      self.fullname = fullname
      self.donation_atttimes_donated = 0
      self.donation_total = 0
      self.average_donation = 0
      self.donordb = {}
      
   def __repr__(self):
      return f"{{\"{self.fullname}\": {{\"donation_total\": {self.donation_total:.2f}, \"times_donated\": {self.times_donated}, \"average_donation\": {self.average_donation:.2f}}}"
       
   @property
   def calculate_donations(self):
      return self.donation_total
   
   @calculate_donations.setter
   def calculate_donations(self, donation):
      self.donation_total = donation + self.donation_total
      self.times_donated+=1
      self.average_donation = self.donation_total / self.times_donated

   # @classmethod
   # def from_donor(cls, fullname, donation):
   #    pass
  
   def send_thankyou(self):
      pass

