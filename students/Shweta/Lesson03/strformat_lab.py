#!/usr/bin/env python3
#string formating code , each function is given name for each task except for formatter as asked in question


input_tpl=( 2, 123.4567, 10000, 12345.67)

#Task 1

def task1():
    t1_string='file_{:03d}: {:05.2f},{:.2e},{:.2e}'.format(2,123.4567,10000,12345.67)
    return(t1_string)
print(task1)

#Task 2
def task2(input_tpl):
    return(f'file_{input_tpl[0]:03d}: {input_tpl[1]:05.2f},{input_tpl[2]:.2e},{input_tpl[3]:.2e}')

print(task2(input_tpl))

#Task 3
seq=(1,2,3,4,5)
def formatter(seq):
    '''print tuple value using format and join'''
    l=len(seq)
    print(f"the {l} number are: "+','.join(["{}"]*(l)).format(*seq))
    
formatter(seq)    

#task 4
tpl1=( 4, 30, 2017, 2, 27)
def task4(tpl1):
    '''print tuple value using f method of string formatting'''
    return(f'{tpl1[3]:02d} {tpl1[4]:02d} {tpl1[2]:04d} {tpl1[0]:02d} {tpl1[1]:02d}')   

    
print(task4(tpl1))

#Task 5

flist=['oranges', 1.3, 'lemons', 1.1]

def task5(flist):
    '''print list value with upper and multiplication'''
    print(f'The weight of an {flist[0]} is {flist[1]} and the weight of {flist[2]} is {flist[3]}')
    print(f'The weight of an {flist[0].upper()} is {flist[1]*1.2} and the weight of {flist[2].upper()} is {flist[3]*1.2}')

task5(flist)

#Task 6

def task6():
    ''''string formatting using length of columens
        {:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')'''
    line1='{:20}{:20}{:>20}'.format('Smith',23,'$9089.08')
    line2='{:20}{:20}{:>20}'.format('Will',28,'$9000089.08')
    line3='{:20}{:20}{:>20}'.format('Trailor',38,'$898989.08')
    line4='{:20}{:20}{:>20}'.format('Clark',38,'$108989.08')
    print(line1)
    print(line2)
    print(line3)
    print(line4)

task6()

#Part two of Task 6
def task6_2():
    '''print tuple of 10 consucutive number with column of 5 length'''
    t10=(0,1,2,3,4,5,6,7,8,9)
    print(','.join(["{:5}"]*10).format(*t10))

task6_2()
