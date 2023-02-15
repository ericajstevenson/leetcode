# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        L1 = headA
        L2 = headB
        while L1 != L2:
            L1 = L1.next if L1 else return null # if L1 is not null, move to the next node
            L2 = L2.next if L2 else return null
        if L1 == L2:
            return L1