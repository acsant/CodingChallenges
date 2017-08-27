import java.util.*;
import java.io.*;

class FindLargestSquare {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int M = sc.nextInt();
    int N = sc.nextInt();
    String line;
    int[][] Matrix = new int[N][M];
    for ( int i = 0; i < N; i++ ) {
      for ( int j = 0; j < M; j++ )
        Matrix[i][j] = sc.nextInt();
    }

    int dim = findLargestSquare(Matrix, N, M);
    System.out.println(dim);
  }

  private static int findLargestSquare(int[][] Matrix, int N, int M) {
    int maxSize = -1;
    for ( int i = 0; i < N; i++ ) {
      for ( int j = 0; j < M; j++ ) {
        if ( i >= 1 && j >= 1 && Matrix[i][j] > 0 )
          Matrix[i][j] += Math.min(Math.min(Matrix[i][j-1], Matrix[i-1][j]), Matrix[i-1][j-1]);
        maxSize = Math.max(maxSize, Matrix[i][j]);
      }
    }
    return maxSize;
  }
}
