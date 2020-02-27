/*      Brute Force: 1 - nums[last]
        Binary Search: 1- mid -last

    takeaways:
            1. how to decide the guard of the D&C recusion;
            2. upper bound divsion treak // other than Math.ceil() / floor
*/
class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int end = nums[nums.length-1];
        return binarySearch(nums, threshold, 1, end);
    }
    
    public static int binarySearch(int[] nums, int threshold, int start, int end) {
        if (start >= end) return end;
        
        int sum = 0;
        int divisor = (start + end) / 2;
        for (int num : nums) {
            sum += (divisor + num - 1) / divisor; // take the upper bound;
        }
        
        if (sum <= threshold) 
            return binarySearch(nums, threshold, start, divisor); // => equal gaurd
        else
            return binarySearch(nums, threshold, divisor+1, end); // > start > end gaurd
    }
}