#!/usr/bin/env python3
"""Done except for the bonus """

def askUser(question):
  response = input(question)
  return response

def addFruit(fruits,newFruit):
  newFruits = list(fruits)
  newFruits.append(newFruit)
  return newFruits
  
def askForNumber():
  response = int(0)
  response = input("Enter a number less than 6 > ")
  return response

def addFruitWithPlus(listOfFruit,fruit):
  listOfFruit = [fruit] + listOfFruit
  return listOfFruit
  
def addFruitWithInsert(listOfFruit,fruit):
  listOfFruit.insert(0, fruit)
  return listOfFruit

def displayFruitsStartingWith(listOfFruit,startingLetter):
  print("Fruits starting with letter ",startingLetter)
  for item in listOfFruit:
    if(item[0] == startingLetter):
      print(item)

def series1(fruitList):
  print('Starting List: ', fruitList)
  newFruit =  askUser("Enter name of fruit to add > ")
  userUpdatedFruit = addFruit(fruitList,newFruit)
  print('Updated List: ', userUpdatedFruit)

  usersNumber = askForNumber()
  thedisplay   = "Fruit number {thenumber} is {thefruit}".format(thenumber = usersNumber, thefruit = userUpdatedFruit[(int(usersNumber)-1)])
  print("Back to user: " ,thedisplay)
  myUpdatedFruit = addFruitWithPlus(userUpdatedFruit,'Lemons')
  withInsertedFruit = addFruitWithInsert(myUpdatedFruit,'Mango')
  displayFruitsStartingWith(withInsertedFruit,'P')
  print('Final List: ', withInsertedFruit)
  return withInsertedFruit

def doSeries2Bonus(doubledList):
  print('doSeries2Bonus Starting List: ', doubledList)
  deleteFruit =  askUser("Enter name of fruit to delete for Bonus > ")
  print('doSeries2Bonus delete fruit: ', deleteFruit)
  if deleteFruit in theList:
    print(deleteFruit, " was found in List")
#    theList.remove(deleteFruit)
  else:
    print(deleteFruit, " was not found in List")

def series2(theList):
  print('Series 2 Starting List: ', theList)
  theList.pop()
  print('After removing the last fruit: ', theList)
  deleteFruit =  askUser("Enter name of fruit to delete > ")
  print('Series 2 delete fruit: ', deleteFruit)
  if deleteFruit in theList :
    print(deleteFruit, " was found in List")
    theList.remove(deleteFruit)
  else:
    print(deleteFruit, " was not found in List")
  return theList

def series3(theList):
#  print('Series 3 Starting List: ', theList)
  for fruit in reversed(theList):
#    print('Ask if they like ', fruit)
    question = "Do you like "+ fruit +" (y or n) > "
    answer =  askUser(question)
    if not (answer=='n') or (answer=='y'):
      valid = False
      while not valid:
        question = "Do you like "+ fruit +" (y or n) > "
        answer =  askUser(question)
        if (answer=='n') or (answer=='y'):
          valid = True
          break
    else:    
      if(answer=='n'):
        print('Delete ', fruit)
        theList.remove(fruit)
      else:
        continue
      
  return theList

def series4(theList):
#  print('Series 4 Starting List: ', theList)
  newList = []
  for fruit in theList:
#    print('fruit: ', fruit [::-1])
    newList.append(fruit [::-1])
  theList.pop()
  print('Original List: ', theList)
  return newList


fruit_tuple = ('Apples', 'Pears', 'Oranges' , 'Peaches')
fruits_list = ['Apples', 'Pears', 'Oranges' , 'Peaches']
fruits_set = {'Apples', 'Pears', 'Oranges' , 'Peaches'}

series1List = series1(fruit_tuple)
print('series1List: ', series1List)

#series2List = series2(series1List)
#print('series2List: ', series2List)
##doSeries2Bonus(series2List*2)

#series3List = series3(series1List)
#print('series3List: ', series3List)

series4List = series4(series1List)
print('series4List: ', series4List)

