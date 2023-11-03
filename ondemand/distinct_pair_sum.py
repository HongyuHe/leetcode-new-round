"""
[Forests OA]
Given a target number and an array of integers (potentially having duplicates), 
return the number of distinct pairs that sum to the target value.

Example 1: target = 12, array=[5,7,9,13,11,6,6,3,3]. 
  Answer: 3. Because there are 3 distinct pairs: (5,7), (3,9), and (6,6).
Example 2: target = 47, array=[1,3,46,1,3,9]. 
  Answer: 1. Because there is only 1 distinct pair: (1,46).
Example 3: target = 12, array=[6,6,3,9,3,5,1]. 
  Answer: 1. Because there are 2 distinct pairs: (3,9) and (6,6).
"""

def count_distinct_pairs(target, nums):
    #* Variants of two sum I and II.
    seen = set()
    distinct_pairs = set()
    
    for num in nums:
        residual = target - num
        
        if residual in seen and (num, residual) not in distinct_pairs and (residual, num) not in distinct_pairs:
            distinct_pairs.add((num, residual))
        
        seen.add(num)
    
    return len(distinct_pairs)

# Test cases:
array1 = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target1 = 12
array2 = [1, 3, 46, 1, 3, 9]
target2 = 47
array3 = [6, 6, 3, 9, 3, 5, 1]
target3 = 12

result1 = count_distinct_pairs(target1, array1)
result2 = count_distinct_pairs(target2, array2)
result3 = count_distinct_pairs(target3, array3)

print(result1)  # Output: 3
print(result2)  # Output: 1
print(result3)  # Output: 1
