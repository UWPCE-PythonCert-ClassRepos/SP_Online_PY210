#-----TASK 1-----
print('Task 1')
test1 = (2,123.4567,10000,12345.67)
output = 'file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}'.format(*test1)
print(output)

#-----TASK 2-----
print('Task 2')
#Alternate method to achieve task 1. This turned out to be a lot more clunky, since I do not know how to use fstring with formatting numbers
filenum = '%03d' %test1[0]
firstval = '%.2f' %test1[1]
secval = '%.2e' %test1[2]
thirdval = '%.2e' %test1[3]
print(f"file_{filenum} :   {firstval}, {secval}, {thirdval}")

#-----TASK 3-----
print('Task 3')
def format_my_tuple(tuple):
    outputstring = 'the 3 numbers are: '
    size = len(tuple)
    i = 0
    while i < size:
        outputstring += '{:d}, '
        i += 1
    printstring = outputstring.format(*tuple)
    #deletes the extra comma and space
    print(printstring[:-2])

test3 = (1,2,3)
format_my_tuple(test3)

#-----TASK 4-----
print('Task 4')
test4 = (4,30,2017,2,27)
print('{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}'.format(*test4))

#-----TASK 5-----
print('Task 5')
datatoprint = ['oranges',1.3,'lemons',1.1]
#The fruit names are printed to exclude the s at the end
print(f"The weight of an {datatoprint[0][:-1]} is {datatoprint[1]} and the weight of a {datatoprint[2][:-1]} is {datatoprint[3]}")

#-----TASK 6-----
print('Task 6')
header = ['Name', 'Age','Cost']
testlst = [['First',54,3455.23],['Second',52,235.23],['Third',42, 54315.65]]
header_format = "{:<10}" + "{:<10}" + "{:<10}"
row_format ="{:<10}" + "{:^10}" + "${:>10.2f}"
i=0
print(header_format.format(*header))
for row in testlst:
    print (row_format.format(*testlst[i]))
    i += 1

#-----TASK 6 EXTRA-----
print('Task 6 Extra')
nums = (1,2,3,4,5,6,7,8,9,10)
print(('{:5}'*10).format(*nums))
