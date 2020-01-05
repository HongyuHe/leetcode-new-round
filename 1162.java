// a super ugly solution ...

import java.util.*;

class Solution {
    public int maxDistance(int[][] grid) {
        List<ArrayList<Integer>> checker = new ArrayList<ArrayList<Integer>>();
        int N = grid.length;
        
        for (int j = 0; j < N; j++) {
            checker.add(new ArrayList());
            for (int i = 0; i < N; i++) {checker.get(j).add(grid[j][i]);}
        }
        
        // check -1;
        if (checker.stream().allMatch(row -> row.stream().allMatch(cell->cell == 0)) || 
            checker.stream().allMatch(row -> row.stream().allMatch(cell->cell == 1)))
            return -1;
        
        int maxLevel = -1;
        for (int j = 0; j < N; j++) {
            for (int i = 0; i < N; i++) {
                if (grid[j][i] == 0) { // find a water-cell
                    int level = 1;
                    
                    while(level <= (N-1)*2) {
                        Boolean touchLand = false;
                        for (int r = 0; r <= level; r++) { // expand
                            int c = level - r;
                            
                            if (j+r < N && i+c < N && grid[j+r][i+c] == 1 ||
                                j-r >=0 && i-c >=0 && grid[j-r][i-c] == 1 ||
                                j+r < N && i-c >=0 && grid[j+r][i-c] == 1 ||
                                j-r >=0 && i+c < N && grid[j-r][i+c] == 1) {
                                touchLand = true;
                                break;
                            }
                        }
                        if (touchLand) 
                            break;
                        level++;
                    }
                    if (level == (N-1)*2+1) level--;
                    maxLevel = Math.max(level, maxLevel);
                    level = 1;
                }
            } 
        }
        return maxLevel;
    }
}