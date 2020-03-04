/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// takeaway: compute the common ancestor for 2 tree nodes

class Solution {
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        LinkedHashSet<Integer> pPath = new LinkedHashSet<>();
        LinkedHashMap<Integer, TreeNode> pMap = new LinkedHashMap<>();
        LinkedHashSet<Integer> qPath = new LinkedHashSet<>();
        LinkedHashMap<Integer, TreeNode> qMap = new LinkedHashMap<>();
        
        trackPath(root, p, pPath, pMap);
        trackPath(root, q, qPath, qMap);
        
        pPath.retainAll(qPath);
        int lcaVal = (int)pPath.toArray()[pPath.size()-1];

        return pMap.get(lcaVal);
    }
    
    boolean trackPath(TreeNode currNode, TreeNode target, Set<Integer> path, Map<Integer, TreeNode> map) {
        if (currNode == null) return false;
        
        path.add(currNode.val);
        map.putIfAbsent(currNode.val, currNode);
        if (currNode.val == target.val) {
            return true;
        }
        
        boolean res = trackPath(currNode.left, target, path, map);
        if (res == false) {
            res = trackPath(currNode.right, target, path, map);
        }
        if (res) return res;
        else {
            path.remove(currNode.val);
            map.remove(currNode.val);
            return false;
        }
    }
}














