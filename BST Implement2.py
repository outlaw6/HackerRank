class Node:

	def __init__(self, val):
		self.value = val
		self.rightChild = None
		self.leftChild = None

	def insert(self, data):

		if self.value == data: # duplikat
			return False

		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		elif self.value < data:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)

		else:
			print("Aldready in")


class Tree:

	def __init__(self):
		self.root = None

	def insert(self, data):

		if self.root == None:

			self.root = Node(data)

		else:

			self.root.insert(data)
			return True

	def prinTree(self, node):

		if node != None:
			self.prinTree(node.leftChild)
			print(str(node.value))
			self.prinTree(node.rightChild)


if __name__ == '__main__':

	drvo = Tree()
	a = Node(1)
	drvo.insert(a)

	for x in range(100):
		#a = Node(x)
		drvo.insert(x)
	drvo.prinTree(a)