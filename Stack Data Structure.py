class Solution:
    # Write your code here
    def __init__(self):
        self.items = []
        self.items2 = []
    def pushCharacter(self, char):
        self.items.append(char)

    def enqueueCharacter(self, char):
        self.items2.insert(0,char)

    def popCharacter(self):
        self.items.pop()

    def dequeueCharacter(self):
        self.items2.pop(0)

    def isprintaj(self):
    	print(self.items)
    	print(self.items2)

obj = Solution()

obj.pushCharacter(1)
obj.pushCharacter(2)
obj.pushCharacter(3)
obj.enqueueCharacter(1)
obj.enqueueCharacter(2)
obj.enqueueCharacter(3)

obj.isprintaj()

obj.popCharacter()
obj.dequeueCharacter()
obj.isprintaj()


lists = []
def num(x):

	for num in range(1,x+1):
		if x % num == 0:
			lists.append(num)
	print(lists)
	return sum(lists)

print(num(6))