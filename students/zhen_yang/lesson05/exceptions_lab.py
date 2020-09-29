###########################
# Exceptions Lab Exercise #
###########################
# Create a wrapper function that return None
# when the user enters ^C for keyboard interrupt or
# ^D (^Z on windows) for end of file.
def safe_input():
    try:
        file_name = input(" Please Input File name: ")
        print(f'Filename: {file_name}')
        return 1
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

# Calling the safe_input() function
if not safe_input():
    print("\n Keyboard interrupt or EOF. ")
