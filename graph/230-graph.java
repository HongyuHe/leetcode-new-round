/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// inOrderTraversal
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> nSmalls = new LinkedList<>();
        inOrderTraversal(root, nSmalls);
        return nSmalls.get(k-1);
    }
    
    public void inOrderTraversal(TreeNode parent, List<Integer> nSmalls) {
        if (parent.left != null) inOrderTraversal(parent.left, nSmalls);
        
        nSmalls.add(parent.val);
        
        if (parent.right!= null) inOrderTraversal(parent.right, nSmalls);
    }
}