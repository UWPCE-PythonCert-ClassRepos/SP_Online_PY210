
# Author     -  Chieu Quach
# Assignment -  Lesson 4
# Exercise   -  Mailroom Part 2

import sys
global donation_list, len_donation_list


donation_list = {1: {'first name': 'William', 'last name': 'Gates III', 'Amount': '653684.49',
                     'num_gift': '2', 'avg_amt': '326892.24'},
                 2: {'first name': 'Mark', 'last name': 'Zukerberg', 'Amount': '16396.10',
                     'num_gift': '3', 'avg_amt': '5465.37'},
                 3: {'first name': 'Jeff', 'last name': 'Bezos', 'Amount': '877.33',
                     'num_gift': '1', 'avg_amt': '877.33'},
                 4: {'first name': 'Paul', 'last name': 'Allen', 'Amount': '708.42',
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
      
     
   response = input(" Please enter full name ") 
   for key, value in donation_list.items():
      name   = value['first name'] + " " + value['last name']
      if response == name or response == value['first name']:
                     
          amount = float(value['Amount'])                
          last_name = value['last name']
          # added "_" to last name
          last_name = ("_".join(last_name.split()))
          fullname = value['first name'] + "_" + last_name
          fullname = fullname + ".txt"
          #print ("fullname ", fullname)       
               
          #print("msg".format(name_list[0], name_list[1]))
          print(msg.format(name, amount))
          # sends text message to output file
          outfile = open(fullname, "w")
          cpy = (msg.format(name, amount))
          outfile.writelines(cpy)
          break       
      else:
          if key == len_donation_list:
              print ("Please re-enter name ")
              print ("\n")
              send_thankyou()
              
def send_letters():

     # reading key and value in list
     # prints list of letters from donation list
      for key, value in donation_list.items():            
    
                   
          amount = float(value['Amount'])                
          name   = value['first name'] + " " + value['last name']
          amount = float(value['Amount'])                
          last_name = value['last name']
          # added "_" to last name
          last_name = ("_".join(last_name.split()))
          fullname = value['first name'] + "_" + last_name
          fullname = fullname + ".txt"
         # print ("fullname ", fullname)       
    
          print(msg.format(name, amount))
          outfile = open(fullname, "w")
          cpy = (msg.format(name, amount))
          outfile.writelines(cpy)
         # print ("cpy ", cpy)
       
          outfile.close()
            
      
                          
            
def create_report():

   name_header  = " Donor Name "
   total_given = " |  Total  Given   |"
   num_gifts    = " Num Gifts      | "
   average_gift = " Average  Gift  " 
   print ("{:15}  {:15}  {:15}  {:15}"
   .format(name_header, total_given, num_gifts, average_gift))
   print (" ------------------------------------------------------------------------")
   # reading key and value in list
   for key, value in donation_list.items():            
    
         full_name = value['first name'] + " " + value['last name']    
         list_name = (full_name, float(value['Amount']), int(value['num_gift']), float(value['avg_amt']))
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
