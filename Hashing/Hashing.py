#
#
# Hashing function
# Convert a set of arbitrarily long string (data) into
# a fixed size. That is called hashing
#
# Hashing is a O(1) complexity operation
# meaning that a fixed time length is needed to perform it

slots = [  x  for x in range(11) ]

nums = [113 , 117 ,  100 , 114 , 108 , 116 , 105 , 99]

for x in nums:
	pos = x % len(slots)
	print(x, pos, x%len(slots))
	print("Broj: " + str(x) + " ide na lokaciju: " + str(pos))
	nums[pos] = x
print(nums)

class HashTable:

	def __init__(self):
		tableSize = 11
		self.slots = [None] * tableSize
		self.data = [None] * tableSize


	def put(self, key)