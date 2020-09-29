
# #Task One
mytup = (2, 123.4567, 10000, 12345.67)
print("file_{0:0>3d}: {1:.2f}, {2:.2e}, {3:.2e}".format(*mytup))

# #Task Two
print(f"file_{mytup[0]:0>3d}: {mytup[1]:.2f}, {mytup[2]:.2e}, {mytup[3]:.2e}")
# #Is there a better way to do this with f-strings?

#Task Three
def formatter(in_tuple):
    #tuplelength = len(in_tuple)
    #print(tuplelength)
    form_string = str('{:d},'*len(in_tuple))[:-1]
    #print(form_string)
    return form_string.format(*in_tuple)

#Task Four
thetup = (4,30,2017,2,27)
print("{3:0>2d} {4:0} {2:0} {0:0>2d} {1:0}".format(*thetup))

#Task Five
list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {list[0].upper()[:-1]} is {list[1] * 1.2} '
      f'and the weight of a {list[2].upper()[:-1]} is {list[3] * 1.2}')

#Task Six
people  = [('Erica', 29, 102.05),
('Mark', 42, 10102.0523),
('Shadow', 9, 1102.8675309),
('Carbon', 10, 8675309.05)
]

for person in people:
    print('{:10}{:10}{:20.{decimalplaces}f}'.format(*person, decimalplaces=2))
print()

#Task Six Extra
consecutive_numbers = (1,2,3,4,5,6,7,8,9,10)
print(('{:{width}}'*10).format(*consecutive_numbers, width=5))    

if __name__ == "__main__":
    print(formatter((1,2,3)))    
  