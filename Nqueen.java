import java.util.ArrayList;
import java.util.List;
// redad
public class NQueens {

    // Function to solve the N-Queens problem
    public static List<List<String>> solveNQueens(int n) {
        List<List<String>> solutions = new ArrayList<>();
        char[][] board = new char[n][n];

        // Initialize the board with '.'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        solve(0, board, solutions);
        return solutions;
    }

    // Recursive function to place queens
    private static void solve(int row, char[][] board, List<List<String>> solutions) {
        if (row == board.length) {
            // Convert the board to a list of strings and add to solutions
            solutions.add(construct(board));
            return;
        }

        for (int col = 0; col < board.length; col++)
