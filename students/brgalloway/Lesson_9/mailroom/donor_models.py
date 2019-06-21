
class Donor(object):
   '''
   Donor class takes a fullname to initiate a single donor. 
   Each donor has three attributes: total donated, number of donations, and average donation
   '''
   def __init__(self, fullname, donation):
      self.fullname = fullname
      self.donation_total = donation
      
   def __repr__(self):
      # Prints out the object in dictionary format
      # TODO output Donor object as dictionary to match representation
      return f"[{self.sum_of_donations:.2f}, {self.times_donated}, {self.average_donation:.2f}]"

   def __lt__(self, other):
         # allow the donations to be sorted
         return self.donation_total < other.donation_total

   @property
   def times_donated(self):
      # return the length of the list to automatically 
      # calculate the number of total donations
      return len(self.donation_total)
   
   @property
   def sum_of_donations(self):
      # returns the sum for string formatting
      return sum(self.donation_total)

   @property
   def average_donation(self):
      # returns the average for string formatting
      return  self.sum_of_donations / self.times_donated

   def apply_donation(self, donation):
      # append a donation to the list of donations
      self.donation_total.append(donation)

   
   def send_thankyou(self):
      '''Send email to a single donor showing their single donation'''
      email_output = []
      email_template = "\n".join((f"Dear {self.fullname},\n\nThank you for your very kind donations this year totaling at ${self.sum_of_donations:.2f}.\n",
                     "It will be put to very good use.\n",
                     "Sincerely,",
                     "-The Team"))
         
      filename = self.fullname.replace(" ","_") + ".txt"

      if "," in filename:
         filename = filename.replace(",","") + ".txt"
         with open(filename.replace(" ", "_"), "w") as file:
               email_output.append(filename)
               file.write(email_template)
      else:
         with open(filename, "w") as file:
               email_output.append(filename)
               file.write(email_template)

      return email_output

class DonorCollection(object):
   '''
   A collection of donors and the donations contributed. 
   Donor Collection can also be used to send an email to 
   all donors. 
   '''
   def __init__(self, *args):
      '''
      initailizes with a list to hold donors and their information
      as well as a tracking variable
      '''
      self.donor_list = {d.fullname: d for d in args}
      self.new_user = False

   def __iter__(self):
      # allows the list to be iterated over
      return self.donor_list.__iter__()

   def __len__(self):
      # used to loop over database
      return self.donor_list.__len__()

   def apply_donation(self, name, donation):
      if self.donor_list.get(name):
      # if user exists add donation to list
         self.donor_list[name].apply_donation(donation)
      else:
      # add donor if it does not exist
         self.donor_list[name] = Donor(name, donation)

   def generate_report(self):
      '''
      Generate report based on menu choice
      and return user to the menu prompt  
      '''  
      print("{:<20}|{:^15}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
      print("-" * 70)
  
      for donors in self.donor_list.values():
         name = donors.fullname
         total = donors.sum_of_donations
         times = donors.times_donated
         average = donors.average_donation
         print(f"{name:<20}${total:>14.2f}{times:^18}${average:>12.2f}")
          
   def bulk_thankyou(self):
      '''Send email to all donors showing their total donations'''
      for donors in self.donor_list.values():
         donors.send_thankyou()
    
