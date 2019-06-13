# from mailroom_oo import database as db

class Donor(object):
   '''
   Donor class takes a fullname to initiate donor. 
   '''
   def __init__(self, fullname):
      self.fullname = fullname
      self.times_donated = 0
      self.donation_total = 0
      self.average_donation = 0
      
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

   @classmethod
   def from_donor(cls, fullname, donation):
      pass
  
   def send_thankyou(self):
      pass
