vals = []
    # iterate through the linked list and add the node values to the list
    while head:
        vals.append(head.val)
        head = head.next
    # check if the list is equal to its reverse
    return vals == vals[::-1]