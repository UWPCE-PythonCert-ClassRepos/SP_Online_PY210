
# Author    : Chieu Quach
# Assignment: Lesson03
# Exercise  : String Formating Exercise

# =============================================
# task 1 

def task1():
    
    global file, floatnum, scienum2, scienum3
    
    print ("task 1 ")
    fnames = [2, 123.4567, 10000, 12345.67]
    lenfnames = len(fnames)

    # padded 2 leading 0
    print ("file %03d" %fnames[0])
    file = "%03d" %fnames[0]


    print ("float number %3.2f" %fnames[1])
    floatnum = "%3.2f" %fnames[1]

    # print scientifi notation "e"
    print ("Scientific  %2.3e" %fnames[2])
    scienum2 = "%2.3e" %fnames[2]
    # it prints ---> Scientific  1.000e+04
    print ("Scientifi 3 %.3e" %fnames[3])
    scienum3 = "3 %.3e" %fnames[3]


# =============================================
# task 2
# f-string format
#    ---> use letter f and {} (store variable name inside {})

def task2():

    print ("task 2 (f-string format)")
    print(f"file {file} and float number is {floatnum}.")
    print(f"scientific notation 2 decimal {scienum2}.")
    print(f"scientific notation 3 significant figure {scienum3}.")

    # str.format{}
    # use {} and .format()
    # file = "002"
    # example - print("filename is {} ".format(file))
    print ("task 2 (str.format)")
    print ("file is {} and float number is {} " .format(file,floatnum))
    print("scientific notation 2 decimal {} " .format(scienum2))
    print("scientific notation 3 significant figure {} " .format(scienum3))

def task3():

    print ("task 3 - Build up format strings ")
    in_tuple = (2,3,5)
    bracket = "{:d},"
    merge_bracket = " the {} numbers are : "
    len_in_tuple = len(in_tuple)
    i = 0
    while i < len_in_tuple:
               
        merge_bracket = str(merge_bracket) + bracket
        
        i = i + 1
    # the [:-1] Removed unwanted "," at end of merge_statement
    merge_bracket = merge_bracket[:-1]
    print (merge_bracket.format(len_in_tuple,*in_tuple))

def task4():
    
    # task 4
    # Print 5 elements tuple
    print ("task 4 - 5 element tuple ")     
    in_tuple = (4, 30, 2017, 2, 27)

    # the *in_tuple would not print any comma
    # #example - {3:0>2d} is index position 3 (number 2) with padded 0
    print (" {3:0>2d} {4} {2} {0:0>2d} {1}".format(*in_tuple))



def task5():

    seq = ["orange", 1.3, "lemon", 1.1]

    onehalf = 1.2
    len_seq = len(seq)
    print ("seq ", seq)
    for n in range (0,len_seq):
   
        tot_onehalf = 0
        # check if seq[n] is type float
        if type(seq[n]) == float:
           
            # take argument variable seq[n] * 1.2
             seq[n] = onehalf * float(seq[n])        

    # print items in list in format string
    print (f"the weight of an {seq[0].upper()} is {seq[1]} and the weight of a {seq[2].upper()} is {seq[3]} ")


def task6():

    name = ["steve", "jeff", "tim"]
    age  = [15, 24, 34]
    cost = [100, 1400, 24000]
   
    # {:<7} - moves 7 spaces for character string to the left
    # {:3d} - moves 3 spaces for numeric string to the left
    print("{:<7} {:<3d}  {:3d}".format(name[0], age[0], cost[0]))
    print("{:<7} {:<3d}  {:3d}".format(name[1], age[1], cost[1]))
    print("{:<7} {:<3d}  {:3d}".format(name[2], age[2], cost[2]))  

# Main function
if __name__ == "__main__": 
 
   task1()
   task2()
   task3()
   task4()
   task5()
   task6()
