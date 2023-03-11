def detectCycle(head):
    slow = fast = head
    # Increment fast and slow pointers
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    else: return None
    # Increment two slow pointers to find start of cycle
    while head != slow:
        head, slow = head.next, slow.next
    return head