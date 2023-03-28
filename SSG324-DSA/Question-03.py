def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    
    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    
    return dummy.next