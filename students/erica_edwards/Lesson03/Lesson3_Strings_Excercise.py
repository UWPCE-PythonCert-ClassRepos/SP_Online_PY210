
# #Task One
# mytup = (2, 123.4567, 10000, 12345.67)
#print("file_{0:0>3d}: {1:.2f}, {2:.2e}, {3:.2e}".format(*mytup))

# #Task Two
# print(f"file_{mytup[0]:0>3d}: {mytup[1]:.2f}, {mytup[2]:.2e}, {mytup[3]:.2e}")
# #Is there a better way to do this with f-strings?

#Task Three
# def formatter(in_tuple):
#     #tuplelength = len(in_tuple)
#     #print(tuplelength)
#     form_string = str('{:d},'*len(in_tuple))[:-1]
#     #print(form_string)
#     return form_string.format(*in_tuple)

#Task Four
# thetup = (4,30,2017,2,27)
# print("{3:0>2d} {4:0} {2:0} {0:0>2d} {1:0}".format(*thetup))

#Task Five
list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {list[0].upper()[:-1]} is {list[1] * 1.2} '
      f'and the weight of a {list[2].upper()[:-1]} is {list[3] * 1.2}')


#if __name__ == "__main__":
    #print(formatter((1,2,3)))    
    