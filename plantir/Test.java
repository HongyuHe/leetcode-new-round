// package plantir;

import java.util.*;

/**
 * 
 * 1 2 3 0 0 0 4 5 8 -> 0 0 1 9 7 0 1 0 0
 */
public class Test {
    public static void main(String[] args) {
        int M = Integer.parseInt(args[0]);
        int N = Integer.parseInt(args[1]);
        // System.out.println(M);
        // System.out.println(N);
        int[][] field = new int[M][N];

        Scanner in = new Scanner(System.in);
        for (int j = 0; j < M; j++) {
            for (int i = 0; i < N; i++) {
                field[j][i] = in.nextInt();
            }
        }
        in.close();

        int[][] res = new int[M][N];
        // for (int[] row : res) {
        // Arrays.fill(row, -1);
        // }
        List<int[]> highPoints = new ArrayList<>();

        System.out.println(Arrays.deepToString(res));
        test1(field, res, highPoints);
        System.out.println("Find hight points: \n" + Arrays.deepToString(res));
        // System.out.println(highPoints);
        highPoints.forEach(e -> System.out.println(Arrays.toString(e)));

        System.out.println("Sort: ");
        highPoints.sort((p1, p2) -> field[p2[0]][p2[1]] - field[p1[0]][p1[1]]); // desc
        highPoints.forEach(e -> System.out.println(Arrays.toString(e)));

        flood(highPoints, res, field);
        System.out.println("Flood: ");
        System.out.println(Arrays.deepToString(res));

        // test2(field, res);

    }

    public static void test1(int[][] field, int[][] res, List<int[]> hightPoints) {
        for (int i = 0; i < field.length; i++) {
            for (int j = 0; j < field[0].length; j++) {
                if (fill(i, j, field, res)) {
                    res[i][j] = 1;
                    hightPoints.add(new int[] { i, j });
                }

                // else
                // res[i][j] = 0;
                System.out.println(Arrays.deepToString(res));
            }
        }
    }

    public static boolean fill(int row, int col, int[][] field, int res[][]) {
        // if (res[row][col] == 1 || res[row][col] == 0)
        // return field[row][col] == 1;

        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                if (i == 0 && j == 0)
                    continue;
                if (row + i >= 0 && col + j >= 0 && row + i < field.length && col + j < field[0].length
                        && field[row][col] < field[row + i][col + j]) { // q2: <
                    System.out.println("Low: " + field[row][col]);
                    return false;
                }
            }
        }
        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                if (row + i >= 0 && col + j >= 0 && row + i < field.length && col + j < field[0].length)
                    res[row + i][col + j] = 0;
            }
        }
        return true;
    }

    public static void flood(List<int[]> highPoints, int[][] res, int[][] field) {
        for (int[] row : res) {
            Arrays.fill(row, highPoints.size());
        }
        // order???
        for (int i = 0, height = 1; i < highPoints.size(); i++, height++) {
            int[] point = highPoints.get(i);
            if (i > 0 && field[point[0]][point[1]] == field[highPoints.get(i - 1)[0]][highPoints.get(i - 1)[1]]) {
                height--;
            }
            res[highPoints.get(i)[0]][highPoints.get(i)[1]] = height;
        }
    }
}
