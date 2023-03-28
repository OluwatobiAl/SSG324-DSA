
def remove_greater_nodes(self, head):
    if not head:
        return None

    sentinel = ListNode(0)
    sentinel.next = head

    prev, curr = sentinel, head
    while curr:
        remove = False
        runner = curr.next
        while runner:
            if runner.val > curr.val:
                remove = True
                break
            runner = runner.next

        if remove:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return sentinel.next