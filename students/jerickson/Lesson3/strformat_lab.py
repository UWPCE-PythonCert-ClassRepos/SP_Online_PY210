def task_one():
    print("Task One")
    seq = (2, 123.4567, 10000, 12345.67)
    print(f"file_{seq[0]:03.0f} : {seq[1]:0.2f}, {seq[2]:0.2e}, {seq[3]:0.3g}")


def task_two():
    print("Task Two")
    seq = (2, 123.4567, 10000, 12345.67)
    print(
        "file_{num:03.0f} : {dec:0.2f}, {sci:0.2e}, {sig:0.3g}".format(
            num=seq[0], dec=seq[1], sci=seq[2], sig=seq[3]
        )
    )


if __name__ == "__main__":
    task_one()
    task_two()
