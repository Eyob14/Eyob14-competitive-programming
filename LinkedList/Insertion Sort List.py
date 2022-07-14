# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
# Insertion sort in Python
    def insertionSort(self, array):
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1       
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        
        self.insertionSort(result)
        print(result)
        temp = ListNode()
        head = temp
        temp.val = result[0]
        for i in range(1,len(result)):
            temp1 = ListNode()
            temp1.val = result[i]
            temp.next = temp1
            temp = temp.next
        return head
            
        