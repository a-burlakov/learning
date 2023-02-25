# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
def codewars(word: str) -> str:
	word = word.lower()
	letters = set(word)
	decoding_table = {}
	for letter in letters:
		if word.count(letter) == 1:
			decoding_table[letter] = "("
		else:
			decoding_table[letter] = ")"

	return "".join([decoding_table[x] for x in word])



codewars("Succ ess")