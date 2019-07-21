
#By Reem Alqaysi
#lesson01

#This Function will cause NameError exception
def lunch_NameError():
 fruit = 1
 Sandwitch = 1

 lunch = fruit + Sandwitch + vegetable
 print('The function is working fine')


#This Function will cause TypeError exception
def lunch_TypeError():
 fruit = 'Apple'
 Sandwitch = 1
 vegetable = 2

 lunch = fruit + Sandwitch + vegetable
 print('The function is working fine')

#This Function will cause SyntaxError exception
def lunch_SyntaxError():
 fruit = 1
 Sandwitch = 1
 vegetable = 2

 lunch = fruit + Sandwitch  vegetable
 print('The function is working fine')

#This Function will cause AttributeError exception

def lunch_AttributeError():
 fruit = 1
 Sandwitch = 1
 vegetable = 2

 lunch = fruit + Sandwitch + vegetable
 print(lunch.portionSize)
 print('The function is working fine')

#lunch_NameError()
#lunch_TypeError()
lunch_SyntaxError()
#lunch_AttributeError()
