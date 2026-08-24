# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ One attempt: 14min
        Plan:
            * while loop from the start
            * keep the prv_nxt
            * compute gcd, insert
        """
        import math

        prev_nxt = head
        nxt = head.next
        while nxt:
            gcd = math.gcd(prev_nxt.val, nxt.val)
            node = ListNode(val=gcd, next=nxt)
            prev_nxt.next = node

            prev_nxt = nxt
            nxt = nxt.next
        return head