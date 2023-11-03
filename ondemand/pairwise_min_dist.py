"""
[Forests OA]
Given two list for example: `l1 = [1, 3, 6, 8, 9]` and `l2 = [1,2,3,7,9]`, 
find the minimum sum of the pair-wise distances among their elements. 
For `l1` and `l2`, the answer is `abs(1-1) + abs(2-3) + abs(3-6) + abs(7-8) + abs(9-9) = 0 + 1 + 3 + 1 + 0 = 5`
"""
def find_min_pairwise_dist_sum(l1, l2):
    l1.sort()
    l2.sort()
    min_sum = 0

    for i in range(len(l1)):
        min_sum += abs(l1[i] - l2[i])

    return min_sum