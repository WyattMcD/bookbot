def word_count(text):
	words = text.split()
	return len(words)

def character_count(text):
	characters = {}
	for character in text:
		lower_char = character.lower()
		if lower_char in characters:
			characters[lower_char] += 1
		else:
			characters[lower_char] = 1

	return characters

def sort_on(char: tuple[str, int]) -> int:
	return char[1]

def chars_dict_to_sorted_list(count: dict[str, int]) -> list[tuple[str, int]]:
	result = []
	for char in count:
		char_count = count[char]
		result.append((char, char_count))
		sorted_results = sorted(result, reverse=True, key=sort_on)
	return sorted_results