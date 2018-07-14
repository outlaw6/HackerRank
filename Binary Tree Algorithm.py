class Node:

	def __init__(self, value=None):
		self.value = value
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree:

	def  __init__(self):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.leftChild == None:
				cur_node.leftChild = Node(value)
			else:
				self._insert(value, cur_node.leftChild)
		elif value > cur_node.value:
			if cur_node.rightChild == None:
				cur_node.rightChild = Node(value)
			else:
				self._insert(value, cur_node.rightChild)
		else:
			print("Value already in tree")

	def printTree(self):
		if self.root != None:
			self._printTree(self.root)

	def _printTree(self, cur_node):
		if cur_node != None:
			self._printTree(cur_node.leftChild)
			print(str(cur_node.value))
			self._printTree(cur_node.rightChild)

	def height(self):
		if self.root != None:
			return self._height(self.root, 0)
		else:
			return 0
	def _height(self, cur_node, curHeight):

		if cur_node == None:
			return curHeight
		leftHeight = self._height(cur_node.leftChild, curHeight + 1)
		rightHeight = self._height(cur_node.rightChild, curHeight + 1)

		return max(leftHeight, rightHeight)


def fillTree(tree, num_elements=100, max_int=1000):
	from random import randint
	for _ in range(num_elements):
		cur_elem = randint(0,max_int)
		tree.insert(cur_elem)
	return tree
tree = BinarySearchTree()
b=[20,50,35,44,9,15,62,11,13]
a=[3,5,2,1,4,6,7]
for x in a:
	tree.insert(x)

print(tree.height())