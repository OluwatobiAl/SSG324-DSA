def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    
    return dummy.next



