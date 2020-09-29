#Task One
a_tuple = (2, 123.4567, 10000,12345.67)
print('file_{:0>3}'.format(a_tuple[0]) + " :    " + '{:.2f}'.format(a_tuple[1])
      + ', {:.2e}'.format(a_tuple[2]) + ', {:.2e}'.format(a_tuple[3]))

#Task Two
print(f"file_{a_tuple[0]:0>3} :    {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}")

#Task Three
def formatter(in_tuple):
    size = len(in_tuple)
    form_string = 'The {}'.format(size) + " numbers are: " + "{:d} " * size
    return form_string.format(*in_tuple)
print(formatter((2,3,5,56,7,8)))

#Task Four
tuple_five = (4, 30, 2017, 2, 27)
print('{:0>2} {:0>2} {:0>2} {:0>2} {:0>2}'.format(tuple_five[3],tuple_five[4],tuple_five[2],tuple_five[0],tuple_five[1]))

#Task Five
a_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an orange is {a_list[1]} and the weight of a lemon is {a_list[3]}")

print(f"The weight of an {a_list[0].upper()} is {a_list[1] * 1.2} and the weight of a {a_list[2].upper()} is {a_list[3] * 1.2}")

#Task Six
print('{:<20}{:>4}{:>20}'.format('Calvin', '34','$99.01'))
print('{:<20}{:>4}{:>20}'.format('Kalvin', '44','$1999.01'))
print('{:<20}{:>4}{:>20}'.format('Kevin', '54','$999.01'))
print('{:<20}{:>4}{:>20}'.format('Malvin', '64','$9912.01'))
print('{:<20}{:>4}{:>20}'.format('Dalvin', '74','$199.01'))
print('{:<20}{:>4}{:>20}'.format('Devin', '84','$9119.01'))
print('{:<20}{:>4}{:>20}'.format('Zacharaery', '104','$29119.01'))