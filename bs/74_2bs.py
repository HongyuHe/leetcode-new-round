class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      """
      Rows are sorted:
        Binary search for row number -> binary search within a row
      """
      rows = len(matrix)
      cols = len(matrix[0])

      #* Search row number
      low, high = 0, rows-1
      mid = (low+high) // 2
      while low <= high:
        if target == matrix[mid][0]:
          return True

        if target < matrix[mid][0]:
          high = mid - 1
        else: #* target >= matrix[mid][0]:
          low = mid + 1

        mid = (low+high) // 2
        
      row = matrix[mid]

      #* Search within a row
      left, right = 0, cols-1
      mid = (right+left) // 2
      while left <= right:
        if target == row[mid]:
          return True
        
        if target > row[mid]:
          left = mid + 1
        else:
          right = mid - 1
        
        mid = (right+left) // 2
      
      return False