# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        Plan:
            * Store the pointers in an array
            * Index `n` into the array and remove the node
            * Return list[0]
        """
        ll = []
        node = head
        while node:
            ll.append(node)
            node = node.next
        
        todrop = ll[-n]
        if n == len(ll):
            # Drops the head
            return ll[1] if len(ll) > 1 else None

        prev = ll[-n-1]
        prev.next = todrop.next
        return ll[0]