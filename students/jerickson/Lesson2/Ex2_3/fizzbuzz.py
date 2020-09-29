for i in range(1, 101):
    s = ""
    s = s + "fizz" if not i % 3 else s
    s = s + "buzz" if not i % 5 else s
    s = (
        str(i) if not len(s) else s
    )  # If length is zero (not divisible by 3or5), print the number instead
    print(f"{s}")
