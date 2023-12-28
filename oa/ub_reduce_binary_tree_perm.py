"""https://leetcode.com/discuss/interview-question/4350883/Uber-OA
"""

from typing import *


class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
  
  def __repr__(self):
    return str(self.data)


def create_binary_tree(tree):
  if not tree:
    return None
  
  def get_node(idx):
    if idx >= len(tree):
      return None
    node = Node(tree[idx])
    node.left = get_node(2*idx + 1)
    node.right = get_node(2*idx + 2)
    return node
    
  return get_node(0)

def generate_permutations(root: 'Node'):
  """Backtracking
      3
    7   9
  12 17 16 15
  """
  perms = []
  
  def swap_children(node: 'Node'):
    node.left, node.right = node.right, node.left
  
  def get_perm(node: 'Node'):
    #* Base case
    if not node.left and not node.right:
      return 
    
    perms.append( traverse_bfs(root) )
    get_perm(node.left)
    get_perm(node.right)    
    
    swap_children(node)
    perms.append( traverse_bfs(root) )
    get_perm(node.left)
    get_perm(node.right)
    #* Backtrack
    swap_children(node)
  
  #TODO: Dedupe
  get_perm(root)
  for perm in perms:
    print(perm)
  return [create_binary_tree(perm) for perm in perms]
    

def reduce_sum_permutations():
  pass

def traverse_bfs(root: 'Node'):
  queue = [root]
  traversal = []
  while queue:
    #* A queue not a stack (pop from the start)
    node = queue.pop(0)
    traversal.append(node.data)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return traversal

def traverse_inorder(root: 'Node'):
  if not root:
    return 
  traversal = []
  
  def inorder(node: 'Node'):
    if node.left:
      inorder(node.left)
    
    traversal.append(node.data)
    
    if node.right:
      inorder(node.right)
    return

  inorder(root)
  return traversal

if __name__ == '__main__':
  tree1 = [3,7,9,12,17,16,15]
  root = create_binary_tree(tree1)
  # print("Inorder:", traverse_inorder(root))
  # print("BFS:\t", traverse_bfs(root))
  print(len(generate_permutations(root)))