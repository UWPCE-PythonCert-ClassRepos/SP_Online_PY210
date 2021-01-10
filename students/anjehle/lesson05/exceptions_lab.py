def safe_input():
    try:
        key = input("Hello")
        return key
    except EOFError:
        return
    except KeyboardInterrupt:
        return


print(safe_input())
