"""
https://leetcode.com/discuss/interview-question/3937797/Uber-Online-Assesment-Question

Problem:
* Move up/down or left/right for any distance
* Complete in K moves

Brute force:
* Recursively try all possible next location, carrying the move counter
* Return a valid if reaches the destination with K moves
"""

from typing import *


def k_moves(n: int, m: int, k: int, start: List[int], dest: List[int]):
  sequences = 0
  
  def move(pos: Tuple, moves: int):
    nonlocal sequences
    if pos == (dest[0]-1, dest[1]-1) and moves != k:
      #* Can only touch the destination at the last move.
      return
    if moves == k-1:
      #* One step left to the destination: In the same row/col -> a valid path
      if pos[0] == dest[0]-1 or pos[1] == dest[1]-1:
        sequences += 1
        return
      else:
        return 
    
    nxt_row = [i for i in range(n) if i != pos[0]]
    nxt_col = [j for j in range(m) if j != pos[1]]
    for row in nxt_row:
      move((row, pos[1]), moves+1)
    for col in nxt_col:
      move((pos[0], col), moves+1)

  move((start[0]-1, start[1]-1), 0)
  print(f"{sequences=}")
  return sequences


if __name__ == '__main__':
  k_moves(3, 2, 2, [1,1], [2,2])
  k_moves(3, 4, 3, [1,2], [2,3])