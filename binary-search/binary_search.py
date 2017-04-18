class BinarySearch(list):
	def __init__(self, length, step):
		list.__init__(self, [i for i in range(step, (length*step) + 1, step)])
		self.length = len(self)

	def search(self, value):
		pass

if __name__ == '__main__':
	print(BinarySearch(20, 2))
