/*
    1. bottom-up
    2. dp
*/

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {

        if (triangle.size() == 0) {
            return 0;
        }
        if (triangle.size() == 1) {
            return triangle.get(0).get(0);
        }

        List<ArrayList<Integer>> dp = new ArrayList<ArrayList<Integer>>(triangle.size());
        // base case
        for (int row = 0; row < triangle.size(); row++) {
            if (row == 0) {
                dp.add(new ArrayList<>(triangle.get(row)));
                continue;
            }
            dp.add(new ArrayList<Integer>());
            for (int cell = 0; cell < triangle.get(row).size(); cell++) {
                int lp = cell - 1;
                int rp = cell;
                int lpVal = Integer.MAX_VALUE;
                int rpVal = Integer.MAX_VALUE;
                if (lp >= 0) {
                    lpVal = triangle.get(row).get(cell) + dp.get(row - 1).get(lp);
                }
                if (rp < triangle.get(row - 1).size()) {
                    rpVal = triangle.get(row).get(cell) + dp.get(row - 1).get(rp);
                }
                dp.get(row).add(Math.min(lpVal, rpVal));
            }
        }
        return Collections.min(dp.get(dp.size() - 1));
    }
}