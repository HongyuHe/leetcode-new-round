/*
    [[1,0,1,0],
     [0,0,1,0],
     [0,0,1,0],
     [0,0,0,1]]
*/

class Solution {
    int O = 0;

    public int countServers(int[][] grid) {

        int m = grid.length;
        int n = grid[0].length;

        int numServer = 0;

        for (int j = 0; j < m; j++) { // O(mn + numServer*max(m,n)) == O(16+6*4) = O(16+24) < O(n^2+n^2) = O(n^2)
            for (int i = 0; i < n; i++) {
                if (grid[j][i] == 1) {
                    int connections = dfs(j, i, grid);
                    if (connections > 0) {
                        numServer += ++connections; // add connections and itself;
                    }
                    // O++;
                }
                O++;
            }
        }
        System.out.println("O: " + O);
        return numServer;
    }

    int dfs(int row, int col, int[][] grid) {
        // O++;
        // System.out.println("Check: "+row+" "+col);
        grid[row][col]++; // visited
        for (int[] r : grid) {
            for (int cell : r) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
        System.out.println("-------------");

        int counter = 0;
        for (int i = 0; i < grid[row].length; i++) { // check row
            if (grid[row][i] == 1) {
                counter++;
                counter += dfs(row, i, grid);
            }
            O++;
        }

        for (int i = 0; i < grid.length; i++) { // check col
            if (grid[i][col] == 1) {
                counter++;
                counter += dfs(i, col, grid);
            }
        }
        return counter;
    }

}