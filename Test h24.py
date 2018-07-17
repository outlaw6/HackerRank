class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        q = []
        glava = head
        #print("\n" + str(glava.data),)
        #print(glava.next.data,)
        '''while glava.next:
                                    if not glava.data:
                                        pass
                                    if glava.data == glava.next.data:
                                        print(glava.data)
                                        q.insert(0,glava.next.data)
                                        glava.next = glava.next
                                return 1'''
    
        current = head
        while current.next:
            if current.data == current.next.data:
                current.data = current.next.next
            else:
                current = current.next
        return head        


mylist= Solution()
head=None
data = 0
for i in range(8):
    data += i
    head=mylist.insert(head,data)
head=mylist.insert(head, 28) 
mylist.display(head)   

head=mylist.removeDuplicates(head)
print(head)

mylist.display(head)