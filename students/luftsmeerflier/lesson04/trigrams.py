#/usr/bin/env python3

import sys
import re
import random


#Turn a wall-of-text into a list

# starting with index 0 as n,  take the n and n+1 index-items of the list as a string "hello world", save as a key # to a trigramsionary with the value being the  n+2 index {"Hello world" : "lorem"}

#Then, increment the n index and repeat (n, n+1, n+2) => {"world lorem", "ipsum"} etc. 

#Use a while loop tha breaks 
def populate_dict_with_keys(arr, current_word, next_word, trigrams):
	if next_word in arr and next_word not in trigrams:
		key = (current_word, next_word)
		trigrams[key] = []
	else:
		return

def trigram_generator(text):
	# Split text into an array
	arr = text.split(' ')
	# Make a trigramsionary to store key-value pairs
	trigrams = {}

	for i in range(len(arr) - 1):
		word = arr[i]
		next_word = arr[i + 1]
		populate_dict_with_keys(arr, word, next_word, trigrams)

	keys_array = [key for key in trigrams.keys()]

	for i in range(len(arr) - 2):
		word = arr[i]
		next_word = arr[i + 1]
		possible_key = (word, next_word)
		subsequent_word = arr[i + 2]
		if possible_key in keys_array:
			trigrams[(possible_key)].append(subsequent_word)


	# trim keys that have no values
	for key in trigrams.copy():
		if len(trigrams[key]) == 0:
			del trigrams[key]

	return trigrams


def generate_random(trigrams, final_string):
	random_list = []
	# trigrams is a dictionary contianing tuple keys and a list of strings as their values
	# turn dictionary into array, then choose random index with randint
	trigram_list = [keys for keys in trigrams.keys() ]


	# Make sure the value of the tuple derived from index is not empty ['']
	def get_index():
		index = random.randint(0, len(trigram_list) - 1)
		# Use that selection to re-enter the dict and select use the value
		key_tuple = trigram_list[index]
		third_word_list = trigrams[key_tuple]
		if third_word_list == ['']:
			return get_index()
		else:
			return index

	for i in range(10):
		index = get_index()
		first_two = trigram_list[index] #tuple
		third = trigrams[first_two][0]
		next_tuple = (first_two[1], third)


		final_string.append(first_two[0])
		final_string.append(first_two[1])
		final_string.append(third)

	return final_string

	



	# random_list.append(key_tuple[0])
	# random_list.append(key_tuple[1])
	# A random key (tuple) turned to a string
	# get third word
	# def get_third_word():
	# 	third_word_list = trigrams[key_tuple]
	# 	# third_word_index = random.randint(0, len(third_word_list)-1)
	# 	third_word_index = 0
	# 	third_word = str(third_word_list[third_word_index])
	# 	if len(third_word) == 0:
	# 		return get_third_word(key_tuple)
	# 	else:
	# 		return third_word

	#third_word = get_third_word(key_tuple)
	#print(third_word)
	# random_list.append(first_two_words)
	# random_list.append(third_word)
	# get next key
	#next_key = (random_list[-1], random_list[-2])

	# print("random list", random_list)
	# print(trigrams)
	# print(next_key)
	# print(random_list)
	# print(trigrams)


	# def gen(key):
	# 	while len(random_list) < 100:






	#print(tuple_)
	# pick a random number (either 0 or 1) to access tuple for starting word


def regex(story):
	# p = re.compile('\*+.*\*+')
	# m = p.match(story)
	# print(m)
	# m = re.search('\*+\sSTART OF THIS PROJECT GUTENBERG EBOOK.+?\*\*\*', story)
	m = re.search('Tom Swift, who had been slowly looking through the pages of a magazine', story)
	delimiter = m.group()

	content = story.split(delimiter,1)[1]
	# remove double quotes
	content = content.replace('"', '')
	content = content.replace(',', '')
	return content[818:1160]

def open_file(text):
	with open(text, 'rt') as file:
		story = file.read().replace('\n', '')
		return story


def main():
	# get the filename from the command line
	try:
		filename = sys.argv[1]
	except IndexError:
		print("You must pass in a filename")
		sys.exit(1)

	story = open_file(filename)
	words = regex(story)
	trigrams = trigram_generator(str(words))

	words_list = generate_random(trigrams, final_string = [])
	print(' '.join(words_list))

if __name__ == "__main__":

	main()

