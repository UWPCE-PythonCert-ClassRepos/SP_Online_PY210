#!/usr/bin/env python3

# Dominic Divakaruni
# Lesson03 - String Formatting Exercise

num = ( 2, 123.4567, 10000, 12345.67)

print("\n --== Task 1 ==--")
print("file_" + str(num[0]).zfill(3)+ ":", str(round(num[1],2))+ ",","{:.2E}".format(num[2])+ ",", "{:.2E}".format(num[3]) )


print("\n --== Task 2 ==--")
print("file_{:03}: {:.2f}, {:.2e}, {:.2e}".format(*num))

print("\n --== Task 3 ==--")
def task3(t):
    size = len(t)
    string = ("the {} numbers are: " + (" {}," * int(size-1)) + " {}").format(size, *t, t[size-1])
    return string
t1 = (2,3,5)
t2 = (2,3,5,7,9)
print(task3(t1))
print(task3(t2))

print("\n --== Task 4 ==--")
t4 = ( 4, 30, 2017, 2, 27)
print(f"{t4[3]:02} {t4[4]} {t4[2]} {t4[0]:02} {t4[1]}")

print("\n --== Task 5 ==--")
t5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {t5[0][:-1]} is {t5[1]} and the weight of a {t5[2][:-1]} is {t5[3]}")


print("\n --== Task 6 ==--")
print("\n --Task 6a--")
kids = (('Derek', 7, 30000), ('Keira', 5, 20000), ('Mia', 3, 10000))

row = "{Name:<5s} | {Age:^5d} | ${Cost:>5.2f}".format
print("{:<5} | {:^5} | {:>5}".format('Name', 'Age', 'Cost'))
for i in kids:
    print(row(Name=i[0], Age=i[1], Cost=i[2]))

print("\n --Task 6b--")
task6b = (1,22,44,66,88,99,111,222,333,444)
print(('{:^10}'* len(task6b)).format(*task6b))