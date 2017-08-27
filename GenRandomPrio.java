import java.util.*;
import java.text.*;

class GenRandomPrio {
  static int MAX = 10;
  static double[][] output = new double[10][10];
  static double[][] sumMatrix = new double[10][10];

  public static void main(String[] args) {
    for ( int k = 0; k < 6; k++ ) {
      for ( int i = 0; i < MAX; i++ ) {
        for ( int j = 0; j < MAX; j++ ) {
          if ( i == j ) {
            output[i][j] = 1;
          } else if ( j < i ) {
            output[i][j] = 1/output[j][i];
          } else {
            int rand = (int)(Math.random()*3);
            double powered = Math.pow(2, rand);
            output[i][j] = powered;
          }
          sumMatrix[i][j] += output[i][j];
          System.out.print(new DecimalFormat("0.00").format(output[i][j]));
          if ( j < MAX - 1 )
            System.out.print(" ");
        }
        System.out.println();
      }
      System.out.println();
      System.out.println();
      System.out.println();
    }

    // output sum
    System.out.println("AVG MATRIX");
    for ( int i = 0; i < MAX; i++ ) {
      for ( int j = 0; j < MAX; j++ ) {
        System.out.print(new DecimalFormat("0.00").format(sumMatrix[i][j]/6));
        if ( j < MAX - 1 )
          System.out.print(" ");

      }
      System.out.println();
    }
  }


}
