def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    tail = dummy = ListNode(0)
    if not l1: #if l1 is empty
        return l2
    if not l2:
        return l1
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next
#edit
