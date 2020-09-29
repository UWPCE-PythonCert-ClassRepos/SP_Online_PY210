#/usr/bin/env python3


def series_1():

	fruits = ["Apples", "Pears", "Oranges", "Peaches"]

	print(fruits)

	response = input("Please add another fruit to the list\n")

	fruits.append(response)

	number = int(input("Please type a number (1-4)\n"))

	print(number)
	print(fruits[number-1])

	fruits = ["Strawberry"] + fruits
	print(fruits)

	fruits.insert(0, "Banana")
	print(fruits)

	for fruit in fruits:
		if fruit[0].lower() == 'p':
			print(fruit)

	return fruits


def series_2(fruits):
	print("In series 2")
	input_ = fruits
	def list_gen(fruits):
		print(fruits)
		response = input("Type a fruit to delete\n").title()
		if response not in fruits:
			print("Try one of these:")
			return list_gen(fruits[:] + fruits[:])
		return [fruit for fruit in fruits if fruit != response]

	print(fruits)

	fruits.pop()
	print(fruits)

	print(list_gen(fruits))

def series_3(fruits):
	def get_response():
		response = input("Do you like {}? Y/N\n".format(fruit))
		if not (response.upper() == 'Y' or response.upper() == 'N'):
			print("Input Y or N")
			return get_response()
		elif response.upper() == 'N':
			fruits.remove(fruit)

	for fruit in fruits[:]:
		get_response()

	print(fruits)

def series_4(fruits):
	print("In series 4")
	reversed = [fruit[::-1] for fruit in fruits[:]]
	fruits.pop()
	print(reversed)
	print(fruits)

def main():
	list = series_1()
	#series_2(list)
	#series_3(list)
	series_4(list)

if __name__ == "__main__":
	main()