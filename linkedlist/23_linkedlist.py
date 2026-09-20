# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """ One attempt: 25min
        Plan:
            * Use a front pointer for each list
            * Use a tail pointer to keep track of the merged list
            * Iteratively add nodes to the merged list by comparing the fronts and append the smallest
        """
        if not lists or (len(lists) == 1 and not lists[0]):
            return None
        
        wavefronts = [node for node in lists if node]
        head, tail = None, None
        while wavefronts:
            smallest = float('inf')
            idx_min = None
            for i, front in enumerate(wavefronts):
                if front.val < smallest:
                    idx_min = i
                    smallest = front.val
            if tail:
                tail.next = wavefronts[idx_min]
            else:
                head = wavefronts[idx_min]
            tail = wavefronts[idx_min]
            
            if wavefronts[idx_min].next:
                wavefronts[idx_min] = wavefronts[idx_min].next
            else:
                wavefronts = wavefronts[: idx_min] + wavefronts[idx_min+1: ]
        return head

