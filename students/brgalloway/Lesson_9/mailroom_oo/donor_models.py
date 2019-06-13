# from mailroom_oo import database as db

class Donor(object):

   def __init__(self, fullname, donation):
      self.fullname = fullname
      self.donation = donation
      # on creation set donations total to 0
      # self.donation_total = 0
      self.times_donated = 0
      self.average_donation = 0
   
   def __repr__(self):
      return "\"{}\": {{{}, {}, {}}}".format(self.fullname, self.donation_total, self.times_donated, self.average_donation)
   
   @property
   def donation_total(self):
      return self.donation_total
   
   @donation_total.setter
   def donation_total(self, donation):
      self.donation = donation
      self.donation_total = self.donation_total + self.donation
      self.times_donated+=1
      self.average_donation = self.donation_total / self.times_donated

   @classmethod
   def from_donor(cls, fullname, donation):
      pass
  
   def send_thankyou(self):
      pass
