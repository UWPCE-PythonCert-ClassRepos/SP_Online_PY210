for x in range(n,0,1) & n>0:
    range_plus=n+1
    horizontal_list=[+]
    vertical_list=[|]
    count = n

    # this is a test to print ' ' to the list if odd
    if n%2=>0 and n>0:
        count=count-1
        print(' '.join(map(str,horizontal_list)))

    # this is a test to print '-' to the list if even
    elif n%2==0 and n>0:
        count=count-1
        print('-'.join(map(str,horizontal_list)))

    # this is to print '+' when range is done
    elif count=range_plus:
        print('+'.join(map(str,horizontal_list)))
        print('\n'.join(map(str,horizontal_list)))

    # print verticals
for y in range
