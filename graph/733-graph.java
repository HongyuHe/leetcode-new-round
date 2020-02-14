/**
 * take away: 1. initialization of 2D array; 2. input requirements
 * 
 * [[1,1,1], [1,1,0], [1,0,1]]
 * 
 * [[2,2,2], [2,2,0], [2,0,1]]
 * 
 * [[0,0,0], [0,0,0]]
 */

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int N = image.length;
        int M = image[0].length;
        Set<String> visited = new HashSet<>();
        if (N == 1 && M == 1) {
            return new int[][] { new int[] { newColor } };
        }

        Queue<int[]> q = new ArrayDeque<>();
        int sColor = image[sr][sc];
        q.add(new int[] { sr, sc });

        while (!q.isEmpty()) {
            int[] nextPix = q.poll();
            if (checkPix(sColor, nextPix, visited, image)) {
                image[nextPix[0]][nextPix[1]] = newColor;
                addNewPix(q, sColor, nextPix, visited, image);
                visited.add(Integer.toString(nextPix[0]) + Integer.toString(nextPix[1]));
            }
        }
        return image;
    }

    static boolean checkPix(int sColor, int[] coor, Set<String> visited, int[][] image) {
        return coor[0] >= 0 && coor[1] >= 0 && coor[0] < image.length && coor[1] < image[0].length
                && image[coor[0]][coor[1]] == sColor
                && !visited.contains(Integer.toString(coor[0]) + Integer.toString(coor[1]));
    }

    static void addNewPix(Queue<int[]> q, int sColor, int[] newPix, int[][] image) {

        if (checkPix(sColor, new int[] { newPix[0] + 1, newPix[1] }, image))
            q.add(new int[] { newPix[0] + 1, newPix[1] });
        if (checkPix(sColor, new int[] { newPix[0] - 1, newPix[1] }, image))
            q.add(new int[] { newPix[0] - 1, newPix[1] });
        if (checkPix(sColor, new int[] { newPix[0], newPix[1] + 1 }, image))
            q.add(new int[] { newPix[0], newPix[1] + 1 });
        if (checkPix(sColor, new int[] { newPix[0], newPix[1] - 1 }, image))
            q.add(new int[] { newPix[0], newPix[1] - 1 });
    }
}
