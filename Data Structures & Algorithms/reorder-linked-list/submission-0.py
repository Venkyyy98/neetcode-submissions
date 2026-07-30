# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head

        while first and first.next and first.next.next:
            second = first.next

            # Find the last node and the node before it
            previous = None
            current = first

            while current.next:
                previous = current
                current = current.next

            last = current

            # Remove last node from the end
            previous.next = None

            # Insert last node after first
            first.next = last
            last.next = second

            # Move first forward
            first = second

                