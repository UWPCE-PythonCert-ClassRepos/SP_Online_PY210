#hello_name
def hello_name(name):
    return "Hello " + name + "!"


assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'
print("hello_name tests passed")

