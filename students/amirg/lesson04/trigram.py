'''This file generates a new story using trigrams'''
import random
import string

'''Reads in the the short story data file'''
def read_in_data(file):
	with open(file, 'r') as f:
		story = f.read()
	f.close()
	'''makes the story text lower case'''
	story = story.lower()
	'''replaces tabs and indents'''
	whitespace = dict.fromkeys('\r\n\t', ' ')
	'''replaces the indentation'''
	punctuation = dict.fromkeys(string.punctuation, ' ')
	story = story.translate(story.maketrans(whitespace))
	story = story.translate(story.maketrans(punctuation))
	story = story.split()
	return story

'''Builds the trigrams'''
def build_trigrams(words_list):
	trigrams = {}
	for i in range(len(words_list)-2):
		'''starts pair at beginning of list'''
		pair = words_list[i:i + 2]
		pair = tuple(pair)
		follower = words_list[i + 2]
		follower = list(follower.split())
		'''pair is in trigrams'''
		if pair in trigrams:
			trigrams[pair].extend(follower)
		else:
			trigrams.update({pair: follower})
	return trigrams

'''builds the new story text'''
def build_text(words_dict, words_list):
	'''generates a random integer'''
	rand_int = random.randint(0, len(words_list)-3)
	text = words_list[rand_int:rand_int + 2]
	choice = tuple(text)
	'''generates a random choice from list'''
	random_text = random.choice(words_dict.get(choice))
	'''story length is 400 words'''
	while len(text) < 250:
		while choice == (words_list[-2], words_list[-1]):
			'''removes last element from text'''
			text.pop()
			choice = (text[-2], text[-1])
			print(text)
			'''as long as new list if 1 word long'''
			while len(words_dict.get(choice)) == 1:
				if len(text) == 2:
					text.pop()
					rand_int = random.randint(0, len(words)-3)
					text.extend(words[rand_int:rand_int + 2])
					choice = tuple(text)
					break
				else:
					text.pop()
					choice = (text[-2], text[-1])
		random_text = random.choice(words_dict.get(choice))
		text.append(random_text)
		choice = (choice[-1],random_text)
		print(text)
	return " ".join(text)

'''main interactions'''
if __name__ == '__main__':
	list_of_words = read_in_data('sherlock_small.txt')
	grams = build_trigrams(list_of_words)
	final = build_text(grams, list_of_words)
	print(final)