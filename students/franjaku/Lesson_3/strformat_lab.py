#!/usr/bin/env python3

#Task 1
t = ( 2, 123.4567, 10000, 12345.67)
string1 = 'file_00{:d} : {:.2f}, {:.2e}, {:.3g}'
print(string1.format(*t))

#Task 2
string2 = 'file_{:0>3} : {:.2f}, {:.2e}, {:.3g}'
print(string2.format(*t))

#Task 3
def formatter(t):


    string3 = 'The {} numbers are: {}'
    return print(string3.format(len(t),str(t)[1:len(str(t))-1]))

if (__name__ == "__main__"):
    formatter((2,3,5))
    formatter((1,2,3,4,5))

#Task 4
string4 = '{3:0>2} {4} {2} {0:0>2} {1}'
print(string4.format(4,30, 2017, 2, 27))

#Task 5
Task5List = ['oranges',1.3,'lemons',1.1]
print(f"The weight of an {Task5List[0]} is {Task5List[1]} and the weight of a {Task5List[2]} is {Task5List[3]}")
print(f"The weight of an {Task5List[0].upper()} is {Task5List[1]*1.2} and the weight of a {Task5List[2].upper()} is {Task5List[3]*1.2}")


#Task 6
names = ['Bob','Mark','Sydney','Marie','Francisco','Sofia'];
ages = [37,62,53,87,20,23];
prices = [400, 567, 23049, 56, 4999, 1500];

print('{:^10} {:^6} {:^10}'.format('Name','Age','Cash'))

for name,age,price in zip(names, ages, prices):
    print(f"{name:<10} {age:^6} ${price:>10.2f}")
