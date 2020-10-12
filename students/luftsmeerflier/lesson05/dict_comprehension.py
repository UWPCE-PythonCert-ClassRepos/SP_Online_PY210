#!/user/bin/env python3


food_prefs = {
	"name" : "Chris",
	"city" : "Seattle",
	"cake" : "chocolate",
	"fruit" : "mango",
	"salad" : "greek",
	"pasta" : "lasagna"
}


hex_nums = {hex(num): num for num in range(1,15)}

count_a = {entry : entry.count('a') for entry in food_prefs}

divisors = {2: [], 3: [], 4 : []}



# s2 = {num for num in range(1, 20) if num % 2 == 0}

# s3 = {num for num in range(1, 20) if num % 3 == 0}

# s4 = {num for num in range(1, 20) if num % 4 == 0}


def main():
	#print("{name} is from {city}. He likes {cake}, {fruit}, {salad}, and {pasta}.".format(**food_prefs))
	#print(hex_nums)
	#print(count_a)
	#print(s2)
	#print(s3)
	#print(s4)
	divisors = {2: ['s2', ''], 3: ['s3', ''], 4: ['s4', '']}

	for key in divisors:
		divisors[key][1] = [num for num in range(1,20) if num % key == 0]

	print(divisors)




if __name__ == "__main__":
	main()