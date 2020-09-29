for i in range(1,101):
    text = ''
    if i % 3 == 0:
        text += 'Fizz'
    if i % 5 == 0:
        text += 'Buzz'
    if text == '':
        print(i)
    else:
        print(text)