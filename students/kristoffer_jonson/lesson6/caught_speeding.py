'''
You are driving a little too fast, and a police officer stops you.
Write code to compute the result,
encoded as an int value: 0=no ticket,
1=small ticket, 2=big ticket. If speed is 60 or less,
the result is 0. If speed is between 61 and 80 inclusive,
the result is 1. If speed is 81 or more, the result is 2.
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
'''

def caught_speeding(speed, is_birthday):
    speed_limit = 60
    big_ticket_limit = 80
    if is_birthday:
        speed_limit += 5
        big_ticket_limit += 5
    if speed > speed_limit and speed <= big_ticket_limit:
        return 1
    elif speed > big_ticket_limit:
        return 2
    else:
        return 0