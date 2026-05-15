# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     # --- SETUP ---
    # previous: The "target" box behind us. Starts at None because nothing is behind the first box.
        previous = None
    
    # current: The box you are currently standing on. We start at the front (head).
        current = head

    # --- THE LOOP ---
    # As long as you are standing on a real box (and haven't walked off the end into None)...
        while current:
        
        # STEP 1: Look ahead and save the next box
        # You point your finger at the next box so you don't lose the rest of the train 
        # when you break the current connection.
            next_node = current.next

        # STEP 2: Grab the arrow and bend it backward
        # You physically detach the arrow coming out of your current box, 
        # lift it over your head, and point it backward at the 'previous' box.
            current.next = previous

        # STEP 3: Slide the "backwards target" label forward
        # This current box is fixed! So you move the 'previous' sticky note 
        # onto the box you are standing on. It is now the target for the next round.
            previous = current

        # STEP 4: Slide your feet forward
        # You look at where your finger has been pointing (next_node) 
        # and physically step forward onto that next box to repeat the process.
            current = next_node

    # --- THE FINISH LINE ---
    # 'current' has walked off the train and is now None.
    # But the 'previous' label is resting on the very last box we fixed.
    # Because all arrows now point backward, this last box is the brand-new front (head).
        return previous