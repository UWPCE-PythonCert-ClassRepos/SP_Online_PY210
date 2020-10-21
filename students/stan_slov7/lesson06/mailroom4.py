##!/usr/bin/env python3

#+----------------------------+
#| Mailroom Part 4 - Lesson 6 |
#+----------------------------+

# Refactoring:
#   1.  added getbd - getter function for db verification
#   2. changed add_donation to return the resulting string in addition to printing

import sys, os.path

cur_dir = os.getcwd()
# current directory for file operations

db = {
    "Albert Einstein": [1535.2, 15],
    "Richard Feinman": [150, 17],
    "Lev Landau": [53, 121, 35, 79],
    "Niels Bohr": [135.2, 15],
    "Ilya Prigogine": [15.2, 10]
    }


prompt = "\n".join(("> Welcome to the Mailroom Part 4!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Print Report",                    
          "3 - Send letters to all Donors",
          "4 - Exit",
          ">>> "))


# added getter to verify the db
def getmydir():
    return cur_dir
    

def getdb():
    return db


# input error handling
def safe_input(prompt = ''):
    try:
        result = input(prompt+"\n")
    except (KeyboardInterrupt, EOFError):
        result = None
    return result


def write_file(fname,text):
    try:                            # Catch File Open Exceptions
        file = open(fname,'w')
    except (OSError, IOError):
        print("File Open Error for: ",fname)
    
    try:                            # Catch File Write Exceptions
        file.write(text)
        file.close()
        print("written: ", fname)
    except (OSError, IOError):
        print("File Write Error for: ",fname)


# -> refactor to generate a letter text for send_letters    
def gen_letter(name, amount):
    # div = "===--------------------------------------"
    template = "Dear {name},\n\n\tThank you for your very kind donation of ${amount}.\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t   -The Team."
    letter = template.format(name=name,amount=amount)
    return letter


# -> refactor: added default argument to pass db
def send_letters(dbn = db):
    print("Sending letters to all donors...")
    div = "===--------------------------------------"
    # template = "Dear {name},\n\n\tThank you for your very kind donation of ${amount}.\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t   -The Team."
    #print letters
    for fname, amt in dbn.items():
        print(div)        
        # letter = template.format(name=fname,amount=sum(amt))
        letter = gen_letter(fname,sum(amt))
        print(letter)
        # write to file
        filename = "_".join(fname.split())+".txt"
        write_file(filename,letter)
        
   
# no changes
def send_thankyou():
    new_name = get_name()
    # new_amount = get_amount()
    # print(f"=== Thank You, {new_name}! ===")
    new_amount = get_amount()
    resstr = add_donation(new_name, new_amount)
    print(resstr)


# refactored some code
def add_donation(n_name = "John Doe", n_amount = 0):
    # -> refactored code
    n_name = n_name.title()
    if n_name in db:
        # update_record
       db[n_name].append(n_amount)
    else:
        # add new record
       db[n_name] = [n_amount]
    # -> refactored code
    result = f"=== Thank You, {n_name}, for the ${n_amount:0.2f} donation! ==="
    # print(result)
    return result
    # print(f"=== Thank You, {n_name}, for the ${n_amount:0.2f} donation! ===")
  
    
def get_name():

    np = "> Enter new Donor's Full Name, type 'list' to see all Donors:\n>>> "
    name = safe_input(np) # input errors
    while name.lower() == "list":
        # create_report()
        print_list()
        name=safe_input(np) # input errors
    return(name.title())

def get_amount(): # add error handling on not numbers, and input errors
 
    np = "> Enter a Donation amount:\n>>> "
    try:
        amt = float(safe_input(np))     # input errors
    except (ValueError):
        print("Not valid amount")
        amt = 0 
        
    while amt <= 0 :
        try:
            amt = float(safe_input(np)) # input errors
        except (ValueError):
            print("Not valid amount")
            amt = 0 
        
    return(amt)

    
# refactored to return a string    
def create_report():
    headers = ("Donor Name","Total Given","Num Gifts","Average Gift")
    # hfmt = "{:<25s}\t|{:^15s}\t|{:^10s}\t|{:>15s}"
    hfmt = " {:<25s}|{:>15s}|{:^12s}|{:>15s}" # Header formatting
    valfmt = " {:<25s}|${:>14.2f}|{:^12n}|${:>14.2f}" # value records formatting
    slength = 70
    
    headerstr = hfmt.format(*headers)
    divstr = " "+"-"*slength
    # Printing    
    # print("\n"+divstr)
    # print(headerstr)
    # print(divstr)
    
    header = "\n" + divstr +"\n" + headerstr + "\n" + divstr
    # print(header)
    # -> refactor to build a string instead of printing
  

# changed to comprehension before for part 3       
# Calculate totals and push to new list using comprehension    
    totals = {donor: [sum(donations), len(donations), sum(donations)/len(donations)] for donor, donations in db.items()}
    # totals = {donor: sum(donations) for donor, donations in db.items()}
    # print("Totals comprehension: ") # diagnostic
    # print(totals) # diagnostic
    
    #-> refactor to build and return a string
    tabstr = ''
    for item in totals: # for dict item is key
        # print(valfmt.format(item,totals[item][0],totals[item][1],totals[item][2]))
        # tabstr = valfmt.format(item,totals[item][0],totals[item][1],totals[item][2])
        # print(tabstr)

        tabstr += valfmt.format(item,totals[item][0],totals[item][1],totals[item][2]) + "\n"
    
    tabstr += divstr+"\n"
    tabstr = header + "\n" + tabstr
     
    print(tabstr)    
    return(tabstr)    
        # print(item, totals[item][0])
    # print(divstr+"\n")
    
    
# --> refactored to return a string
def print_list():
    res = ''
    for item in db:
        # print(f"\t{item}: {db[item]}")    # updated for dict
        res += f"\t{item}: {db[item]}" + "\n"
    print(res)
    return(res)


def exit_program():
    print("Good Bye...")
    sys.exit(0);


main_args = {
            1: send_thankyou,
            2: create_report,
            3: send_letters,
            4: exit_program}


def main(): 
    os.chdir(cur_dir) # change to current working directory program is running in
    # print("Main Args: ", main_args)  # diagnostic
    while True:
        try:            # Error handling on range and input errors
            response = int(safe_input(prompt))  # continuously collect user selection
        except(ValueError):
            print("Input error!")            
            response = 0
        # now redirect to feature functions based on the user selection
        # refactor to dict switch
        
        # print("got this: ", response) # diagnostic
        
        if response in main_args:
            main_args.get(response)() # execute option
        else:
            print("Not a valid option!")            
        
 
if __name__ == "__main__":
    main();
