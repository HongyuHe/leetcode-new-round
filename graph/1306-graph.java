/*
    take away: dfs
*/

class Solution {
    public boolean canReach(int[] arr, int start) {
        if (arr[start] == 0)
            return true;

        int move = arr[start];
        arr[start] = -1; // visited

        if (start + move < arr.length && dfsJump(start + move, arr)) {
            return true;
        } else if (start - move >= 0 && dfsJump(start - move, arr)) {
            return true;
        }
        return false;
    }

    Boolean dfsJump(int pos, int[] arr) {
        if (pos >= arr.length || pos < 0 || arr[pos] < 0)
            return false;
        if (arr[pos] == 0)
            return true;

        int move = arr[pos];
        arr[pos] = -1; // visited

        if (dfsJump(pos + move, arr) || dfsJump(pos - move, arr)) {
            return true;
        }
        return false;
    }

}

// Solution for check if it can reach all 0s in `arr`

class Solution {
    public boolean canReach(int[] arr, int start) {
        if (arr.length == 1)
            return (arr[0] == 0) ? true : false;

        int numZero = 0;
        for (int i : arr) {
            numZero = (i == 0) ? ++numZero : numZero;
        }

        int move = arr[start];
        int counter = (move == 0) ? 1 : 0;
        arr[start] = -1; // visited

        if (start + move < arr.length && dfsJump(start + move, counter, numZero, arr)) {
            return true;
        } else if (start - move >= 0 && dfsJump(start - move, counter, numZero, arr)) {
            return true;
        }

        return false;
    }

    Boolean dfsJump(int pos, int counter, int numZero, int[] arr) {
        System.out.println("At: [" + pos + "]");
        if (counter == numZero)
            return true;
        if (pos >= arr.length || pos < 0 || arr[pos] < 0)
            return false;
        System.out.println("Val: " + arr[pos]);

        int move = arr[pos];
        if (move == 0)
            counter++;
        arr[pos] = -1; // visited

        if (dfsJump(pos + move, counter, numZero, arr) || dfsJump(pos - move, counter, numZero, arr)) {
            return true;
        }
        return false;
    }
}
