class BinarySearch(list):
	def __init__(self, length, step):
		list.__init__(self, [i for i in range(step, (length*step) + 1, step)])
		self.length = len(self)

	def search(self, value, midpo=0):
		first = 0
		last = self.length - 1
		count = 0

		# midpoint = (value // 2) - 1

		while first <= last:
			midpoint = (first + last)//2
			if self[midpoint] == value:
				return {'count': count, 'index': midpoint}
			else:
				count += 1
				if value < self[midpoint]:
					last = midpoint-1
				else:
					first = midpoint+1

		return {'count': count, 'index': -1}
