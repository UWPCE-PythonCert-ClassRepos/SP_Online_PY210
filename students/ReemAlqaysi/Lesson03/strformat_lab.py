#generate a filename with zero pad-ed number, floating point number with 2 decimal places,
# third value is float display in a scientific notation with 2 decimal places, forth value is float in scientific notation with 3 decimal places
def task_one(astr):
    finalstr = 'file{0:0>2d}, {1:.2f}, {2:.2e}, {3:.2e}'
    return finalstr.format(*astr)

#repeat task one with format()
def task_two(astr):
    return f'file{astr[0]:0>2d}, {astr[1]:.2f}, {astr[2]:.2e}, {astr[3]:.2e}'

#re-write a string with dynamic variables , so I can pass any truple value. 
def task_three(bstr):
    l = len(bstr)
    return (("the {} numbers are : " + " ,".join(["{}"]*l)).format(l,*bstr))

#Given a 5 element tuple:( 4, 30, 2017, 2, 27)use string formating to print:'02 27 2017 04 30'
def task_four(cstr):
    return f'{cstr[3]} , {cstr[4]} , {cstr[2]} , {cstr[0]} , {cstr[1]}'

#Write an f-string that will display: 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
def task_five(dstr):
	return f'The weight of an {dstr[0].upper()} is {(dstr[1]*1.2)} and the weight of a {dstr[2].upper()} is {(dstr[3]*1.2)}'

#display a data colomns
def task_six(estr):
    print("| {:^10} | {:^10} | {:^10} |".format('Name', 'Age', 'Cost'))
    for i in range(len(estr)):
        print(f"| {estr[i][0]:^10} | {estr[i][1]:^10} | {estr[i][2]:^10} |")
    return

#print the tuple in columns that are 5 charaters wide
def task_extra(fstr):
    print(("{:5}"*len(fstr)).format(*fstr))




if __name__ == "__main__":
    astr = (2, 123.4567, 10000, 12345.67)
    bstr = (2, 3, 4, 5, 6, 7, 8)
    cstr = ( 4, 30, 2017, 2, 27)
    dstr = ('oranges', 1.3, 'lemons', 1.1)
    estr = (("Tom", 20, "$2000"), ("Jan", 30, "$200"),("Lina", 25, "$5000"),("Dima", 30, "$5000"))

    assert task_one(astr) == 'file02, 123.46, 1.00e+04, 1.23e+04'
    assert task_two(astr) == 'file02, 123.46, 1.00e+04, 1.23e+04'
    assert task_three(bstr) ==  'the 7 numbers are : 2 ,3 ,4 ,5 ,6 ,7 ,8'
    assert task_four(cstr) ==  '2 , 27 , 2017 , 4 , 30'
    assert task_five(dstr) == 'The weight of an ORANGES is 1.56 and the weight of a LEMONS is 1.32'

    print("tests passed")

