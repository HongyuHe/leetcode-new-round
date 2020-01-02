// DFS union

// [/][/]
// [/][ ]

// [ ][ ][/][ ][ ][/]
// [ ][/][ ][ ][/][ ]
// [/][ ][ ][/][ ][ ]
// [ ][ ][/][ ][ ][ ]
// [ ][/][ ][ ][ ][ ]
// [/][ ][ ][ ][ ][ ]

// Space complexity can be improved by using Bitset rather than Boolean[][];
class Solution {
    public int regionsBySlashes(String[] grid) {
        final int N = grid.length;
        Boolean[][] map = new Boolean[3 * N][3 * N];

        for (Boolean[] row : map)
            Arrays.fill(row, true);

        for (int j = 0; j < N; j++) {
            for (int i = 0; i < N; i++) {
                if (grid[j].charAt(i) != ' ') {
                    if (grid[j].charAt(i) == '/')
                        map[3 * j + 2][3 * i] = map[3 * j + 1][3 * i + 1] = map[3 * j][3 * i + 2] = false;
                    if (grid[j].charAt(i) == '\\')
                        map[3 * j][3 * i] = map[3 * j + 1][3 * i + 1] = map[3 * j + 2][3 * i + 2] = false;
                }
            }
        }
        // printMap(map);

        int region = 0;
        for (int j = 0; j < 3 * N; j++) {
            for (int i = 0; i < 3 * N; i++) {
                if (map[j][i]) {
                    dfs(j, i, map);
                    region++;
                }
                // printMap(map);
            }
        }

        return region;
    }

    void dfs(int row, int col, Boolean[][] map) {

        if (row < 0 || row >= map.length || col < 0 || col >= map.length || !map[row][col])
            return;

        map[row][col] = false;

        dfs(row + 1, col, map);
        dfs(row - 1, col, map); // if we don't search upwards, then it will fail on up-corner case [" /"," "]
        dfs(row, col - 1, map);
        dfs(row, col + 1, map);
    }

    // test
    void printMap(Boolean[][] map) {
        for (int j = 0; j < map.length; j++) {
            for (int i = 0; i < map.length; i++) {
                System.out.print(map[j][i] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
