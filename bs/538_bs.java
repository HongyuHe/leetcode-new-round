/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


// takeaway: reversed in-order traversal

class Solution {
    public TreeNode convertBST(TreeNode root) {
        if (root == null) return root;
        
        nodeNewValue(root, null);
        
        return root;
    }
    
    static int nodeNewValue(TreeNode node, TreeNode biggerAncestor) {
        if (node.right != null)
            node.val += nodeNewValue(node.right, biggerAncestor); // for right child, `biggerAncestor` can be simply paased on. 

        if (biggerAncestor != null && node.right == null) 
            node.val += biggerAncestor.val; // as a leaf of the left subtree, inherit the value from the ancestor greater with greater value

        if (node.left != null) 
            return nodeNewValue(node.left, node); // change `biggerAncestor` to ther current node

        return node.val;
    }
}