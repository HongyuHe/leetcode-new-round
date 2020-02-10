/*
    take away: the manipulation of binary search indeices is subtle.
*/

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ans = new LinkedList<>();
        int index = Arrays.binarySearch(arr, x);

        if (index < 0) {
            index = binarySearch(arr, x, 0, arr.length - 1);
        }
        int right = index + 1;
        int left = index;

        while (ans.size() < k) {
            int lAbs = (left < 0) ? Integer.MAX_VALUE : Math.abs(arr[left] - x);
            int rAbs = (right >= arr.length) ? Integer.MAX_VALUE : Math.abs(arr[right] - x);

            if (lAbs <= rAbs) {
                ans.add(0, arr[left]);
                left--;
            } else {
                ans.add(arr[right]);
                right++;
            }
        }
        return ans;
    }

    // 1 4 5 6 8 9 -> 7?
    static int binarySearch(int[] arr, int x, int start, int end) {
        if (start >= end) {
            return start - 1;
        }

        int mid = (start + end) / 2;
        if (x >= arr[mid]) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }

        return binarySearch(arr, x, start, end);
    }
}
