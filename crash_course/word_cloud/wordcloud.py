import sys

import wordcloud

# from wordcloud import WordCloud

# Get input from user (name of text file)
# TODO use command line arguments

excluded_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


def main():
	if len(sys.argv) != 2:
		# sys.exit('Missing command line argument')
		sys.exit("Usage: python wordcloud.py file.txt")

	# print(process_words(get_file(sys.argv[1])))

	# Get all the words from file
	words = process_words(get_file(sys.argv[1]), excluded_words)

	# Get the dictionary for the counts
	# print(sorted(calculate_frequencies(words).items()))
	# for word, frequency in sorted(calculate_frequencies(words).items()):
	# 	print(f"{word}: {frequency}")

	generate_cloud(calculate_frequencies(words))

def get_file(filename):
	"""
	Takes a filename as a parameter and returns an 
	array of the words in the file
	"""
	words = []
	try:
		with open(filename, encoding="utf8") as text:
			for line in text:
				words_in_line = line.split()

				words = [*words, *words_in_line]
				
	except FileNotFoundError:
		sys.exit('File does not exist')

	return words

def process_words(words_list, excluded_words):
	"""
	Take the list of words and make sure each word is
	in all lowercase, and has no punctuation
	"""
	# words = map(lambda word: word.strip(), words_list)
	processed_words = []

	for word in words_list:
		# word = word.lower()
		# for index, character in enumerate(word):
		# 	if not character.isalpha():
		
		# For each word, create a list containing only the alphabetical characters
		# And then join that list into a new word
		# TODO some punctuation like the 's in a word should probably stay and contractions.
		processed_word = "".join([character if character.isalpha() else "" for character in word.lower()])
		
		if processed_word not in excluded_words:
			processed_words.append(processed_word)

	return processed_words

def calculate_frequencies(words):
	"""
	Take a list of words and return a dictionary with words as keys
	and the frequency of that word as its value.
	"""
	frequencies = {}
	for word in words:
		if word in frequencies:
			frequencies[word] += 1
		else:
			frequencies[word] = 1
	
	return frequencies

def generate_cloud(frequencies):
	cloud = wordcloud.WordCloud()
	cloud.generate_from_frequencies(frequencies)
	cloud.to_file("myfile.jpg")


if __name__ == '__main__':
	main()