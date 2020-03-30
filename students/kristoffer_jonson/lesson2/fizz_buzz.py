
for i in range(1,100):
    s = ''
    if i % 3 == 0:
        s = 'Fizz'
    if i % 5 == 0:
        s += 'Buzz'
    if s == '':
        print(i)
    else:
        print(s)