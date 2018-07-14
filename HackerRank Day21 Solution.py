class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        #Write your code here
        if root == None:
            return -1
        left = self.getHeight(root.left) + 1
        right = self.getHeight(root.right) + 1

        return max(left, right)
myTree=Solution()
root=None
for i in range(5):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       