#!/usr/bin/env python3

for i in range(1,101):
    
    if i%3 == 0 and not i%5 == 0:
        print("fizz - ",i)

    elif i%5 == 0 and not i%3 == 0:
        print("buzz - ",i)
        
    elif i%3 == 0 and i%5 == 0:
        print("fizzbuzz - ",i)

    else:
        print(i)
    
