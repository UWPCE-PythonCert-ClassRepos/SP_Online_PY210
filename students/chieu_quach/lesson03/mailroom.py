
# Author     -  Chieu Quach
# Assignment -  Lesson 3
# Exercise   -  Mailroom Part 1

import sys
global donation_list, len_donation_list
donation_list = {}
donation_list = [("William Gates III", 653784.49, 2, 326892.24),
                 ("Mark Zukerberg", 16396.10, 3, 5465.37),
                 ("Jeff Bezos", 877.33, 1, 877.33),
                 ("Paul Allen", 708.42, 3, 236.14),
                ]
         # donation_list [] [] - to access name enter [1][0]
         # the name (like Bill Gates) locates at [0]

len_donation_list = len(donation_list)
prompt = "\n".join(("Welcome to the Mailroom Part 1",
                    "Please choose from below options: ",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>>"))

from operator import itemgetter

def send_thankyou():

      from_addr   = "chieu@yahoo.com"
      to_addr     = "@yahoo.com"
      subject     = "Thank you"
      msg  = "Thank you {} for your generous donation of {} "
      msg1 = "An email has been sent to {}"
      total_num_gifts = 0
      total_amount = 0
      fname = ""
      e = 1
      len_donation_list = len(donation_list)
      print ("len_donation_list ", len_donation_list)
      name_found = ""
      response = input(" Please enter full name ") 
      for z in donation_list:
            
            if response == "list":
            
               if e == 1:
                  print ("List of Names \n")
               e = e + 1
               print (z)
               name_found = "list"
            elif response == z[0]:
               name_found = "yes"
               name = z
            else:
               continue
      print ("\n")
      # if donation name is located 
      if name_found == "yes": 
            amount_donate =  float(input(" Please Enter Donation Amount: "))
            
           
            new_amount = name[1] + amount_donate
            new_amount = round(new_amount,2)
            num_gifts    = name[2] + 1
            #print ("new_amount", new_amount)
            avg_amount = new_amount / num_gifts
            
            name_list = (name[0], new_amount, num_gifts, avg_amount)
            # Merge first and lastname without space in between
            fullname = name[0]
            len_name  = len(fullname)
            for u in range(0, len_name):
                if fullname[u] != " ":
                   fname = fname + fullname[u]
                else:
                   continue
            #print ("name_list ", name_list)
            donation_list.remove(name)
            donation_list.append(name_list)
            #print ("name_list ", name_list)
            to_addr = fname + to_addr
            print ("from {} to {} subject {}".format(from_addr, to_addr, subject))
            print (f"Thank you {name_list[0]} for your generous donation of {name_list[1]}")
            print ("\n\n\n")
           
      elif name_found == "list":
            main()
      else:
            amount_donate =  float(input(" Please Enter Donation Amount: "))
           
            num_gifts = 1
            name_list = (response, amount_donate, num_gifts, amount_donate)
            fullname = name_list[0]
            donation_list.append(name_list)
            
            len_name  = len(fullname)
            for u in range(0, len_name):
                if fullname[u] != " ":
                   fname = fname + fullname[u]
                else:
                   continue
            to_addr = fname + to_addr
            print ("\n")
            print ("from {} to {} subject {}".format(from_addr, to_addr, subject))
            print (f"Thank you {name_list[0]} for your generous donation of {name_list[1]}") 
            print ("\n\n\n")
            
                       
            
def create_report():

   
   name_header  = " Donor Name "
   total_given = " |  Total  Given   |"
   num_gifts    = " Num Gifts      | "
   average_gift = " Average  Gift  "

   print ("{:15}  {:15}  {:15}  {:15}"
   .format(name_header, total_given, num_gifts, average_gift))
   print (" ------------------------------------------------------------------------")

   sorted_item = sorted(donation_list, key=itemgetter(1), reverse= True)  
   #print ("sorted_item ", sorted_item)

   for n in sorted_item:
     
      # *n - the * tells python to unpack the tuple into seperate argument
      # {:<14.2f = means to left aligned wi1th 14 print float number
      print("{:<19} {:14.2f} {:14d} {:=21.2f}".format(*n))

   print ("\n\n\n")
    
   
def exit_program():
   print ("Thanks for visiting ")
   sys.exit()

def main():

   while True:
       response = input(prompt)
       if response == "1":
          send_thankyou()
       elif response == "2":
          create_report()
       elif response == "3":
          exit_program()
       else:
          print("Not a valid option!")
          
         


# Main function
if __name__ == "__main__": 
 
   main()
