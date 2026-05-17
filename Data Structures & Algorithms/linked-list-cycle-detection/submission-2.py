# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # The slow and fast runner problem, a check to see if the Hare(Fast) laps the Tortise(slow)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True
        return False