# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        Attempts:
            1. 25min, fixed modulo bug
        Plan:
            * Keep two pointers for the heads of the two lists
            * Create a new linked list for the result (alt: overwrite + extend the longest)
        """

        answer = ListNode()
        answer_head = answer
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                addition = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                addition = l1.val + carry
                l1 = l1.next
            elif l2:
                addition = l2.val + carry
                l2 = l2.next
            else:
                addition = carry
                carry = 0
            
            carry = addition // 10
            answer.val = addition % 10

            nxt = ListNode()
            answer.next = nxt
            tail = answer
            answer = nxt

        # Cut the tail
        tail.next = None
        return answer_head
