"""
exercise 3.3: string formatting lab
joli umetsu
"""


"""---TASK ONE---"""
print("---task one---")

tuple = (2, 123.4567, 10000, 12345.67)

# print items using string formatting 
print("file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*tuple))


"""---TASK TWO---"""
print("\n---task two---")

# print items using literal string interpolation 
a, b, c, d = tuple
print(f"file_{a:03d} :   {b:.2f}, {c:.2e}, {d:.2e}")


"""---TASK THREE---"""
print("\n---task three---")

""" (i didn't follow directions on my first try)
def formatter(input_tuple):
    n = len(input_tuple)
    # convert input tuple to strings 
    str_tuple = []
    for num in input_tuple:
        str_tuple.append(str(num))
    # use join to define list of numbers seperated with commas 
    number_list = ", ".join([*str_tuple])
    # use f-string to print final output string 
    print(f"the {n} numbers are: {number_list}")  """
    
def formatter(in_tuple):
    n = len(in_tuple)
    d = '{:d}'
    num_list = ", ".join([d for i in in_tuple])
    form_string = "the {} numbers are: {}".format(n,num_list)
    return form_string.format(*in_tuple)
    
    
"""---TASK FOUR---"""
print("\n---task four---")

tuple4 = (4,30,2017,2,27)
v,w,x,y,z = tuple4
print("{:02d} {:d} {:d} {:02d} {:d}".format(y,z,x,v,w))


"""---TASK FIVE---"""
print("\n---task five---")

list = ['oranges', 1.3, 'lemons', 1.1]
f1, w1, f2, w2 = list 
print(f"The weight of an {f1[:-1].title()} is {w1*1.2} and the weight of a {f2[:-1].title()} is {w2*1.2}")


"""---TASK SIX---"""
print("\n---task six---")

name = ('Name', 'Outback', 'Corolla', 'Focus')
age = ('Age', '8','10','15')
cost = ('Cost', '$11000.00', '$9500.99','$990.95')

for i, j, k in zip(name, age, cost):
    print("{:<10}{:^7}{:>10}".format(i,j,k))

print("\n---extra---")
tup = (1,2,3,4,5,6,7,8,9,10)
print((len(tup)*"{:^5}").format(*tup))    
