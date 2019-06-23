#Task One

mytuple = (2, 123.4567, 10000, 12345.67)

print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(*mytuple))

#Task Two

print(f"file_{mytuple[0]:0>3d} :   {mytuple[1]:.2f}, {mytuple[2]:.2e}, {mytuple[3]:.2e}")

#Task Three

def formatter(mytuple):
    x = len(mytuple)
    mystring = f"the {x} numbers are: "
    for i in mytuple:
        if i == mytuple[-1]:
            mystring += "{:.0f}"
        else:
            mystring += "{:.0f}, "
    return mystring.format(*mytuple)

print(formatter(mytuple))

#Task Four

fourtuple = (4, 30, 2017, 2, 27)

print(f"{fourtuple[3]:0>2d} {fourtuple[4]:.0f} {fourtuple[2]:.0f} {fourtuple[0]:0>2d} {fourtuple[1]:0>2d}")

#Task Five

fivelist = ["oranges", 1.3, "lemons", 1.1]

print(f"The weight of an {fivelist[0][:-1].upper()} is {fivelist[1]*1.2} and the weight of a {fivelist[2][:-1].upper()} is {fivelist[3]*1.2}")

#Task Six

names = ["Agatha", "Beatrice", "Charlotte"]
ages = ["1", "10", "100"]
costs = ["$1.00", "$10.00", "$100.00"]

print(f"{names[0]:10} {ages[0]:10} {costs[0]:10}")
print(f"{names[1]:10} {ages[1]:10} {costs[1]:10}")
print(f"{names[2]:10} {ages[2]:10} {costs[2]:10}")