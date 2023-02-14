# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur: # while cur is not null (after end of list)
            while cur.next and cur.next.val == cur.val: # while cur.next is not null and the next value is the same
                cur.next = cur.next.next # skip the next value (deletes node)
            cur = cur.next # move to next node
        return head

