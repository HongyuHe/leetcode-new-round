class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Mono-decreasing stack (DSC from bottom to top where top is the smallest)
        """
        #* <idx, t>
        stack = []
        #* Default to 0 temperature.
        results = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                #* Popping the top
                i, _ = stack.pop()
                results[i] = idx - i
            #* Pushing the current
            stack.append((idx, t))
        return results
        