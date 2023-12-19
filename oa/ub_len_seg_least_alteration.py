"""
Bob is the governor of the city X. This city consists on N spots which are arranged in a straight line A spot can be either a red spot of a green spot . the color of a spot is give as a string STR

if STR[i] is 'R' the ith spot is a red spot
if STR[i] is 'G' the ith spot is a green spot
Bob wants to turn this city into a green city. It is given that a city is called a green city if there exists at least one consecutive segment of K spots which are all green spots.

Bob can pass a bill at-most once. According to this bill any segment of consecutive spots can all be designated as green spots. However, bob wants to find the length of the shortest segment that can be alterded such that the city becomes a green city.

Constraints
1 <= N <= 10^5
1 <= K <= 10^5
1 <= len (STR)<=10^5

Sample Input Sample Output Explanation
5
5 
RRGRG
select segment 1 to 4. we'll have a greenzone of length 5 ans=4

5
3 
RRGRG
select segment 4 to 4 we'll have a greenzone of length 3 ans=1

5
1
RRGRG
we already have a greenzone of length 1 ans=0


Examples:
12
4
RRGRGRRGRRRR

R RGRG RRGRRRR
RGRG -> RGR
Answer: 3

-> sliding window of length K


Examples:
12
6
RRGRGRRGRRGR

RR GRGRRG RRGR
GRGRRG -> RGRR
Answer: 4
"""


def get_shortest_seg_least_designations(STR, K):
  """ Sliding window
  """
  if K > len(STR):
    #* Impossible case
    return -1
  
  segment = STR[:K]
  least_designations = len([s for s in segment if s=='R'])
  prev_designations = least_designations
  win = 1
  
  #* O(N)
  while win+K <= len(STR) and least_designations > 0:
    new_designations = prev_designations
    if STR[win-1] == 'G':
      new_designations += 1
    # else:
    #   new_designations -= 1
      
    if STR[win+K-1] == 'G':
      new_designations -= 1
    # else:
    #   new_designations += 1
    
    if new_designations < least_designations:
      least_designations = new_designations
      segment = STR[win: win+K]
    
    #* Moving the window.
    win += 1
    prev_designations = new_designations
  
  print(f"{segment=} {least_designations=}")
  
  trim = 0
  if segment[0] == 'G':
    trim += 1
  if len(segment) > 1 and segment[-1] == 'G':
    trim += 1
  result = len(segment) - trim
  print(f"{result=}")
  return result


if __name__ == "__main__":
  get_shortest_seg_least_designations('RRGRG', 5)
  get_shortest_seg_least_designations('RRGRG', 3)
  get_shortest_seg_least_designations('RRGRG', 1)
  get_shortest_seg_least_designations('RRGRGRRGRRRR', 4)
  get_shortest_seg_least_designations('RRGRGRRGRRGR', 6)
  