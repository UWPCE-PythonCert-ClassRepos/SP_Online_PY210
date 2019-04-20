
# Author      :  Chieu Quach
# Assignment  :  Lesson 4
# Exercise    :  Dictionary and Set Lab

# first variable = key : second variable = value
# Example = "Name" is key : "Chris" is value

def dictionaries():


    dict_name = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}

    print ("Dict_name ", dict_name)
    # Remove 'Cake' from the list
    dict_name.pop('Cake')
    print ("Dict_name ", dict_name)
    # Add an entry for fruit
    dict_name.update({'Fruit': 'Mango'})
    print ("Dict_name ", dict_name)

    for key,value in dict_name.items():
        print ("key ", key)
        print ("value ", value)
    
    print("Cake is in Dictionary", 'Cake' in dict_name)
    # check to see "Mango" value exist in Dictionary
    print ("Mango is in Dictionary", 'Mango' in dict_name.values())

    # Dictionaries 2
    # count number of 't's in each value
    ctr_key   = 0
    ctr_value = 0
    for key, value in dict_name.items():
    
    #print ("value ", value)
        for o in value:
            if o == "t":
               name_value = value
               ctr_value = ctr_value + 1
    
      
    print ("{} has {} number of 't's value ".format(name_value,ctr_value))


def sets():

    # Sets

    set_num = [2,3,4]
    s2 = set()
    s3 = set()
    s4 = set()

    for z in set_num:
        for o in range(0, 20):
           if z == 2:
       
                if o % 2 == 0:
                    s2.add(o)
           elif z == 3:
                if o % 3 == 0:
                    s3.add(o)
           elif z == 4:
                if o % 4 == 0:
                    s4.add(o)

        # print sets s2,s3 and s4 that contain numbers from zero through twenty
        # divisible by 2,3 and 4.
    print ("s2 = ", s2)
    print ("s3 = ", s3)
    print ("s4 = ", s4)

    # is s3 subset of s2
    print ("is s3 subset of s2 ", s3.issubset(s2))
    # is s3 subset of s2
    print ("is s3 subset of s2 ", s4.issubset(s2))

    # Sets 2


    python_set = set(["Python"])
    python_set.add("i")

    # frozen set
    frozen_set = frozenset(["marathon"])

    print ("python_set ", python_set)
    print ("frozen_set ", frozen_set)

    union_set = python_set | frozen_set
    inter_set = python_set & frozen_set

    print ("union_set ", union_set)
    print ("inter_set ", inter_set)


# Main function
if __name__ == "__main__": 
 
   dictionaries()
   sets()
