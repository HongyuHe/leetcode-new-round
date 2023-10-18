class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #* Two-pointer problem
        #* Space: O(1); Time: O(n)
        leftptr = 0
        rightptr = len(numbers) - 1
        total = numbers[leftptr] + numbers[rightptr]

        #* Solutioin is guaranteed to exist.
        while leftptr < rightptr:
            if total < target:
                leftptr += 1
            elif total > target:
                rightptr -= 1
            else:
                #* Found a solution.
                break
            total = numbers[leftptr] + numbers[rightptr]
            
        return [leftptr+1, rightptr+1]
