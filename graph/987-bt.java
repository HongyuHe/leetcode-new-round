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
 * idea: 1. hash the position X and the value is a list of numbers 2. sort every
 * list
 * https://stackoverflow.com/questions/24796273/incompatible-types-list-of-list-and-arraylist-of-arraylist
 * 
 * Takeaway: how to use Comparator 1h
 * 
 */

class Solution {

    static class Vnode {
        int y;
        int val;

        Vnode(int y, int val) {
            this.y = y;
            this.val = val;
        }
    }

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        if (root == null)
            return null;
        Map<Integer, ArrayList<Vnode>> xMap = new TreeMap<>();

        hashNode(0, 0, root, xMap);
        // System.out.println(xMap);

        List<List<Integer>> res = new ArrayList<List<Integer>>();

        for (Map.Entry<Integer, ArrayList<Vnode>> entry : xMap.entrySet()) {
            List<Vnode> nodes = entry.getValue();
            // System.out.println(nodes);
            nodes.sort(new Comparator<Vnode>() {
                public int compare(Vnode node1, Vnode node2) {
                    if (node1.y != node2.y)
                        return node1.y - node2.y;
                    else
                        return node1.val - node2.val;
                }
            });

            res.add(nodes.stream().map(vn -> vn.val).collect(Collectors.toList()));
        }

        // System.out.println(res);

        return res;
    }

    static void hashNode(int x, int y, TreeNode parent, Map<Integer, ArrayList<Vnode>> xMap) {
        if (parent == null)
            return;

        xMap.putIfAbsent(x, new ArrayList<Vnode>());
        xMap.get(x).add(new Vnode(y, parent.val));

        hashNode(x - 1, y + 1, parent.left, xMap);
        hashNode(x + 1, y + 1, parent.right, xMap);
    }
}