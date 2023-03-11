# This file contains extra functions that are often useful
# to solve linked list problems.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # NOTE: Suppose there are n nodes in the linked list, 
    # then the index of the middle node middleIndex is: 
    # middleIndex = n//2
    # if we use 0-base indexing.

    # Returns the middle node of a linked list,
    # in a single pass.
    def find_middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    # Depending on the problem, you might also have to find
    # the node that comes before the middle of the list.
    # For example, you would need to do so to delete the middle
    # node of a linked list.
    # You can do this using this variant of the above function:
    # def find_premiddle_and_middle(self, head):
    #     prev_slow = slow = fast = head
    #     while fast and fast.next:
    #         prev_slow = slow
    #         slow, fast = slow.next, fast.next.next
    #     return prev_slow, slow


cur = head = ListNode(0)
for i in range(1,4):
    cur.next = ListNode(i)
    cur = cur.next
sol = Solution()
print(sol.find_middle(head).val)