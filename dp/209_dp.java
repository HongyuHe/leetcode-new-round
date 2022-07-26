/**
    @logic: dp memoization
            memo[i][j]: the sum of starting at i and ending at j
            memo[i][j] = memo[i][j-1] + nums[j]
            if memo[][] > s
                return j-i+1;
            
            ==> Memory Limit Exceeded!!!
            ==> optimization: memorize only the current row and the optimal val `minLen`
    @time: 30min
*/

class Solution {

    public int minSubArrayLen(int s, int[] nums) {
        int minLen = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length; i++) {
            int[] memo = new int[nums.length+1];    // only memorize the current row
            
            for (int j = i+1; j < nums.length+1; j++) {
                memo[j] = memo[j-1] + nums[j-1];    // overwrite memo every loop
                if (memo[j] >= s)
                    minLen = Math.min(j-i, minLen);
            }
        }
        return (minLen == Integer.MAX_VALUE)? 0 : minLen;
    }

    // Memory Limit Exceeded
    public int minSubArrayLen(int s, int[] nums) {
        int[][] memo = new int[nums.length][nums.length+1];
        
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++)
            for (int j = i+1; j < nums.length+1; j++) {
                memo[i][j] = memo[i][j-1] + nums[j-1];
                if (memo[i][j] >= s)
                    minLen = Math.min(j-i, minLen);
            }
        return (minLen == Integer.MAX_VALUE)? 0 : minLen;
    }
}