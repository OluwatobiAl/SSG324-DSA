def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    # Move fast pointer n steps ahead
    for i in range(n):
        fast = fast.next
    
    # Move both pointers until fast pointer reaches the end
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node from the end
    slow.next = slow.next.next
    
    return dummy.next