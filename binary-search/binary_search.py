class BinarySearch(list):
	def __init__(self, length, step):
		list.__init__(self, [i for i in range(step, (length*step) + 1, step)])
		self.length = length
		self.step = step

	def search(self, value):
		first = 0
		last = self.length - 1
		count = 0

		if value > self[last] or value < self[first] or value % self.step != 0:
			return {'count': count, 'index': -1}
		elif value == self[first]:
			return {'count': count, 'index': first}
		elif value == self[last]:
			return {'count': count, 'index': last}


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
