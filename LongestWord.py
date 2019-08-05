def longest_word(word1, word2, word3):
	w1len = len(word1)
	w2len = len(word2)
	w3len = len(word3)

	if w1len > w2len and w1len > w3len:
		return word1
	elif w2len > w1len and w2len > w3len:
		return word2
	elif w3len > w1len and w3len > w2len:
		return word3


def main():
	word1 = raw_input("Enter the first word: ")
	word2 = raw_input("Enter the second word: ")
	word3 = raw_input("Enter the third word: ")


	longest = longest_word(word1, word2, word3)
	print(longest)

main()