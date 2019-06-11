# from mailroom_oo import database as db

class Donor(object):

   def __init__(self, fullname):
      self.fullname = fullname
      
      self.times_donated = 0
      self.average_donation = 0

   def __repr__(self):
      return "{{\"{}\":{{{}, {}, {}}}".format(self.fullname,self.donation_total, self.times_donated, self.average_donation)
   
   @property
   def donated(self):
      return self.donation_total
   
   @donated.setter
   def donated(self, donation):
      self.donation_total = 0
      self.donation = donation
      self.donation_total = self.donation_total + self.donation
      self.times_donated+=1
      self.average_donation = self.donation_total / self.times_donated

   @classmethod
   def from_donor(cls, fullname, donation):
      pass
  
   def send_thankyou(self):
      pass
