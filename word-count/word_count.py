def words(sentence):
	word_list = sentence.split()
	unique_word_list = set(word_list)
	occurrences = dict()

	for term in unique_word_list:
		count = word_list.count(term)
		if term.isdigit():
			term = int(term)
		occurrences[term] = count

	return occurrences
