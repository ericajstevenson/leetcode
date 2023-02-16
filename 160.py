# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution 1: use a hash map (set)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set() # set or hash map
        l1,l2 = headA, headB
        while l1:
            seen.add(l1)
            l1 = l1.next
        while l2:
            if l2 in seen:
                return l2
            l2 = l2.next
        return l1 # will return null if there is no intersection

# solution 2: use two pointers to traverse l1 into l2 and vice versa (they will meet at the intersection)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1 # if they are equal, return either one
