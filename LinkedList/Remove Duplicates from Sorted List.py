# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        result = set(result)
        result = list(result)
        result.sort()
        if len(result) == 0:
            return first
        temp = ListNode()
        head = temp
        temp.val = result[0]
        for i in range(1,len(result)):
            temp1 = ListNode()
            temp1.val = result[i]
            temp.next = temp1
            temp = temp.next
        return head