#second set of warmup exercises

#string_times
def string_times(str, n):
    return str*n

print(string_times('Hi',2))
print(string_times('Hi',3))
print(string_times('Hi',1))
print('-' * 25)

#front_times
def front_times(str, n):
    return str[:3] * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
print('-' * 25)

#string_bits
def string_bits(str):
    return str[::2]

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
print('-'*25)

#string_splosion
def string_splosion(str):
    result = ''
    for i in range(len(str)):
        chars = str[:i]
        result += chars
    return result + str

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print('-' * 25)

#last2
def last2(str):
    count = str.count(str[-2:])
    return count -1

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print('-' * 25)


