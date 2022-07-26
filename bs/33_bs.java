/**
    0.  a. empty array
        b. no pivot point
    1. traverse the array to find the pivot;
    2. binary search on two parts;
    
    take away: binay=ry search
    time: 20min

*/

class Solution {
    public int search(int[] nums, int target) {
        // 0.a
        if (nums.length == 0) return -1;
        // 1
        int pivot = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] > nums[i])
                pivot = i;
        }
        // 1
        int res = -1;
        if (pivot < 0) { // 1.b
            res = binarySearch(target, 0, nums.length-1, nums);
        } else {
            res = binarySearch(target, 0, pivot-1, nums);
            if (res < 0)
                res = binarySearch(target, pivot, nums.length-1, nums);
        }
        return res;
    }
    
    static int binarySearch(int target, int start, int end, int[] nums) {
        if (start > end)
            return -1;
        
        int mid = (start + end) / 2;
        if (nums[mid] == target) 
            return mid;
        
        if (target > nums[mid])
            return binarySearch(target, mid+1, end, nums);
        else
            return binarySearch(target, start, mid-1, nums);
    }
}









