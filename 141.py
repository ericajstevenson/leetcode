# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution 1: use a hash map (set)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:  # while cur is not null (after end of list)
            if cur in seen:
                return True
            else:
                seen.add(cur)
                cur = cur.next
        return False

# solution 2: use two pointers (more time efficient)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,f = head, head # initiate slow and fast pointers at head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False # if we get to the end of the list, there is no cycle


