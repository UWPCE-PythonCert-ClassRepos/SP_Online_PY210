#!/usr/bin/env python

from operator import *

donation_list = [{'full name': 'William Gates III', "Amount": 653684.49,
                     "num_gift": "2", "avg_amt": 326892.24},
                 {'full name': 'Mark Zukerberg', 'Amount': 16396.10,
                     'num_gift': '3', 'avg_amt': 5465.37},
                 {'full name': 'Jeff Bezos', 'Amount': 873.33,
                     'num_gift': '1', 'avg_amt': 873.33},          
                 {'full name': 'Paul Allen', 'Amount': 708.42,
                     'num_gift': '3', 'avg_amt': 236.14 }]



    
 
def select_user(fname):

    chk_input = [value for  value in donation_list if value['full name'] == fname]

    amount   = chk_input[0]['Amount']
    giftnum  = chk_input[0]['num_gift']
    avg_amt  = chk_input[0]['avg_amt']
    # need to put int for giftnum
    fullname = ("Mark Zukerberg", 16396.10, int(giftnum))           
    list_out = (fname, amount, int(giftnum), avg_amt)
    # print ("list_out ", list_out)
    #  print ("{:<19} {:14.2f}{:^15d}{:=21.2f}".format(*list_out))
    return list_out

def updating_list(fullname, update_val):

    
    chk_input = [value for  value in donation_list if value['full name'] == fullname]
    amount   = chk_input[0]['Amount']
    giftnum  = chk_input[0]['num_gift']
    avg_amt  = chk_input[0]['avg_amt']

    oldlist  = {'full name': fullname, 'Amount': amount, 'num_gift': giftnum, 'avg_amt': avg_amt}
    grand_amount = amount + update_val
    totgift      = int(giftnum) + 1
    grand_avg    = grand_amount / totgift
    grand_avg    = float("%3.2f" %grand_avg)
    newlist = {'full name': fullname, 'Amount': grand_amount, 'num_gift': totgift, 'avg_amt': grand_avg}
    newlistz = (fullname, grand_amount, totgift, grand_avg)
    donation_list.remove(oldlist)
    donation_list.append(newlist) 
    return newlistz
 #   print(newlistz)

def send_thankyou(fname, amount):

    fname = str(fname)
    
    msg  = (" Dear {},\n"
      "\t"  "Thank you for your generous donation of {:5.2f}\n "         
      "\t"  "It will be put to very good use.\n\n"
      "\t" "   Sincerely,\n"
      "\t" "    -The Team\n"
      )
    msg = (msg.format(fname, amount))
   # msg = [msg]
    return msg

def users_list():
    
   chk_inputz = [value for  value in donation_list]
   new_chk    = sorted(chk_inputz, key=itemgetter('Amount'), reverse=True)

   chkout = ["{:<19} {:14.2f}{:^15d}{:=21.2f} ".format(value['full name'],value['Amount'],
                int(value['num_gift']), value['avg_amt']) for value in new_chk]
   

   return chkout    
#name = (["Mark Zukerberg", 16396.10, 3, 5465.37],1500)
#updating_list("Mark Zukerberg", 1500)
#send_thankyou("Mark Zukerberg", 3100)        
       
