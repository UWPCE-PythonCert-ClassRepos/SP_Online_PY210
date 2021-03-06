#strformat_lab.py
def formatter(in_tuple):
    num = len(in_tuple)
    tups = in_tuple
    message = "The %s numbers are: %s" % (num, tups)
    return message

if __name__ == "__main__":
#Task One
    #Given Inputs
    inputs = (2, 123.4567, 10000, 12345.67)

    #Desired Outputs
    """
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    #File Name
    file_num = inputs[0]
    if inputs[0] < 10:
        file_num = f"file_00{inputs[0]}"
    elif inputs[0] >= 10:
        file_num = f"file_0{inputs[0]}"
    elif inputs[0] > 99:
        file_num = f"file_{inputs[0]}"  
    deliv1 = file_num
    
    #Display (2) decimal places
    flo_num = str(inputs[1])
    output = ""
    Need_Decimal = False
    count = 0
    while Need_Decimal == False:        
        for i, a in enumerate(flo_num):
            if a == ".":
                count = i
                Need_Decimal = True
    output = flo_num[(count+1):(count+4)]
    number_sub1 = int(output[-1:])
    number_sub2 = int(output[-2:-1])
    if output.isnumeric():
        if number_sub1 >= 5:
            number_sub2 += 1
    output = str(number_sub2)
    deliv2 = flo_num[:(count+2)]+output
    
    #Display Scientific Information 2 decimal places
    place_holder = str(inputs[2])
    sci_num = f"{place_holder[:1]}.{place_holder[1:3]}e+0{len(place_holder)-1}"
    deliv3 = sci_num

    #Display Flot Num as 2 decimal places
    place_holder = str(inputs[3])
    mod_flo = ""
    while Need_Decimal == True:
        count = 0
        for i, a in enumerate(place_holder):
            if a == ".":
                count = i
                mod_flo = f"{place_holder[:1]}.{place_holder[1:3]}e+0{i-1}"
                output = place_holder[:i+3]
                Need_Decimal = False
    deliv4 = mod_flo
    
    print(f"{deliv1} :\t{deliv2}, {deliv3}, {deliv4}")

#Task Two
    print("{0}:    {1}, {2}, {3}".format(deliv1, deliv2, deliv3, deliv4))

#Task Three
    t3_t = (6,3,1,15, 100, 25, 96, 69)
    print(formatter(t3_t))

#Task Four
    t4_t = ( 4, 30, 2017, 2, 27)
    '''
    Desired Outcome
    '02 27 2017 04 30'
    '''
    outcome = "0{3} {4} {2} 0{0} {1}".format(*t4_t)
    print(outcome)

#Task Five
    t5_input = ['oranges', 1.3, 'lemons', 1.1]
    '''
    Desire Outcome
    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    '''
    print(f"The weight of an {t5_input[0]} is {t5_input[1]} and the weight of a {t5_input[2]}  is {t5_input[3]}")
    print(f"The weight of an {t5_input[0].upper()} is {t5_input[1] * 1.2} and the weight of a {t5_input[2].upper()}  is {t5_input[3] * 1.2}")

#Task Six
    names = ['Ian', 'Jill', 'Spencer', 'Ryan', 'Dan']
    ages = [12, 36, 57, 34, 39]
    cost = [10.00, 1000.00, 0.00, 25.00, 6.00]

    print("{0:>15s}{1:^15s}{2:>12s}".format("Name", "Age", "Cost"))

    for name in range(len(names)):
        print("{0:>15s}".format(names[name]), end=' ')
        print("{0:^15}".format(ages[name]), end=' ')
        print("{0:>10.2f}".format(cost[name]))