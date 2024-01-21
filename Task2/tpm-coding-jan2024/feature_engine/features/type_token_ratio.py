"""
file: type_token_ratio.py
---
Defines a feature that outputs the word type-token ratio.
"""
from features.word_count import *
import string
"""
function: get_word_TTR
@param text: The message for which we are calculating the word type-token ratio.
Recall that the type-token ratio is equal to (# of unique words) / (# of total words).
The output of this function should be a number (specifically, a float).
Example: “Please, oh please can I go to the ball?” → 8 / 9 → 0.889
"""
def get_word_TTR(text):
	if len(text) == 0:
		return 0
	text = text.lower()
	punc = list(string.punctuation)
	for character in text:
		if character in punc:
			text = text.replace(character, "")
	print(text)
	unique = []
	total_words = text.split()
	for word in total_words:
		if word not in unique:
			unique.append(word)
	return round((len(unique)/len(total_words)), 3)