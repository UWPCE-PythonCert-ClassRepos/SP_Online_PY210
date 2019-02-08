def Fizz_Buzz():
    for number in range(1, 101):
        output_string = ""
        if number%3 ==0: output_string = 'Fizz'
        if number%5 ==0: output_string += 'Buzz'
        if output_string == "":
            print(number)
        else:
            print(output_string)
if __name__ == '__main__':
    Fizz_Buzz()