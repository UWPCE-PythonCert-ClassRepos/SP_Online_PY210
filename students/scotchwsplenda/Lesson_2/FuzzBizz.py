for i in range(1,101):
    if i%3 ==0:
        print('Fuzz')
    if i%5==0:
        print('Bizz')
    if i%5==0 and i%3==0:
        print('FuzzBizz')
    else:
        print(i)
