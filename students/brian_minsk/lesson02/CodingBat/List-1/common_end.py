def common_end(a, b):
    if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
        return True
    return False

print(common_end([1, 2, 3], [1, 2, 4]))
print(common_end([1, 2, 3], [5, 4, 3]))
print(common_end([1, 2, 3], [3, 2, 1]))