#Lesson 3 String Formatting
#Task 1
some_tuple = (2, 123.4567, 10000, 12345.67)

'file_{:0>3d} :, {:.2f}, {:.2e}, {:.2e}'.format(some_tuple[0],some_tuple[1],some_tuple[2],some_tuple[3])

#Task 2
print(f"file_{some_tuple[0]:0>3d} :, {some_tuple[1]:.2f}, {some_tuple[2]:.2e}, {some_tuple[3]:.2e}")

#Task 3
some_tup = (2,3,5,6,7,8)

def formatter(some_tup):
    tup_length = len(some_tup)
    numbers = '{:d}, ' * tup_length
    nums = numbers[:-2]
    string = ('the ' + str(tup_length) + ' numbers are: ' + nums)
    return string.format(*some_tup)

print(formatter(some_tup))

#Task 4
t = (4, 30, 2017, 2, 27)

print(f"{t[3]:0>2d} {t[4]} {t[2]} {t[0]:0>2d} {t[1]}")

#Task 5
i = ['oranges',1.3,'lemons',1.1]

print(f'The weight of an {i[0].rstrip("s")} is {i[1]} and the weight of a {i[2].rstrip("s")} is {i[3]}')

#Task 6
t = ['first',10,'$99.01','second',15,'$5600.10','third',25,'$107']
t1 = t[:3]
t2 = t[3:6]
t3 = t[6:9]

print(('{:<7}{:^7}{:7}').format(t1[0],t1[1],t1[2]))
print(('{:<7}{:^7}{:7}').format(t2[0],t2[1],t2[2]))
print(('{:<7}{:^7}{:7}').format(t3[0],t3[1],t3[2]))

#Extra task
print(('{:^5d}' * 10).format(*tuple(range(1,11))))
