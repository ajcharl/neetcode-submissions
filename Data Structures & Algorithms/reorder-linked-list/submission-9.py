# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # use the fast and slow algorithm to find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # cut the linked list in half from where SECOND sits (fast is at    the end)
        second = slow.next # this is at the middle of the list
        slow.next = None # make it point to None

        # now reverse the second half
        previous = None
        current = second
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        #
        first = head # this is the head of the OG linked list
        second = previous # this is the beginning of the second list

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        