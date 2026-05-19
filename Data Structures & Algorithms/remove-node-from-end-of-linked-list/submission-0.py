# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # --- SETUP ---
        # Create a fake dummy box to handle deleting the first node safely
        dummy = ListNode(0)
        dummy.next = head
    
        # Both trackers start at the dummy box
        left = dummy
        right = dummy

        # --- STEP 1: THE HEAD START ---
        # We push the 'right' tracker forward exactly 'n' steps.
        # Now, the physical gap between left and right is exactly 'n' boxes.
        for i in range(n):
            right = right.next

        # --- STEP 2: THE MARCH ---
        # March both trackers forward at the exact same pace.
        # Stop the moment 'right' lands on the VERY LAST box in the list.
        while right.next:
            left = left.next
            right = right.next

        # --- STEP 3: THE SNIP ---
        # Because of the gap, 'left' is now standing right BEFORE the target box.
        # We stretch left's arrow completely past the target to drop it from the centipede.
        left.next = left.next.next

        # Return the actual real head of our modified list
        return dummy.next                                                                  