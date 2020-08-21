#!/usr/bin/env python3

'''

'''

# Task One

input_tuple = ( 2, 123.4567, 10000, 12345.67)
formatted_string = "file_{:0>3} :   {:5.2f}, {:3.2e}, {:3.2e}".format(*input_tuple)

# Task Two

alt_formatted_string = f"""file_{input_tuple[0]:0>3} :   {input_tuple[1]:5.2f}, 
{input_tuple[2]:3.2e}, {input_tuple[3]:3.2e}""".replace('\n', '')
