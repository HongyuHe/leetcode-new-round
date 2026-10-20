class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Attempts:
            * 35min
        Notes:
            * mincap = max(weights), maxcap = sum(weights)
            * Binary search on [mincap, maxcap]
                * M = maxcap - mincap
                * N = len(weights)
                * O(logM * N)
        """
        def cap_fits(cap: int) -> bool:
            duration = 1
            total = 0
            for weight in weights:
                if total + weight <= cap:
                     total += weight
                else:
                    duration += 1
                    total = weight
                    if duration > days:
                        return False
            return True

        mincap = max(weights)
        maxcap = sum(weights)

        lo = mincap
        hi = maxcap
        #! The capacity is not necessarily a multiple of the min weight
        # step = min(weights)
        cap = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            #* Try weight being mid
            if cap_fits(mid):
                cap = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return cap
        