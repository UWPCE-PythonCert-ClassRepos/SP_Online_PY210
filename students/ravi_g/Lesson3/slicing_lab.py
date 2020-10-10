# function for first and last items exchanged
def exchange(s):
    return s[-1] + s[1:-1] + s[0]

# with every other item removed
def replace_items(s2):
    # removing every char with even index
    new_s2 = ''
    for i in range(len(s2)):
        if i%2==0:
            continue
        else:
            new_s2 += s2[i]
    return new_s2

# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
def remove4s(s3):
    new_s3 = ''
    if len(s3) < 4:
        return s3 # return string as is if string is of length less than 4
    for i in range(4, len(s3)-4): # looping from index 5 through end of the string minus 4
        if i % 2 == 0:
            continue
        else:
            new_s3 += s3[i]
    return new_s3

# with the elements reversed (just with slicing)
def reverses(s4):
    return s4[::-1]

# with the last third, then first third, then the middle third in the new order
def zigzag(s5):
    l = int(len(s5)/3)
    return s5[-l:] + s5[:l] + s5[l:-l]

if __name__ == '__main__':
    # function for first and last items exchanged
    assert(exchange('Hi Ravi!') == '!i RaviH')
    # function to remove every other item
    assert(replace_items('Hello World!') == 'el ol!')
    # with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
    assert(remove4s('This is awesome') == 'i w')
    # with the elements reversed (just with slicing)
    assert(reverses('Hello World!') == '!dlroW olleH')
    # with the last third, then first third, then the middle third in the new order
    assert(zigzag('abcdefghi') == 'ghiabcdef')
