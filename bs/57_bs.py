class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        """
        • Binary search based on the start positions for the place to insert
        • From the start position, begin merging/combining until a disjoined interval
        """
        if not intervals:
            return [newInterval]

        '''Binary search the 1st overlapping interval'''
        new_start, new_end = newInterval
        l, r = 0, len(intervals)-1
        start_idx = -1
        while l <= r:
            m = (l+r) // 2
            start, end = intervals[m]
            
            if start <= new_start <= end:
                start_idx = m
                break
            elif new_start < start:
                if m > 0:
                    #* The start is greater than the previous end -> stop at this interval
                    if new_start > intervals[m-1][1]:
                        start_idx = m
                        break
                else: #* m==0:
                    start_idx = 0
                    break
                #* Go left
                r = m - 1
            else: #* new_start > end
                if m == len(intervals) - 1:
                    #* The last interval already
                    start_idx = m
                    break
                #* Go right
                l = m + 1
        
        # print(f"{start_idx=}")

        '''Start merging/inserting'''
        new_intervals = intervals.copy()[:start_idx] #* Shallow copy for iteration only.
        for i in range(start_idx, len(intervals)):
            start, end = intervals[i]
            new_start, new_end = newInterval

            #* Case 1: insert at i
            if new_end < start:
                new_intervals.append(newInterval)
                #* Return directly as the rest won't overlap.
                return new_intervals + intervals[i:]
            #* Case 2: insert after i
            if new_start > end:
                new_intervals.append(intervals[i])
            #* Case 3: overlapping
            if start <= new_start <= end or start <= new_end <= end:
                #* Update newInterval
                newInterval = [
                    min(start, new_start),
                    max(end, new_end)
                ]
        new_intervals.append(newInterval)
        return new_intervals

            
                
