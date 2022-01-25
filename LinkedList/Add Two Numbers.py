# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        while l1 is not None:
            s1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 +=str(l2.val)
            l2 = l2.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        result = str(int(s1) + int(s2))
        result = result[::-1]
        
        temp = ListNode()
        temp.val = result[0]
        head = temp
        for i in range(1,len(result)):
            temp1 = ListNode()
            temp1.val = result[i]
            temp.next = temp1
            temp = temp.next
        return head
        