# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head) # give (any) value of 0
        prev, curr = dummy, head

        while curr and curr.next: # while the current node OR the next node isn't the last node (so that they can be exchanged
            # save pointers b/f changing them
            nxtPair = curr.next.next # shift by 2 b/c it is 2 away before switching
            second = curr.next # the node to be switched with first node

            # reverse the pair
            second.next = curr
            curr.next = nxtPair # set the next node for the first ptr to the first in the next pair
            prev.next = second # the second node gets put in the first position (previous points to 2nd now)

            # update pointers
            prev = curr
            curr = nxtPair

        return dummy.next