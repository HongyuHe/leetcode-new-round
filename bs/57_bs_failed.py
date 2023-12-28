class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        • Binary search based on the start positions, where the interval's start <= new start
        • Scan for the end point: 
            1. new_end <= end AND new_end >= start: combining this with the previous (closing with the end OR beginning with the start)
            2. new_end < end AND new_end < start: closing the previous interval with the new_end
            3. New interval is disjoined index
        """
        if not intervals:
            return [newInterval]

        '''Binary search the start'''
        l, r = 0, len(intervals)-1
        new_start, new_end = newInterval
        start_idx = -1
        case_id = 0
        while l <= r:
            m = (l+r) // 2
            start, end = intervals[m]
            
            if new_start >= start and new_start <= end:
                start_idx = m
                break
            elif new_start < start:
                if m > 0:
                    #* The start is greater than the previous end -> disjoined interval
                    if new_start > intervals[m-1][1]:
                        if new_end < start:
                            case_id = 3
                        start_idx = m
                        break
                else: #* m==0:
                    if new_end < start:
                        case_id = 3
                    start_idx = 0

                #* Go left
                r = m-1
            else: #* new_start > end
                #* Go right
                l = m+1
        
        if start_idx < 0:
            case_id = 3
            start_idx = len(intervals)

        '''Scan for the end'''
        end_idx = -1
        if not case_id:
            for i in range(start_idx, len(intervals)):
                start, end = intervals[i]
                if new_end >= start and new_end <= end:
                    case_id = 1
                    end_idx = i
                    break
                elif new_end < start:
                    case_id = 2
                    end_idx = i - 1
                    break
                else: #* new_end > end:
                    continue
            if not case_id: #* The new_end exceeds all intervals.
                if new_start < intervals[start_idx][1]:
                    # New interval spans all intervals.
                    case_id = 1
                else:
                    #* Extend the last interval
                    case_id = 2
                end_idx = i 
        
        # print(f"{case_id=} {start_idx=} {end_idx=}")
        
        '''Inserting the new interval'''
        new_intervals = intervals.copy() #* Shallow
        match(case_id):
            case 1:
                combined_start = intervals[start_idx][0] 
                combined_end = intervals[end_idx][1]
                combined_interval = [
                    combined_start if combined_start <= new_start else new_start,
                    combined_end if combined_end >= new_end else new_end,
                ]
                for i in range(start_idx, end_idx+1):
                    new_intervals.remove(intervals[i])
                new_intervals.insert(start_idx, combined_interval)
            case 2:
                #* Extend the previous (or the last) interval
                new_intervals[end_idx][1] = new_end
                # new_intervals[end_idx][0] = new_start \
                #     if new_start < new_intervals[end_idx][0] else new_intervals[end_idx][0]
            case 3:
                #* Insert disjoined interval directly
                new_intervals.insert(start_idx, newInterval)
            # case 4:
            #     new_intervals = [newInterval]
            case _:
                raise 'Unmatching case'

        return new_intervals
