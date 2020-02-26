/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int countNodes(TreeNode root) {
        return recurCounter(root);
    }
    
    private int recurCounter(TreeNode parent) {
        if (parent == null) return 0;

        return recurCounter(parent.left) + recurCounter(parent.right) + 1;
    }
}