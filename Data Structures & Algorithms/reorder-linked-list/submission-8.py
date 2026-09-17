# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: split and reverse second half
        second = slow.next
        slow.next = None

        previous = None
        current = second
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first = head
        second = previous

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        