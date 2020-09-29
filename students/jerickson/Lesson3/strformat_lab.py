def task_one():
    print("\nTask One")
    seq = (2, 123.4567, 10000, 12345.67)
    print(f"file_{seq[0]:03.0f} : {seq[1]:0.2f}, {seq[2]:0.2e}, {seq[3]:0.3g}")


def task_two():
    print("\nTask Two")
    seq = (2, 123.4567, 10000, 12345.67)
    print(
        "file_{num:03.0f} : {dec:0.2f}, {sci:0.2e}, {sig:0.3g}".format(
            num=seq[0], dec=seq[1], sci=seq[2], sig=seq[3]
        )
    )


def task_three(*args):
    print("\nTask Three")
    length = len(args)
    repeated = " {:d},"
    full = "The {:d} numbers are:" + repeated * length
    full = full[:-1]
    all_args = (length,) + args
    formatted = full.format(*all_args)
    print(formatted)


def task_four():
    print("\nTask Four")
    #
    seq = (4, 30, 2017, 2, 27)
    print(f"{seq[3]:02d} {seq[4]:d} {seq[2]:d} {seq[0]:02d} {seq[1]:d}")
    print("02 27 2017 04 30")


def task_five():
    print("\nTask Five")
    seq = ["oranges", 1.3, "lemons", 1.1]
    print(
        f"The weight of an {seq[0][:-1]} is {seq[1]:0.1f} and the weight of a {seq[2][:-1]} is {seq[3]:0.1f} "
    )
    print("The weight of an orange is 1.3 and the weight of a lemon is 1.1")


def task_six():
    print("\nTask Six")
    title = ("Name", "Age[days]", "Cost")
    data = [
        ("Spamspam", 3, 4200.42),
        ("Eggs", 1, 302.25),
        ("Ham", 6, 10.45),
        ("FooBar", 2, 1.86),
        ("Bar", 9, 0.01),
    ]
    print(f"{title[0]:^8} {title[1]:^10} {title[2]:^6}")
    for item in data:
        print(f"{item[0]:^8} {item[1]:^10d} ${item[2]:06.2f}")


def task_extra():
    print("\nTask Extra")
    print(("{:5d}" * 10).format(*(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))


if __name__ == "__main__":
    task_one()
    task_two()
    task_three(1, 2, 3, 4, 5, 6)
    task_three(42, 42, 42)
    task_four()
    task_five()
    task_six()
    task_extra()
