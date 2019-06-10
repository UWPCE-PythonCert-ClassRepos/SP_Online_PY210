
class Donor(object):

   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      
   @property
   def fullname(self):
      return f"{self.first_name} {self.last_name}"
   
   @property.setter
   def fullname(self, name):
      first, last = name.split(' ')
      self.first = first
      self.last = last
   

      
     