/**
    @logic: same as 33
    
    @take away: binay=ry search
    @time: 4min

*/

class Solution {
    public boolean search(int[] nums, int target) {
        // 0.a
        if (nums.length == 0) return false;
        // 1
        int pivot = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] > nums[i])
                pivot = i;
        }
        // 1
        boolean res = false;
        if (pivot < 0) { // 1.b
            res = binarySearch(target, 0, nums.length-1, nums);
        } else {
            res = binarySearch(target, 0, pivot-1, nums);
            if (!res)
                res = binarySearch(target, pivot, nums.length-1, nums);
        }
        return res;
    }
    
    static boolean binarySearch(int target, int start, int end, int[] nums) {
        if (start > end)
            return false;
        
        int mid = (start + end) / 2;
        if (nums[mid] == target) 
            return true;
        
        if (target > nums[mid])
            return binarySearch(target, mid+1, end, nums);
        else
            return binarySearch(target, start, mid-1, nums);
    }
}









