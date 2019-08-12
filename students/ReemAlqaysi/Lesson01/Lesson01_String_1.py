#String-1
""" this file contains all puzzle functions in codingbat.com String-1"""
#hello_name 
def hello_name(name):
  str = 'Hello '+ name + '!'
  return str

#make_abba 
def make_abba(a, b):
  str = a+b+b+a
  return str

#make_tags 
def make_tags(tag, word):
  str = '<' + tag+'>'+ word +'</'+ tag +'>'
  return str

#make_out_word 
def make_out_word(out, word):
  str = out[0:2] + word +out[2:4]
  return str

#extra_end
def extra_end(str):
  n = len(str)
  newstr = str[n-2:]+str[n-2:]+str[n-2:]
  return newstr

#first_two
def first_two(str):
  x = len(str)
  if x < 2:
    return str
  else:
    newstr = str[:2]
    return newstr

#first_half 
def first_half(str):
  n = len(str) / 2
  newstr = str[:n]
  return newstr

#without_end 
def without_end(str):
  n = len(str)
  newstr = str[1:n-1]
  return newstr

#combo_string 
def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  if len(a) < len(b):
    return a+b+a

#non_start 
def non_start(a, b):
  newstr = a[1:] + b[1:]
  return newstr

# left2 
def left2(str):
  if len(str) >=2:
    newstr = str[2:] + str[0:2]
    return newstr
  else:
    return str


if __name__ == "__main__":
  hello_name('Bob')
  make_abba('Hi', 'Bye')
  make_tags('i', 'Yay')
  make_out_word('<<>>', 'Yay')
  extra_end('Hello')
  first_two('Hello')
  first_half('WooHoo')
  without_end('Hello')
  combo_string('Hello', 'hi')
  non_start('Hello', 'There')
  left2('Hello')
