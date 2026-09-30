# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Attempts: 
            1. 45min, tail < head bug ...
        Plan:
            * Have two pointers: head and tail
            * Keep inserting the tail after head
            * Move head by 2 nodes
            1,2,3,4,5
            1,5,2,3,4
            1,5,2,4,3

            1 2 3 4
            1 4 2 3
        """
        node = head
        # nxt = node.next
        registry = []
        while node:
            registry.append(node)
            node = node.next
        tail_ptr = len(registry)-1
        tail = registry[tail_ptr]
        

        # nxt = head.next
        while head.next:
            if tail_ptr <= len(registry) // 2:
                break

            neck = head.next

            head.next = tail
            tail.next = neck
            # Move 2 nodes forward
            head = neck
            
            tail_ptr -= 1
            tail = registry[tail_ptr]
            tail.next = None
        