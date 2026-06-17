class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This is a DP (dfs) problem:
            * The larger problem (with longer prices) depends on the smaller sub-problems
        """
        if len(prices) == 1:
            return 0
        
        #* [(day, iscooldown, isholding)]
        cache = {}
        def dfs(day, iscooldown, isholding):
            if (day, iscooldown, isholding) in cache:
                return cache[(day, iscooldown, isholding)]
            
            if day == len(prices):
                return 0
            
            maxreturn = float('-inf')
            price = prices[day]
            if not iscooldown:
                if isholding:
                    maxreturn = max(dfs(day+1, True, False)+price, maxreturn)
                else:
                    maxreturn = max(dfs(day+1, False, True)-price, maxreturn)
            #* Doing nothing requires clearing the iscooldown flag.
            maxreturn = max(dfs(day+1, False, isholding), maxreturn)
            cache[(day, iscooldown, isholding)] = maxreturn
            return cache[(day, iscooldown, isholding)]
        
        return dfs(0, False, False)
            