"""https://leetcode.com/discuss/interview-question/3922862/Uber-OA

* At each position, we have 3 choices: 
  (1) assign the number to the previous group, (2) start a new group, or (3) drop this number.
* Having some negtives at the begining can push up the index k for later positives -> bigger beauty value

Backtracking (brute force): 
  Traversing the decision tree and return the final sum
"""
from copy import deepcopy

def compute_beauty_sum(n, k, arr):
  if n < k:
    #* Impossible to choose k nonempty disjoint subarrays.
    return -1
  
  def compute_beauty(groups):
    beauty = 0
    for i, group in enumerate(groups):
      beauty += (i+1) * sum(group)
    
    # print(f"{beauty=} {groups=}")
    return beauty
      
  def dfs(idx, groups):
    if idx == n:
      if len(groups) == k:
        return compute_beauty(groups)
      else:
        return float('-inf')
    
    """Choice 1: Assign to the previous group"""
    groups[-1].append(arr[idx])
    pregroup_beauty = dfs(idx+1, deepcopy(groups))
    #* Backtrack
    groups[-1] = groups[-1][:-1]
    
    """Choice 2: Start a new group"""
    if len(groups) < k and groups[-1]:
      #* Hasn't reached the limiton #groups AND the previous group is non-empty
      groups.append([arr[idx]])
      postgroup_beauty = dfs(idx+1, deepcopy(groups))
      #* Backtrack
      groups = groups[:-1]
    else:
      #* Exceeded the max. # of groups.
      postgroup_beauty = float('-inf')
    
    """Choice 3: Drop this value"""
    dropgroup_beauty = dfs(idx+1, deepcopy(groups))
    
    return max(pregroup_beauty, postgroup_beauty, dropgroup_beauty)
  
  return dfs(0, [[]])


if __name__ == "__main__":
  arr = [1, 3, -1, -2, 1]
  print(compute_beauty_sum(n=5, k=4, arr=arr))
  arr = [-4, -9, 10, 1, -3, 5]
  print(compute_beauty_sum(n=6, k=3, arr=arr))
