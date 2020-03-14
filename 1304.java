// a waste of time
// 10m

class Solution {
    public int[] sumZero(int n) {
        if (n == 0)
            return new int[0];

        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n / 2; i++) {
            res.add(i);
            res.add(-i);
            // System.out.println(i);
        }
        if (n % 2 == 1) {
            res.add(0);
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}