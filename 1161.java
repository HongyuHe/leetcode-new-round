
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */

import java.util.*;

// Naive BFS
class Solution {
    public int maxLevelSum(TreeNode root) {
        int[] max = new int[] { 0, Integer.MIN_VALUE };
        Deque<Object[]> deque = new ArrayDeque<Object[]>();
        deque.add(new Object[] { 1, root });

        int currLevel = 1;
        int sum = 0;

        while (!deque.isEmpty()) {

            Object[] lnode = deque.remove();
            int nodeLevel = (int) lnode[0];
            TreeNode tnode = (TreeNode) lnode[1];

            if (nodeLevel == currLevel) {
                sum += tnode.val;
            } else {
                if (sum > max[1]) {
                    max[0] = currLevel;
                    max[1] = sum;
                }
                currLevel = nodeLevel;
                sum = tnode.val;
            }
            if (tnode.left != null) {
                deque.add(new Object[] { nodeLevel + 1, tnode.left });
            }
            if (tnode.right != null) {
                deque.add(new Object[] { nodeLevel + 1, tnode.right });
            }
        }
        return max[0];
    }
}

// Exhaust BFS (only keep the frings)
class Solution {
    public int maxLevelSum(TreeNode root) {
        int maxValue = Integer.MIN_VALUE;
        int minLevel = 1;
        int currLevel = 0;

        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);

        while (q.size() > 0) {
            int size = q.size();
            currLevel++;
            int sumLevel = 0;

            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                sumLevel += node.val;
                if (node.left != null) {
                    q.add(node.left);
                }

                if (node.right != null) {
                    q.add(node.right);
                }
            }

            if (maxValue < sumLevel) {
                minLevel = currLevel;
                maxValue = sumLevel;
            }
        }

        return minLevel;
    }
}

// Recursive version
class Solution {
    public int maxLevelSum(TreeNode root) {
        List<Integer> levels = new ArrayList<Integer>();
        traverse(root, levels, 0);
        int max = 0;
        for (int i = 1; i < levels.size(); i++) {
            if (levels.get(i) > levels.get(max)) {
                max = i;
            }
        }
        return max + 1;
    }

    public void traverse(TreeNode r, List<Integer> l, int level) {
        if (r != null) {
            if (l.size() - 1 >= level) {
                int t = l.get(level) + r.val;
                l.set(level, t);
            } else {
                l.add(r.val);
            }
            traverse(r.left, l, level + 1);
            traverse(r.right, l, level + 1);
        }
    }
}