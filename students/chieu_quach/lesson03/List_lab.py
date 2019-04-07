#  Author      - Chieu Quach
#  Assignment  - Lesson 3
#  Exercise    - List Lab


                  
def series1(): 
   # Use tools like apppend and insert to add user input
   # item to fruit table
   
   # Declare Global array list fruit 
   global fruit
   global len_fruit
   print (fruit)
   # Append fruit to the list
   response = input("Enter a fruit to be added ")
   fruit.append(response)
   len_fruit = len(fruit)
   print (fruit, end = " ")

   
   # Enter input value
   # Use enumerate function to print 1 on first index
   fruitz = fruit
   print ("\n")
   numsel = int(input("Please select a number for fruit "))
   for n, fruitz in enumerate(fruitz,1):
      if numsel == n:
            print(numsel, fruitz)

   #add fruit fruit using "+" and show the list
   print ("\n")
   fruit =  ["Strawberry"] + fruit
   #lenfruit  = len(fruit)
   print ("Add Strawberry fruit using +  ")
   print (fruit, end = " ")

   # Ask user to enter another fruit
   print ("\n")
   uinput = input("Add another fruit ")
   fruit.insert(0,uinput)
   len_fruit = len(fruit)
   print (fruit, end = " ")

   # shows list of fruit that begins with "P"
   print ("\n")
   print ("Fruits that begin with P ", end = " ")
   i = 0
   while i < len_fruit:
       typefruit = fruit[i]
       typefruit = typefruit[:1]             
       if typefruit == "P":           
          print (fruit[i], end = " ")
       i = i + 1
       
def series2():
   # Remove last fruit and user input item from table
   
   print ("\n")
   print (fruit, "\n")
   len_fruit = len(fruit)
   totfruit = len_fruit - 1
   remitem  = fruit[totfruit]
   fruit.remove(remitem)
   len_fruit = len(fruit)

   print("Remove last fruit ---> ", end = " ")
   print (fruit)

   print("\n")
   ufruit = str(input("Please enter a fruit to delete "))
   n = 0
 
   while n < (len_fruit - 1):
        
        if ufruit == fruit[n]:
            fruit.remove(fruit[n])
           
        n = n + 1

   len_fruit = len(fruit)
   print(fruit, end = " ")

      
def series3(): 

   while True:
       print ("\n")
       print ("fruit ", fruit)

       # the "+" sign is used to join multiple sentences
       uinput = input(("you like  ") + fruit[0] + " ")
            
       # when user reponds with a no, the fruit from the list gets removed
       if uinput =="no":
           fruitz = fruit[0]
           fruit.remove(fruitz)
       elif uinput == "yes":
           break
       else: 
           print ("Please select (yes or no) ")
                                 
           len_fruit   = len(fruit) 
       #  print ("lenfruit ", lenfruit)
       if len_fruit == 0: 
          break
            
def series4():

   len_fruit = len(fruit)
   z = 0
   # Print letters in each item reversed
   for i in range(0,len_fruit):
      fruit1 = fruit[i]
      fruit1 = fruit1[::-1]
      z = z + 1
      print (fruit1, end = " ")
    
      # if it is last fruit, remove it
      # print ("\n") uses to print new line
      if z == len_fruit:
         print ("\n")
         print ("Original ", fruit)
         fruit.remove(fruit[i])
         print ("Copy ", fruit)
      

      

# Main function
if __name__ == "__main__":

   global fruit
   fruit = ["Apples", "Pears", "Oranges", "Peaches"]
 
   series1()
   len_fruit = fruit
   series2()
   series3()
   series4()



