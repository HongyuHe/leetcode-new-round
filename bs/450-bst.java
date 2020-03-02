/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/**
    1. delete a leaf;
    2. delete a internal node;
    
    method: 1) check children 2) keep passing parent
    
    Right solution:
        a. target node has one child: short cut;
        b. two child => replace by its successor: the smallest value in the right subtree;
    
    Qs: a. Is the key always valid? b. any duplication?
*/

class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null; // edge case!!!
        TreeNode[] nodeParentPair = treeSearch(root, root, key);
        TreeNode subroot = null;
        
        if (nodeParentPair == null) {  // no such key
            return root;
        } else {
            subroot = deleteNode(nodeParentPair[0], nodeParentPair[1]);
        }
        
        return (nodeParentPair[1] == subroot)? root : subroot;
    }
    
    public static TreeNode[] treeSearch(TreeNode node, TreeNode parent, int key) {
        if (node.val == key) {
            return new TreeNode[]{node, parent};
        } else if (key > node.val && node.right != null) {
            return treeSearch(node.right, node, key);
        } else if (key < node.val && node.left != null) {
            return treeSearch(node.left, node, key);
        } else {
            return null;
        }
    }
    
    public static TreeNode deleteNode (TreeNode node, TreeNode parent) {
        if (node == parent) { // root
            TreeNode anotherChild = null;
            if (parent.left != null) {
                anotherChild = parent.right;
                parent = parent.left;
            } else {                
                anotherChild = parent.left;
                parent = parent.right;
            }
            if (anotherChild != null) {
                attachNode(anotherChild, parent);
            }
                        
        } else if (node.left != null) {
            if (node == parent.left)
                parent.left = node.left;
            else 
                parent.right = node.left;
            
            if (node.right != null) {
                attachNode(node.right, node.left);
            }
        } else { // left child is null or a leaf
            if (node == parent.left)
                parent.left = node.right;
            else 
                parent.right = node.right;
        }
        
        return parent;
    }
    
    
    static void attachNode(TreeNode child, TreeNode parent) {
        if (child.val <= parent.val) {
            if (parent.left != null)
                attachNode(child, parent.left);
            else
                parent.left = child;
        } else {
            if (parent.right != null)
                attachNode(child, parent.right);
            else
                parent.right = child;
        }
    }
}









