import java.util.LinkedList;
import java.util.Queue;

class RottenOranges {

    // Helper class to represent coordinates in the grid
    static class Orange {
        int row, col, time;

        public Orange(int row, int col, int time) {
            this.row = row;
            this.col = col;
            this.time = time;
        }
    } //s dsf

    public static int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0) return -1;

        int rows = grid.length;
        int cols = grid[0].length;
        Queue<Orange> queue = new LinkedList<>();
        int freshOranges = 0;
        int timeElapsed = 0;

        // Initialize the queue with all rotten oranges and count fresh oranges
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.add(new Orange(i, j, 0)); // Rotten oranges with initial time 0
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        // Directions for adjacent cells (up, down, left, right)
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // Perform BFS
        while (!queue.isEmpty()) {
            Orange current = queue.poll();
            int row = current.row;
            int col = current.col;
            int time = current.time;

            // Update the time elapsed
            timeElapsed = time;

            // Spread the rot to adjacent fresh oranges
            for (int[] direction : directions) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];

                // Check if the adjacent cell is within bounds and contains a fresh orange
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == 1) {
                    grid[newRow][newCol] = 2; // The fresh orange becomes rotten
                    freshOranges--; // Decrease the count of fresh oranges
                    queue.add(new Orange(newRow, newCol, time + 1)); // Add the new rotten orange to the queue
                }
            }
        }

        // If there are no fresh oranges left, return the time, otherwise return -1
        return freshOranges == 0 ? timeElapsed : -1;
    }

    public static void main
