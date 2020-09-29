
print("------------------ TASK 1 ------------------")

x = (2, 123.4567, 10000, 12345.67)

s = f"{x[0]:03}, {x[1]:.2f}, {x[2]:.2E}, {x[3]:.2E}"
print(s)

print("------------------ TASK 2 ------------------")

print('{:03}'.format(x[0]), '{:.2f}'.format(x[1]), '{:.2E}'.format(x[2]),
      '{:.2E}'.format(x[3]))

print("------------------ TASK 3 ------------------")


def formatter(tup):
    vv = 'The {} numbers are: '.format(len(tup))
    for x, y in enumerate(tup):
        if x == len(tup)-1:
            vv = vv + '{:d}'
        else:
            vv = vv + '{:d}, '
    print(vv.format(*tup))


p = (4, 30, 2017, 2, 27)

formatter(p)
print("------------------ TASK 4 ------------------")


output = '{3:02d} {4} {2} {0:02d} {1}'.format(*p)
print(output)

print("------------------ TASK 5 ------------------")

fruit_list = ['oranges', 1.3, 'lemons', 1.1]

output1 = f"The weight of an {fruit_list[0][:-1]} is {fruit_list[1]} and the weight of a {fruit_list[2][:-1]} is {fruit_list[3]}"
print(output1)

output2 = f"The weight of an {fruit_list[0][:-1].upper()} is {fruit_list[1]*1.2} and the weight of a {fruit_list[2][:-1].upper()} is {fruit_list[3]*1.2}"
print(output2)

print("------------------ TASK 6 ------------------")

print("Name: {:>10}  |Age: {:>3}  |Cost:  ${:>10}".format("Ronny", 5, 1))
print("Name: {:>10}  |Age: {:>3}  |Cost:  ${:>10}".format("Ricky", 55, 42042.00))
print("Name: {:>10}  |Age: {:>3}  |Cost:  ${:>10}".format("Ralphio", 555, 69.69))
