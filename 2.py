# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # create a dummy node for a new linked list
        cur = dummy # to keep track of the current node
        carry = 0 # to keep track of what carry value to add to the next node
        while l1 or l2 or carry: # while there is still a number in one of the nodes or carry is not null
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10 # get the tens place for the next carry value
            total = total % 10 # get the ones place for the current node
            cur.next = ListNode(total) # create a new node with the ones place
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None # only update if there is a next node
            l2 = l2.next if l2 else None
        return dummy.next # return the new linked list, excluding the dummy node

