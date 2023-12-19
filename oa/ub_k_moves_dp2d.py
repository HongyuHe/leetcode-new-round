"""
https://leetcode.com/discuss/interview-question/3937797/Uber-Online-Assesment-Question

Problem:
* Move up/down or left/right for any distance
* Complete in K moves

DP solution:
* 2D table [all locations, moves(1, k)]
  - Table size m*n*k
* Base case: k-1 moves in the same row/col

n=3, m=2, k=2, start=[0,0], dest=[1,1]

  moves:  1   2
(0,0)     0   1+1 // (0,0) -> (0,1) (1,0) But not (2,1)
(0,1)     1
(1,0)     1
(1,1)     0
(2,0)     0
(2,1)     1
"""
from typing import *


def k_moves(n: int, m: int, k: int, start: List[int], dest: List[int]):
  rows = m * n
  cols = k + 1 #* The 0th col is unused.
  dp = [[0]*cols for _ in range(rows)]
  #TODO: Smarter indexing.
  coords = [(i, j) for i in range(n) for j in range(m)]
  
  #* Base case
  for pos in range(rows):
    row, col = coords[pos]
    moves = 1
    if row == dest[0]-1 or col == dest[1]-1:
      dp[pos][moves] = 1
    if row == dest[0]-1 and col == dest[1]-1:
      #* Only touch the destination when move==0
      dp[pos][moves] = 0
  
  #TODO: Don't need to iterate the last column (with k moves) -> Only need to compute for the start position.
  #* O( (m*n)^2 * k )
  for moves in range(2, k+1):
    for pos in range(rows):
      paths = 0
      row, col = coords[pos] 
      prev_moves = moves - 1
      for prev_pos in range(rows):
        prev_row, prev_col = coords[prev_pos] 
        if row == prev_row or col == prev_col:
          #* Can't stay in the same position
          if not (row == prev_row and col == prev_col):
            paths += dp[prev_pos][prev_moves]
      dp[pos][moves] = paths
  
  #TODO: Smarter ways of indexing the positions
  result = 0
  for pos in range(rows):
    row, col = coords[pos]
    if row == start[0]-1 and col == start[1]-1:
      result = dp[pos][k]
      break
  print(f"{result=}")
  return result
      

if __name__ == '__main__':
  k_moves(3, 2, 2, [1,1], [2,2])
  k_moves(3, 4, 3, [1,2], [2,3])