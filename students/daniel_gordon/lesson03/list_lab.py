#!/user/bin/env python3
#setup list
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
#input practice
fruit.append(input("Add another fruit> "))
print(fruit)
num = int(input("Give me a number between 1 and 5> "))
print(f"{num}: {fruit[num-1]}")
response = input("Add a fruit again> ")
fruit = [response] + fruit
print(fruit)
fruit.insert(0, input("Add yet another fruit> "))
print(fruit)
for snack in fruit:
    if snack.startswith("P"): print(snack)

#save list as is for parts 3 and 4
series1 = fruit[:]
print(fruit)
fruit.pop()
print(fruit)
fruit *= 2
print(f"Mult by two {fruit}")
delete = input("What should I remove?> ")
#keep asking until a valid value is chosen
while delete not in fruit:
    print(f"{delete} not found")
    print(fruit)
    delete = input("What should I remove?> ")
#remove all instances of element
count = fruit.count(delete)
for _ in range(count):
    fruit.remove(delete)
print(fruit)

#use list from series 1
fruit = series1[:]
answer = ["yes", "no"]
#remove all fruit that user does not like
for snack in fruit[:]:
    like = input(f"Do you like {snack}?> ").lower()
    #keep asking until you understand
    while like not in answer:
        print(f"I dont understand {like}")
        like = input(f"Do you like {snack}?> ")
    if like == "no":
        fruit.remove(snack)
print(fruit)

#Series 4
fruit = series1[:]
rev_fruit = []
for snack in fruit:
    rev_fruit.append(snack[::-1])
fruit.pop()
print(fruit)
print(rev_fruit)
