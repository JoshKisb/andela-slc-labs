class BinarySearch(list):
	def __init__(self, length, step):
		list.__init__(self, [i for i in range(step, (length*step) + 1, step)])
		self.length = len(self)

	def search(self, value):
		first = 0
		last = len(self)-1
		count = 0
		midpoint = (value // 2) 
		if midpoint > len(self):
			midpoint = value // len(self)
		# 	midpoint = (first + last) // 2
		# while midpoint > len(self):
		# 	midpoint = (midpoint // 2)
		midpoint -= 1
		while first <= last:
			if self[midpoint] == value:
				return {'count': count, 'index': midpoint}
			else:
				count += 1
				if value < self[midpoint]:
					last = midpoint-1
				else:
					first = midpoint+1
			midpoint = (first + last)//2
		return {'count': count, 'index': -1}

if __name__ == '__main__':
	small_list = BinarySearch(20, 1)
	print(small_list)
	print("----- search 16 ------")
	print(small_list.search(16))

	medium_list = BinarySearch(20, 2)
	print(medium_list)
	print("----- search 40 ------")
	print(medium_list.search(40))

	large_list = BinarySearch(100, 10)
	print(large_list)
	print("----- search 880 ------")
	print(large_list.search(880))
