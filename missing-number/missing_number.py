def find_missing(array1, array2):
	length1 = len(array1)
	length2 = len(array2)
	if  length1 >= length2:
		longer, shorter = array1, array2
	else:
		longer, shorter = array2, array1

	for el in longer:
		if el not in shorter:
			return el
	return 0		
