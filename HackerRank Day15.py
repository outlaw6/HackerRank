    def insert(self,head,data): 
    #Complete this method
        if head == None:
            return Node(data)
        head.next = self.insert(head.next, data)
        return head
            
        