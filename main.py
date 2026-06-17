from stats import word_count
from stats import character_count
from stats import chars_dict_to_sorted_list
import sys

def get_book_text(path):
	with open(path) as f:
		return f.read()

def print_report(path, num_words, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char, count in sorted_chars:
		if not char.isalpha():
			continue
		print(f"{char}: {count}")
	print("============= END ===============")

def main():
	if len(sys.argv) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	path = sys.argv[1]
	contents = get_book_text(path)
	num_words = word_count(contents)
	chars_dict = character_count(contents)
	sorted_chars = chars_dict_to_sorted_list(chars_dict)
	print_report(path, num_words, sorted_chars)
	
main()
