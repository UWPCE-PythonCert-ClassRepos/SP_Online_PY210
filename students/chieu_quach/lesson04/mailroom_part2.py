
# Author     -  Chieu Quach
# Assignment -  Lesson 4
# Exercise   -  Mailroom Part 2
#               Prints list of users from donation_list.
#               Update new record if username is not found in list


import sys

global donation_list, len_donation_list


donation_list = {1: {'full name': 'William Gates III', 'Amount': '653684.49',
                     'num_gift': '2', 'avg_amt': '326892.24'},
                 2: {'full name': 'Mark Zukerberg', 'Amount': '16396.10',
                     'num_gift': '3', 'avg_amt': '5465.37'},
                 3: {'full name': 'Jeff Bezos', 'Amount': '877.33',
                     'num_gift': '1', 'avg_amt': '877.33'},
                 4: {'full name': 'Paul Allen', 'Amount': '708.42',
                     'num_gift': '3', 'avg_amt': '236.14' },
                            
                }

len_donation_list = len(donation_list)
prompt = "\n".join(("Welcome to the Mailroom Part 2",
                    "Please choose from below options: ",
                    "1 - Send a Thank You to a single donor",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>>"))

msg  = ( " Dear {}, "
      "\n\n"
      "\t"  "Thank you for your generous donation of {:5.2f}. "
      "\n"               
      "\t"  "It will be put to very good use.           "
      "\n\n"
      "\t\t\t" "   Sincerely,       "
      "\n"
      "\t\t\t" "    -The Team       "
      "\n\n"
      )

def send_thankyou():
      
  name_found = ""
  e = 1
  # response = input(" Please enter full name ")
  response = input(" Please enter full name ")
  
  for key, value in donation_list.items():
         
         if response == "list":
            
            if e == 1:
              print ("List of Names \n")
            e = e + 1
            list_name = (value['full name'], float(value['Amount']), int(value['num_gift']), float(value['avg_amt']))
         
            print("{:<19} {:14.2f} {:15d}{:=21.2f} ".format(*list_name))
            name_found = "list"         
         elif response == value['full name']:
            
            name_found = "yes"
            fullname = value['full name']
            amount   = value['Amount']
            giftnum  = value ['num_gift']
           
            keynum   = key
            
         else:
            continue

 
  if name_found == "yes":
     nu_amount    =  float(input(" Please Enter Donation Amount: "))
     new_len_list = len(donation_list) + 1         
  
     grand_amount = nu_amount + float(amount)
     
     gift_tot     = int(giftnum) + 1
     amount_avg   = grand_amount / gift_tot
              
     # Update record to reflect new changes made
     new_list = {keynum: {"full name": response, 
                   "Amount": grand_amount, "num_gift": gift_tot, "avg_amt": amount_avg}}          
   #  print ("new_list ", new_list)
     donation_list.update(new_list)
     full_name = response
     # added "_" to last name
     full_name = ("_".join(full_name.split()))
      
     full_name = full_name + ".txt"               
        
     print(msg.format(response, nu_amount))
     # sends text message to output file
     outfile = open(full_name, "w")
     cpy = (msg.format(response,  nu_amount))
     outfile.writelines(cpy)

  elif name_found == "list":
     main()
  else:
      
     nu_amount =  float(input(" Please Enter Donation Amount: z "))
     
     num_gift = 1
          
     # update new length
     new_len_list = len(donation_list) + 1
     # store name and amount into new_list
     new_list = {new_len_list: {"full name": response, 
             "Amount": nu_amount, "num_gift": num_gift, "avg_amt": nu_amount}}          
     # added "_" to last name
     full_name = ("_".join(response.split()))
      
     full_name = full_name + ".txt"         
     #print("msg".format(name_list[0], name_list[1]))
     print(msg.format(response, nu_amount))
     # sends text message to output file
     outfile = open(full_name, "w")
     cpy = (msg.format(response, nu_amount))          
     donation_list.update(new_list)
     outfile.writelines(cpy)
     outfile.close() 

           
def send_letters():

     # reading key and value in list
     # prints list of letters from donation list
      for key, value in donation_list.items():            
    
                   
          amount = float(value['Amount'])                
          name   = value['full name']
          amount = float(value['Amount'])               
          full_name = value['full name']
          # added "_" to last name
          full_name = ("_".join(full_name.split()))
          
          full_name = full_name + ".txt"
         # print ("fullname ", fullname)       
    
          print(msg.format(name, amount))
          outfile = open(full_name, "w")
          cpy = (msg.format(name, amount))
          outfile.writelines(cpy)
         # print ("cpy ", cpy)
       
          outfile.close()
            
      
                          
            
def create_report():
   from operator import itemgetter
   
   name_header  = " Donor Name "
   total_given = " |  Total  Given   |"
   num_gifts    = " Num Gifts      | "
   average_gift = " Average  Gift  " 
   print ("{:15}  {:15}  {:15}  {:15}"
   .format(name_header, total_given, num_gifts, average_gift))
   print (" ------------------------------------------------------------------------")
   # reading key and value in list
   
   for key,value in sorted(donation_list.items()):
     
      list_name = (value['full name'], float(value['Amount']), int(value['num_gift']), float(value['avg_amt']))
         
      print("{:<19} {:14.2f} {:15d}{:=21.2f} ".format(*list_name))

   print ("\n\n\n")
    
   
def exit_program():
   print ("Thanks for visiting ")
   sys.exit()

def main():

       while True:
             # Use switch case to call functions from user input
           switch = {1: send_thankyou,
               2: create_report,
               3: send_letters,               
               4: exit_program,
                          
           }
           
            
           response = input(prompt)
           response = int(response)
           if response in switch:
               switch[response]()
           else:
               print ("Invalid input ")
     

# Main function
if __name__ == "__main__": 
   
   main() 
