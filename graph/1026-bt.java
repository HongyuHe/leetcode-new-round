/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
/*
 * idea: along the same direction all the way to the end because in this way,
 * the difference value will always increase;
 * 
 * Taky away: WRONG!!! it's not a BST but just a BT there is no value
 * relationship between nodes but only structure; A BT has no order!!!
 * 
 * 1h 30m
 **/

class Solution {
    static class MinMax {
        int min;
        int max;
        int maxDiff;

        MinMax(TreeNode node) {
            this.min = node.val;
            this.max = node.val;
            this.maxDiff = 0;
        }

        MinMax(int min, int max, int diff) {
            this.min = min;
            this.max = max;
            maxDiff = diff;
        }
    }

    public int maxAncestorDiff(TreeNode root) {
        if (root == null)
            return 0;

        return findMinMax(root).maxDiff;

    }

    static MinMax findMinMax(TreeNode parent) {
        if (parent == null)
            return null;

        MinMax minMaxR = findMinMax(parent.right);
        MinMax minMaxL = findMinMax(parent.left);
        if (minMaxR == null)
            minMaxR = new MinMax(parent);
        if (minMaxL == null)
            minMaxL = new MinMax(parent);

        int childMaxDiff = Math.max(minMaxR.maxDiff, minMaxL.maxDiff);
        MinMax minMax = new MinMax(Math.min(minMaxR.min, minMaxL.min), Math.max(minMaxR.max, minMaxL.max),
                childMaxDiff);

        int maxDiff = Math.max(childMaxDiff,
                Math.max(Math.abs(parent.val - minMax.min), Math.abs(parent.val - minMax.max)));

        // System.out.println( "SubTree at: " + parent.val + " Min:" +
        // Math.min(minMax.min, parent.val)+ " Max: " +
        // Math.max(minMax.max, parent.val)+ " Diff: " +
        // maxDiff);
        return new MinMax(Math.min(minMax.min, parent.val), Math.max(minMax.max, parent.val), maxDiff);
    }
}
