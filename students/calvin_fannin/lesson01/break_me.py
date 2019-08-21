def create_name_error():
    print(a)

def create_type_error():
    a=1
    b="huh"
    print(a+b)

def create_syntax_error():
    #print("Hello World"")

def create_attr_error():
    a=3
    print(a.capitalize())



#create_name_error()
#create_type_error()
#create_syntax_error()
create_attr_error()