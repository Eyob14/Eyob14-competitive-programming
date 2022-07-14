# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = []
        while (head != None):
            value.append(head)
            head = head.next
        mid = len(value)//2
        return value[mid]