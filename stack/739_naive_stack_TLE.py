class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use a stack, and pop only if the next element is greater than the top.
        Complexity: O(N^2) worst case: deceasing order
        """
        if len(temperatures) == 1: 
            return 0
        
        results = []
        while temperatures:
            temp = temperatures.pop(0)
            days = 0
            for t in temperatures:
                days += 1
                if t > temp:
                    break
            else:
                #* Didn't trigger a break (no hotter days)
                days = 0
            results.append(days)
        return results