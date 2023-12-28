"""https://leetcode.com/discuss/interview-question/4246559/uber

• Subsequences aren't consequtive.
• Order matters

Examples:
• [3,2,1] -> 3, 2, 1, 3*2=6, 3*1=3, 2*1=2, 3*2*1=6 -> 3+2+1+6+3+2+6=23
• [3,2,2,1] 
    // Subproblems:
    [1]: [1]
    [2,1]: [1] | [2,1] [2]
    [2,2,1]: [1] [2,1] [2] | ([2,1]) [2,2,1] [2,2] ([2])
    [3,2,2,1]: [1] [2,1] [2] [2,2,1] [2,2] | [3,1] [3,2,1] [3,2] [3,2,2,1] [3,2,2] [3]
    -> 1+2+2+4+4+3+6+6+12+12+3=55

-> Power set algorithm
-> Worst case: O(N^2) where every value is distinct.

"""
from typing import *


MOD = (10**9+7)

def get_distinct_subarr_mults_sum(arr: List[int]):
  power_set = set()
  #* subarr -> mult(subarr)
  mult_cache = {}
  total = 0

  for n in arr[::-1]:
    print(n)
    new_set = set(power_set)
    
    if (n,) not in power_set:
      #* Base case
      new_set.add( (n,) )
      print(f"Adding {(n,)}")
      mult_cache[(n,)] = n
      total += n
    
    for s in power_set:
      subarr = list(s)
      subarr.append(n)
      subarr = tuple(subarr)
      if subarr not in power_set:
        new_set.add(subarr)
        print(f"Adding {subarr}")
        mult = n * mult_cache[s]
        mult_cache[subarr] = mult
        total += mult
    
    #* Update the power set
    power_set = new_set
    total %= MOD
  
  print(f"{total=}, {power_set=}")
  return total % MOD


if __name__ == '__main__':
  get_distinct_subarr_mults_sum([3,2,1]) # 32
  get_distinct_subarr_mults_sum([3,2,2,1]) # 55

