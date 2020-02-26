class Solution { // matrix: M x N
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;

        List<Integer> rowHeaders = new ArrayList<>();
        for(int[] row : matrix) rowHeaders.add(row[0]);
        
        int rowNum = Collections.binarySearch(rowHeaders, target);  // O(logM)
        
        if (rowNum < 0) rowNum = -rowNum-2;
        if (rowNum < 0) return false;
        
        return (Arrays.binarySearch(matrix[rowNum], target) >= 0)? true : false; // O(logN)
    }
}