/*
    take away: 
        - edge cases!
        - bound check!
    
    Brute force: iterate all and check left and right
    [1,3,4,10,3,5,6,4,1,2,3,1]
*/

// good binary search

class Solution {
    public:
    
    int findPeakElement(const vector<int> &num) {
        return Helper(num, 0, num.size()-1);
    }
    int Helper(const vector<int> &num, int low, int high) {
        if(low == high)
            return low;
        else {
            int mid1 = (low+high)/2;
            int mid2 = mid1+1;
            if(num[mid1] > num[mid2])
                return Helper(num, low, mid1);
            else
                return Helper(num, mid2, high);
        }
    }
};

// my stupid solution:
class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) return 0;
        
        int midIndex = nums.length / 2;
        Set<Integer> checked = new HashSet<Integer>();
        
        return recurFind(midIndex, nums, checked); // ask whether it's guaranteed to have a peek 
    }
    
    public static int recurFind(int currIndex, int[] nums, Set<Integer> checked) {
        if (currIndex < 0 || currIndex >= nums.length || checked.contains(currIndex)) 
            return -1;
        checked.add(currIndex);

        if ((currIndex == 0 && nums[currIndex] > nums[1]) ||
            (currIndex == nums.length-1 && nums[currIndex] > nums[nums.length-2]))
            return currIndex;

        int leftOffSet = -1;
        int rightOffSet = 1;
        if (currIndex != 0 && nums[currIndex] > nums[currIndex-1]) 
            leftOffSet = -2;
        if (currIndex != nums.length-1 && nums[currIndex] > nums[currIndex+1]) 
            rightOffSet = 2;
        
        if (rightOffSet == 2 && leftOffSet == -2) {
            return currIndex;
        } else {
            int peek = recurFind(currIndex+rightOffSet, nums, checked);
            if (peek < 0) {
                peek = recurFind(currIndex+leftOffSet, nums, checked);
            }
            return peek;
        }
    }
}