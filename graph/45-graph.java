/*
    - DP

*/

class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int pos = 0; pos < nums.length - 1; pos++) {
            for (int jump = 0; jump <= nums[pos]; jump++) {
                if (pos + jump >= nums.length)
                    break;
                if (dp[pos + jump] > dp[pos] + 1)
                    dp[pos + jump] = dp[pos] + 1;
            }
        }
        return dp[nums.length - 1];
    }
}