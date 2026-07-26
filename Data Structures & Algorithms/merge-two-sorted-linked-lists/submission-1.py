# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
                #print("entered 1", tail.next.val, list1.val, list2.val)
            else:
                tail.next = list2
                list2 = list2.next
               # print("entered 2", tail.next.val, list1.val, list2.val)
            tail = tail.next

        if list1:
            tail.next = list1
            #print("entered 3", tail.val)
        elif list2:
            tail.next = list2
           # print("entered 4", tail.val)

        return dummy.next