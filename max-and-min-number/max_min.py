def find_max_min(num_list):
	minimun = min(num_list)
	maximum = max(num_list)

	if minimun == maximum:
		return [len(num_list)]

	return [minimun, maximum]
