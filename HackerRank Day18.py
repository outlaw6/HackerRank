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
        return self.items.pop()

    def dequeueCharacter(self):
        return self.items2.pop()
        
    
        
s = 'yes'

for char in s:
    obj.pushCharacter(char)
    obj.enqueueCharacter(char)

obj.isprintaj()
isPalindrome = True

print(obj.popCharacter(), obj.dequeueCharacter())

for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
if isPalindrome:
    print("Yes")
else:
    print("No")