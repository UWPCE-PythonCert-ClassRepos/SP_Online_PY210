
# Author     -  Chieu Quach
# Assignment -  Lesson 5
# Exercise   -  Mailroom Part 3
#               Use exceptions handling and comprehensions

import sys
# from operator import * is declared here for use itemgetter in sort
from operator import *
global donation_list, len_donation_list

donation_list = [{'full name': 'William Gates III', "Amount": 653684.49,
                     "num_gift": "2", "avg_amt": 326892.24},
                 {'full name': 'Mark Zukerberg', 'Amount': 16396.10,
                     'num_gift': '3', 'avg_amt': 5465.37},
                 {'full name': 'Jeff Bezos', 'Amount': 877.33,
                     'num_gift': '1', 'avg_amt': 877.33},          
                 {'full name': 'Paul Allen', 'Amount': 708.42,
                     'num_gift': '3', 'avg_amt': 236.14 }]


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
  
    e = 0
  
    while True:
      
        try:
            fname = input(" Please enter full name \n" 
            "(select list to list report or exit to return to menu) ")
            if fname == "exit":
                break
            if not  fname:
                raise ValueError
            elif fname.isdigit():
                raise TypeError
        except TypeError as e:
            print ("Please re-enter string name ")
            print (e)
        except ValueError as i:
            print ("Please re-enter (empty string)")
            print (i)
        except NameError:
            print ("Name Error")
            print (z)
        else:
            print("fname ", fname)
            name_found = ""
            # newlist = sorted(donation_list, key=itemgetter('Amount'), reverse=True)
            chk_input = [value for  value in donation_list if value['full name'] == fname]        
            if fname == "list":
                e = e + 1
                if e == 1:
                    print ("List of Names \n")
                chk_inputz = [value for  value in donation_list]
                new_chk    = sorted(chk_inputz, key=itemgetter('Amount'), reverse=True)
                chkout = [print("{:<19} {:14.2f}{:^15d}{:=21.2f} ".format(value['full name'],value['Amount'],
                    int(value['num_gift']), value['avg_amt'])) for value in new_chk]
                print ("\n")
                break    
            if not chk_input:
                name_found = "no"
                fullname = fname
            else:
                name_found = "yes"
                fullname = chk_input[0]['full name']
                amount   = chk_input[0]['Amount']
                giftnum  = chk_input[0]['num_gift']
                avg_amt  = chk_input[0]['avg_amt']           
         
            complete = False
            while not complete: 
                try:
                    nu_amount =  float(input(" Please Enter Donation Amount: "))
                except ValueError:
                    print ("Value Error ")
                except IndexError:
                    print ("Index Error ", response)
                except ValueError as e:
                    print ("ValueError ")
                    print (e)
                except KeyError as o:
                    print ("Invalid selection ")
                    print (o)
                else:
                    print ("no Error")
                    print ("nu amount ", nu_amount)
                    # break
                    if name_found == "yes":
                        name = ""
                        new_list = ""
                        new_len_list = len(donation_list) + 1         
                                       
                        grand_amount = nu_amount + float(amount)                                
                        gift_tot     = int(giftnum) + 1
                        amount_avg   = grand_amount / gift_tot
                        name     = {'full name': fname, 'Amount': amount, 'num_gift': giftnum, 'avg_amt': avg_amt}
                        # print("full name ", fullname)
                         
                          # Update record to reflect new changes made
                        new_list = {"full name": fname,
                            "Amount": grand_amount, "num_gift": gift_tot, "avg_amt": amount_avg}            
                      
                        full_name = fname
                        # added "_" to last name
                        full_name = ("_".join(fullname.split()))
               
                        full_name = full_name + ".txt"
                        output_msg = [print(msg.format(fullname, nu_amount))]                
                        donation_list.remove(name)
                        donation_list.append(new_list)             
                          # sends text message to output file
                        with open(full_name, "w") as outfile:
                             outfile.writelines(msg.format(fullname, nu_amount))
                                    
                        outfile.close()
                        complete = True
                        break
               
                    else:
                        # New user
                        # Append new item to list
                        num_gift = 1
            
                        # update new length
                        new_len_list = len(donation_list) + 1                  
                        full_name = ("_".join(fname.split()))          
                        full_name = full_name + ".txt"                           
                        output_msg = [print(msg.format(fullname, nu_amount))]
                        new_listz = {"full name": fname, 
                           "Amount": nu_amount, "num_gift": num_gift, "avg_amt": nu_amount}  
                        # sends text message to output file
                        with open(full_name, "w") as outfile:
                           outfile.writelines(msg.format(fullname, nu_amount))                       
                        donation_list.append(new_listz)                 
                        outfile.close()
                        complete = True
                        break
              
def create_report():
    # print ("create Report")
    name_header  = " Donor Name "
    total_given = " |  Total  Given   |"
    num_gifts    = " Num Gifts      | "
    average_gift = " Average  Gift  " 
    print ("{:15}  {:15}  {:15}  {:15}"
           .format(name_header, total_given, num_gifts, average_gift))
    print (" ------------------------------------------------------------------------")
    # soft list in ascending order base on field "amount"
    newlist = sorted(donation_list, key=itemgetter('Amount'), reverse=True)
        
    # using list comprehension to print list of items
    chkout = [print("{:<19} {:14.2f}{:^15d}{:=21.2f}".format(value['full name'],value['Amount'],
                  int(value['num_gift']), value['avg_amt'])) for value in newlist]

    print ("\n\n\n")


def send_letters():
    print ("send letters")
    chk_inputz = [value for  value in donation_list]
    #chkit = [print(value['full name'], value['Amount']) for value in chk_inputz] 
  
   # prints message format in list comprehensions
    output_msg = [print(msg.format(value['full name'], value['Amount']))
                 for value in chk_inputz]

    for line in chk_inputz:
        with open(line['full name'] + ".txt", "w") as outfile:
                outfile.writelines(msg.format(line['full name'], line['Amount']))
   
    outfile.close()
   
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
         try:
             response = int(response)
              
         except ValueError:
             print ("Invalid input ", response )
         except KeyError as i: 
             print ("Keyerror ")
             print (i)
         else:    
               
             try:
                 switch[response]()          
            
             except IndexError:
                 print ("Index Error ", response)
             except ValueError as e:
                 print ("ValueError ")
                 print (e)
             except KeyError as o:  
                 print ("Invalid selection ")
                 print (o)
             except KeyboardInterrupt:
                 print ("Wrong key enter ")

             

# Main function
if __name__ == "__main__": 
   
   main() 

