# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        var = head
        while head != None:
            result.append(head.val)
            head = head.next
        result.pop(-1*n)
        # if the length is 0 we return the original head
        if len(result) == 0:
            return head
        temp = ListNode()
        head = temp
        temp.val = result[0]

        for i in range(1,len(result)):
            temp1 = ListNode()
            temp1.val = result[i]
            temp.next = temp1
            temp = temp.next
        return head