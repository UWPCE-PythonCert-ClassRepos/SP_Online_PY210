#!/usr/bin/env python3

def print_grid(n):
    hline = '+'+' -'*(n//2)     
    hline = hline+' '*(n%2)
    hline = hline*2+'+'
    vline = '|'+' '*n
    vline = vline+vline+'|'
    for i in range(1,n+3-n%2):
        if i==1 or i==n//2+2:
            print(hline)
        else:
            print(vline)
    print(hline)


def print_grid2(m,n):
    hline = '+'+' -'*n+' '
    hline = hline*m+'+'
    vline = '|'+' '*(2*n+1)
    vline = vline*m+'|'
    for i in range(1,m*n+m+1):
        if i==1 or i%(n+1)==1:
            print(hline)
        else:
            print(vline)
    print(hline)
