class MyLinkedList:

    def __init__(self,next=None,val=None):
        self.next=next
        self.val=val
        

    def get(self, index: int) -> int:
        cur=self
        for _ in range(index):
            if cur.next:cur=cur.next
        return cur.val if cur.val!=None else -1
        
        
    def addAtHead(self, val: int) -> None:
        self.next,self.val=MyLinkedList(next=self.next,val=self.val),val
        

    def addAtTail(self, val: int) -> None:
        newtail=MyLinkedList(next=MyLinkedList(),val=val)
        cur=self
        if not self.next:
            self.val=val
            self.next=MyLinkedList(next=None,val=None)
            return
        while cur.next.next:
            cur=cur.next
        cur.next=newtail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:self.addAtHead(val);return
        cur=self
        for _ in range(index-1):
            if cur.next:
                cur=cur.next
            else:
                return
        cur.next=MyLinkedList(next=cur.next,val=val)
        
        
    def deleteAtIndex(self, index: int) -> None:
        cur=self
        for _ in range(index):
            if cur.next:
                cur=cur.next
            else:
                return
        if cur.next:
            cur.val=cur.next.val
            cur.next=cur.next.next
            
            
    def __str__(self):
        List=[self.val]
        cur=self
        while cur.next:
            List.append(cur.next.val)
            cur=cur.next
        return str(List)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)