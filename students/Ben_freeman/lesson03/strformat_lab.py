print("Task one\n")

nums=( 2, 123.4567, 10000, 12345.67)
print("file_{:03} :   {:.2f}, {:.2e}, {:.3g}".format(*nums))

print("\nTask Two")

print(f"file_{nums[0]:03} :   {nums[1]:.2f}, {nums[2]:.2e}, {nums[3]:.3g}")

print("\nTask Three")

def formatter(t):
    
    return print("The", str(len(t))," numbers are: ",("{:d} "+",{:d} "*(len(t)-1)).format(*t))

print("\nTask Four")

a= (4,30,2017,2,27)
print(f"{a[3]:02} {a[4]} {a[2]} {a[0]:02} {a[1]}")

print("\nTask Five")

t5list=["oranges",1.3,"lemons",1.1]

print(f"The weight of an {t5list[0]} is {t5list[1]} and the weight of a {t5list[2]} is {t5list[3]}")
print(f"The weight of an {t5list[0].upper()} is {t5list[1]*1.2} and the weight of a {t5list[2].upper()} is {t5list[3]*1.2}")

print("\nTask Six")
zero=["Name","Age","Cost"]
one=["Bill", 1, 10.2]
two=["Billy", 10, 100.3]
three=["Billybil", 100, 1000.14]
print(f"{zero[0]:<10}{zero[1]:<10}{zero[2]:>9}")
print(f"{one[0]:<10}{one[1]:<10}{one[2]:9.2f}")
print(f"{two[0]:<10}{two[1]:<10}{two[2]:9.2f}")
print(f"{three[0]:<10}{three[1]:<10}{three[2]:9.2f}")


print("\nExtra Task")
tuplzseed=int(input("Please input a number: "))
tuplz=(tuplzseed,tuplzseed+1,tuplzseed+2,tuplzseed+3,tuplzseed+4,tuplzseed+5,tuplzseed+6,tuplzseed+7,tuplzseed+8,tuplzseed+9)
print(("{:05}\n"*10).format(*tuplz))
#I realize this wont work with numbers >= 10^5 but im not quite sure how to print numbers larger than that without getting the numbers all garbled up.