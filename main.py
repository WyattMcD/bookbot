from stats import word_count
from stats import character_count
from stats import chars_dict_to_sorted_list

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	path = "books/frankenstein.txt"
	contents = get_book_text(path)
	num_words = word_count(contents)
	chars_dict = character_count(contents)
	sorted_chars = chars_dict_to_sorted_list(chars_dict)
	print(f"Found {num_words} total words")
	print(sorted_chars)
	
	

main()
