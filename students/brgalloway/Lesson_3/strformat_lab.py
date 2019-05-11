
# string formatting exercises

def task_one(a, b, c, d):
    return "file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}".format(a, b, c, d)

print(task_one(2, 123.4567, 10000, 12345.67))

def task_two(a, b, c, d):
    return "file_%003d: %.2f, %.2e, %.2e" % (a, b, c, d)

print(task_two(2, 123.4567, 10000, 12345.67))

def task_four(a_list):
    return "{3:0>2d} {4} {2} {0:0>2d} {1}".format(*a_list)

a_list = ( 4, 30, 2017, 2, 27)
print(task_four(a_list))

def task_five(b_list):
    return f"The weight of an {b_list[0].upper():.6} is {b_list[1] * 1.2} and the weight of a {b_list[2].upper():.5} is {b_list[3] * 1.2}"

b_list = ['oranges', 1.3, 'lemons', 1.1]
print(task_five(b_list))

def task_six(c_list):
    for i in c_list:
        print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}")

c_list = [['Honda', '2018', '$2.73'], ['Ford', '2017', '$380,000'], ['Toyota', '2011', '$40,073']]
task_six(c_list)
