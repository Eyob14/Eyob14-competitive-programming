# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        if list1 == None:
            head = list1
        elif list2 == None:
            head = list2
        elif list1 == None and list2 == None:
            head = list1
        while list1 != None:
            result.append(list1.val)
            list1 = list1.next
        while list2 != None:
            result.append(list2.val)
            list2 = list2.next
        result.sort()
        print(result)
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