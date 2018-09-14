def SelectionSort(q):

	for x in range(len(q) - 1, 0, -1):
		posOfMax = 0
		for y in range(1, x + 1):
			if q[y] > q[posOfMax]:
				posOfMax = y
		q[y], q[posOfMax] = q[posOfMax], q[y]
	return q