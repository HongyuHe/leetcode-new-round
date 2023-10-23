class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #* Serialize the matrix to a 1d array
        #* Do binary search
        #* Example 1: [1,3,5,7,10,11,16,20,23,30,34,60], target=3, (l=0, r=11)
        #*  mid = 11 // 2 + 0 = 5 -> [mid]: 3 < 11, (l=0, r=4)
        #*  mid = 4 // 2 + 0 = 2 -> [mid]: 3 < 5, (l=0, r=1)
        #*  mid = 1 // 2 + 0 = 0 -> [mid]: 3 > 1, (l=1, r=1) => [l] == target 

        #* Example 2: [1,3,5,7,10,11,16,20,23,30,34,60], target=13, (l=0, r=11)
        #*  mid = 11 // 2 = 5 -> [mid]: 13 > 11, (l=6, r=11)
        #*  mid = 5 // 2 + 6 = 8 -> [mid]: 13 < 23, (l=6, r=7)
        #*  mid = 1 // 2 + 6 = 6 -> [mid]: 13 < 16, (l=6, r=5) => [l] != target 

        #* Example 3: [1,3], target=1, (l=0, r=1)
        #*  mid = 0 -> [mid]: 1 == 1

        #* Example 4: [1,3], target=0, (l=0, r=1)
        #*  mid = 0 -> [mid]: 0 < 1, (l=0, r=0)

        array = []
        for row in matrix:
            array += row
        
        left = 0
        right = len(array) - 1
        mid = (right - left) // 2 + left
        while left < right:
            if target > array[mid]:
                left = mid + 1
            elif target < array[mid]:
                right = mid - 1
            else:
                break
            
            #! `(right - left)` could be negative (Example 2)
            mid = (right - left) // 2 + left

        #! The reason why `mid` can be used here is 
        #! because calculating `mid` is at the end of the loop,
        #! which converges it towards the changing two ptrs.
        return True if array[mid] == target else False