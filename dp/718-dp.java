/**
 * take away: 2D dp
 * 
 * @link: nice tutorial
 *        https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/109030/return-the-array-instead-of-the-length-Very-simple-dp-solution-with-the-both-max-and-the-array
 * 
 */

class Solution {
    public int findLength(int[] A, int[] B) {
        int[][] dp = new int[A.length + 1][B.length + 1];
        int max = 0;

        for (int j = 0; j < A.length; j++) {
            for (int i = 0; i < B.length; i++) {
                if (A[j] == B[i]) {
                    dp[j + 1][i + 1] = dp[j][i] + 1;
                    max = Math.max(dp[j + 1][i + 1], max);
                }
            }
        }
        return max;
    }
}