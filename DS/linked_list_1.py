class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Reverse the linked list that starts with "head" ListNode
    # NOTE: return prev because head will be None when exiting the while loop
    def reverse(self, head):
        prev=None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def l1select(self, l1, l2):
            # Define the condition that determines from which list
            # we should take a node and add it to the merged list
            return l1.val < l2.val  # Example

    # Merge two linked lists according to a ListNode condition
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        while l1 and l2:             
            if self.l1select(l1, l2):
                cur.next = l1
                l1, cur = l1.next, l1
            else:
                cur.next = l2
                l2, cur = l2.next, l2     
        if l1 or l2:
            cur.next = l1 if l1 else l2 
        return dummy.next
        

# TODO(?): Delete node that satisfies a condition
# TODO(?): Add common edge case (head is None or head.next is None => return head)

# Common edge case (add at start of solution where applicable)
if not head or not head.next:
    return head