
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

   
   def send_thankyou(self, fullname, donation):
      '''Send email to a single donor showing their single donation'''
      email_output = []
      email_template = "\n".join((f"Dear {self.fullname},\n\nThank you for your very kind donations this year totaling at ${self.donation:.2f}.\n",
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

   def __repr__(self):
      # Prints full database
      return self.donor_list

   def __iter__(self):
      # allows the list to be iterated over
      return self.donor_list.__iter__()

   def __len__(self):
      # used to loop over database
      return self.donor_list.__len__()

   def __getitem__(self, index):
      # output values at  specific index
      return self.donor_list[index]

   def append(self, donor):
      # append donors to database
      self.donor_list.append(donor)
   
   def search(self, fullname):
      '''
      Search database for users and return true or false
      depending on the user is already in the database or not
      '''
      self.fullname = fullname
      for i in range(len(self.donor_list)):
         if self.donor_list[i].fullname == fullname:
            # found user in database
            self.new_user = False 
            return self.new_user 
      else:
         # did not find user in database
         self.new_user = True 
         return self.new_user

   def generate_report(self, donor_list):
      '''
      Generate report based on menu choice
      and return user to the menu prompt  
      '''  
      self.donor_list = donor_list
      sorted_list = sorted(self.donor_list, reverse=True)

      print("{:<20}|{:^15}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
      print("-" * 70)
  
      for donors in sorted_list:
         name = donors.fullname 
         total = donors.donation_total
         times = donors.times_donated
         average = donors.average_donation
         print(f"{name:<20}${total:>14.2f}{times:^18}${average:>12.2f}".format())
         
   def list_names(self):
      for i in self.donor_list:
         print(i.fullname)
   
   def update_donation(self, fullname, donation_amount):
      '''
      Searches the database looking for the donors name given
      and adds their new contribution to the database
      '''
      self.fullanme = fullname
      self.donation_amount = donation_amount
      for i in range(len(self.donor_list)):
         if self.donor_list[i].fullname == fullname:
            self.donor_list[i].donation_total+=donation_amount
            self.donor_list[i].times_donated+=1
            self.donor_list[i].average_donation = self.donor_list[i].donation_total / self.donor_list[i].times_donated

   def find_donor(self, donor_list):
      '''
      Searches database with the search function, list names in database, and sends email
      '''
      self.donor_list = donor_list
      while True:
         fullname = input("type list to display names or quit to exit to main menu\n" \
                         "Enter full name of donor: ")
         if fullname == "list":
            self.list_names(DonorCollection)
         elif fullname and fullname != "quit":
            try:
               # search database for user and set flag
               self.search(DonorCollection, fullname)
               if self.new_user == False:
                  #update donors inside the database
                  donation_amount = float(input("Donation amount: "))
                  self.update_donation(DonorCollection, fullname, donation_amount)
                  self.send_thankyou(Donor, fullname, donation_amount)
               elif self.new_user == True:
                  # ask the user if they want to add this value to the database
                  print("User not found")
                  add_user = input("Would you like to add a new donor? (yes or no)\n>> ")
                  add_user = add_user.lower()
                  add_user = add_user.strip()
                  if add_user == "yes":
                     # if user wants to add them to the database the perform login and email
                     new_donor = Donor(fullname)
                     self.donor_list.append(new_donor)
                     donation_amount = float(input("Donation amount: "))
                     self.update_donation(DonorCollection, fullname, donation_amount)
                     self.send_thankyou(fullname, donation_amount)
                  else:
                     return
            except ValueError:
               print("not a valid response exiting to donor selection")
               return
         elif fullname == "quit":
            return

   def bulk_thankyou(self, donor_list):
      '''Send email to all donors showing their total donations'''
      email_output = []
      self.donor_list = donor_list
      for i in range(len(self.donor_list)):
         donation_amount = self.donor_list[i].donation_total
         email_template = "\n".join((f"Dear {self.donor_list[i].fullname},\n\nThank you for your very kind donations this year totaling at ${donation_amount:.2f}.\n",
                     "It will be put to very good use.\n",
                     "Sincerely,",
                     "-The Team"))
         
         filename = self.donor_list[i].fullname.replace(" ","_") + ".txt"
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



