
def safe_input():
    try:
        entry = input("Enter something: ")
        print(entry)
        return True
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

if __name__ == '__main__':
    if not safe_input():
        print()
        print('Keyboard interrupt and EOF')
