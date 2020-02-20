/**
    wtf? really a waste of time
*/

class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 0) return 0;

        int pivot = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] > nums[i]) pivot = i;
        }
        return (pivot > 0)? nums[pivot] : nums[0];
    }
}