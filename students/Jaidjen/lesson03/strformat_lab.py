#Task 1

Strfrm=( 2, 123.4567, 10000, 12345.67)
print('file_''{:0>3d}:''  {:.2f}'' {:.2e}'' {:.2e}'.format(2,123.4567,10000,12345.67))



#Task 2

Strfrm1=2
Strfrm2=123.567
Strfrm3=1000
Strfrm4=12345.67

print(f'file_{2:0>3d}:')
print(f'{123.567:.2f}')
print(f'{1000:.2e}')
print(f'{12345.67:.2e}')

#Task 3
def formatter():
    form_string = "The numbers are: {:d},{:d},{:d}"
    num = (1, 2, 3)
    print(form_string.format(*num))
formatter()


#Task4
element=(4,30,2017,2,27)
elmtstr= "{3:0>2d},{4},{2},{0:>2d},{1}"
print(elmtstr.format(*element))

#Task5
fruit1= "oranges"
fruit2= "lemons"
wt1=1.3
wt2=1.1

print(f'The weight of {fruit1} is {wt1} and the weight of a {fruit2} is {wt2}')
print(f'The weight of {fruit1.upper()} is {wt1*1.2} and the weight of a {fruit2.upper()} is {wt2*1.2}')

#Task6

info=[['NAME','AGE','COST'],
      ['James','20','1000.00'],
      ['Joanna','25','250.00'],
      ['May','38','100000.90'],
      ['Drew','50','25.76']]

for i in range(len(info)):
    if i == 0:
        print("{:<10s}{:10s}{:12s}".format(info[i][0],info[i][1],info[i][2]))
    else:
        print("{:<10s}{:10s}{:12s}".format(info[i][0],info[i][1],info[i][2]))

