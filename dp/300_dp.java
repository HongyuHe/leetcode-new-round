// [10,9,2,5,3,7,101,18, 20, 31] ==> In this case, although 101 > 7 (101>5), 101 should not be taken; 

class Solution {
    public int lengthOfLIS(int[] nums) {
        /* recursion + memoization */
        int[][] memo = new int[nums.length][nums.length];
        for (int[] row : memo)
            Arrays.fill(row, -1);
        // recurLIS(0, 0, nums, memo);
        return recurLIS(-1, 0, nums, memo);
    }

    public static int recurLIS(int prevIndx, int currIndx, int nums[], int[][] memo) {
        if (currIndx == nums.length)
            return 0;
        if (prevIndx >= 0 && memo[prevIndx][currIndx] > 0)
            return memo[prevIndx][currIndx];

        int takeCurr = 0;
        if (prevIndx < 0 || nums[prevIndx] < nums[currIndx]) { // if always try to take the first one into account;
            takeCurr = 1 + recurLIS(currIndx, currIndx + 1, nums, memo);
        }
        int notTakeCurr = recurLIS(prevIndx, currIndx + 1, nums, memo);

        if (prevIndx >= 0) // cons: cannot remember the first one
            memo[prevIndx][currIndx] = Math.max(takeCurr, notTakeCurr);
        else
            return Math.max(takeCurr, notTakeCurr);

        return memo[prevIndx][currIndx];
    }

}