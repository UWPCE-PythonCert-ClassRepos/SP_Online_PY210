#strformat_lab.py
import math

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
    
    #Display (2) decimal places
    flo_num = str(inputs[1])
    output = ""
    Need_Decimal = False
    while Need_Decimal == False:
        count = 0
        for i, a in enumerate(flo_num):
            if a == ".":
                count = i
                output = flo_num[:i]
                Need_Decimal = True
    
    #Display Scientific Information 2 decimal places
    place_holder = str(inputs[2])
    sci_num = f"{place_holder[:1]}.{place_holder[1:3]}e+0{len(place_holder)-1}"

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
    


    print(file_num)
    print(output)
    print(sci_num)
    print(mod_flo)
