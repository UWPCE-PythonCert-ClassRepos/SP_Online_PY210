# Task 1
########
print("\nTask 1\n")

start = (2, 123.4567, 10000, 12345.67)
print("file_%03d :   %.2f, %.2E, %.3g" % start)

# Task 2
########
print("\nTask 2\n")

print("file_{:0>3d} :   {:.2f}, {:.2E}, {:.3g}".format(*start))

# Task 3
########
def formatter(tup):
    L = len(tup)
    string = "the {:d} numbers are: " + ", ".join(["{}"]*L)
    return string.format(L, *tup)


# Task 4
########
print("\nTask 4\n")

tple = (4, 30, 2017, 2, 27)
print("{:02d} {:02d} {:02d} {:02d} {:02d}".format(tple[3],tple[4],tple[2],tple[0],tple[1]))

# Task 5
########
print("\nTask 5\n")

given = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {given[0][:-1]} is {given[1]} and the weight of a {given[2][:-1]} is {given[3]}")
print(f"The weight of an {given[0][:-1]} is {given[1]*1.2} and the weight of a {given[2][:-1]} is {given[3]*1.2}")

# Task 6
########
print("\nTask 6\n")

table = [['Boeing', 737, 101], ['Airbus', 320, 6], ['Embraer', 175, 23]]
for t in table:
    print("{:>8}{:>4}{:>4}".format(*t))
    
# Task 6 Bonus
##############
print("\nTask 6 Bonus\n")

tup = (1,2,3,4,5,6,7,8,9,10)
print(("{:>5}"*len(tup)).format(*tup))