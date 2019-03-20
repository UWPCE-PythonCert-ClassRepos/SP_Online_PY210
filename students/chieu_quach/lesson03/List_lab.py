#  Author      - Chieu Quach
#  Assignment  - Lesson 3
#  Exercise    - List Lab


def loop_func(lenfruit,typeinput,fruit):
      
      
      i = 0
      #for i in range(0,lenfruit):
      while i < lenfruit:
          
            # check if type typeinput is an integer
            if type(typeinput) == int:
                  if typeinput == i:                       
                        print(typeinput, fruit[i])
                        
            # if type typeinput is "p" then print all fruits that begin with "p"
            elif typeinput   == "P":
                  typefruit = fruit[i]
                  typefruit = typefruit[:1]             
                  if typefruit == "P":
                            
                            print (fruit[i], end = " ")
                            
            else: 
                  print (fruit[i], end = " ")
            i = i + 1   
                  
def series1(fruit): 
      # Use tools like apppend and insert to add user input
      # item to fruit table
      
      # fruit = ["Apples", "Pears", "Oranges", "Peaches"]
      print (fruit)
      # Append fruit to the list
      response = input("Enter a fruit to be added ")
      fruit.append(response)
      lenfruit = len(fruit)
      loop_func(lenfruit,"append",fruit)

      # Enter input value
      print ("\n")
      numsel = int(input("Please enter a number "))
      loop_func(lenfruit,numsel,fruit)

      #add fruit fruit using "+" and show the list
      fruit = fruit + ["Strawberry"]
      lenfruit = len(fruit)
      print ("Add another fruit using +  ")
      loop_func(lenfruit,"add",fruit)

      # Ask user to enter another fruit
      print ("\n")
      uinput = input("Add another fruit ")
      fruit.insert(0,uinput)
      lenfruit = len(fruit)

      loop_func(lenfruit,"add",fruit)

      # shows list of fruit that begins with "P"
      print ("\n")
      print ("Fruits that begin with P ", end = " ")
      loop_func(lenfruit,"P",fruit)


def series2(fruit):
      # Remove last fruit and user input item from table
      print ("\n")
      print (fruit, "\n")
      lenfruit = len(fruit)
      totfruit = lenfruit - 1
      remitem  = fruit[totfruit]
      fruit.remove(remitem)
      lenfruit = len(fruit)

      print("Remove last fruit ---> ", end = " ")
      print (fruit)

      print("\n")
      ufruit = str(input("Please enter a fruit to delete "))
      n = 0
      while n < (lenfruit - 1):
            if ufruit == fruit[n]:
                  fruit.remove(fruit[n])

            n = n + 1

      lenfruit = len(fruit)
      print(fruit, end = " ")

      
def series3(fruit): 

      while True:
            print ("\n")
            print ("fruit ", fruit)

            # the "+" sign is used to join multiple sentences
            uinput = input(("you like  ") + fruit[0])
            
            # when user reponds with a no, the fruit from the list gets removed
            if uinput =="no":
                fruitz = fruit[0]
                fruit.remove(fruitz)
            elif uinput == "yes":
                break
            else: 
                print ("Please select (yes or no) ")
                                 
            lenfruit   = len(fruit)
          #  print ("lenfruit ", lenfruit)
            if lenfruit == 0: 
                break
            
def series4(fruit):

      lenfruit = len(fruit)
      z = 0
      # Print letters in each item reversed
      for i in range(0,lenfruit):
          fruit1 = fruit[i]
          fruit1 = fruit1[::-1]
          z = z + 1
          print (fruit1, end = " ")
    
          # if it is last fruit, remove it
          # print ("\n") uses to print new line
          if z == lenfruit:
              print ("\n")
              print ("Original ", fruit)
              fruit.remove(fruit[i])
              print ("Copy ", fruit)
      

      


if __name__ == "__main__":
      
      fruit = ["Apples", "Pears", "Oranges", "Peaches"]
      series1(fruit)
      series2(fruit)
      series3(fruit)
      fruit = ["Apples", "Pears", "Oranges", "Peaches"]
      series4(fruit)



