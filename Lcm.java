import java.util.*;

public class Lcm {

  // Helper method to calculate the GCD using the euclid's algorithm
  private static int gcd(int a, int b) {
    if ( a == b ) {
      return a;
    } else if ( a < b ) {
      return gcd(a, b-a);
    }

    return gcd(a-b, b);
  }

  public static void main(String[] args) {
    int[] input = new int[args.length];
    // Read the input
    for ( int i = 0; i < args.length; i++ ) {
      input[i] = Integer.parseInt(args[i]);
    }

    int[] DP = new int[input.length];
    DP[0] = input[0];

    // Let DP[i] represent the LCM of numbers from index 0 to i
    for ( int i = 1; i < input.length; i++ ) {
      // LCM(0,i) = LCM( LCM(0,i-1), i )
      DP[i] = Math.abs(DP[i-1] * input[i]) / gcd(DP[i-1], input[i]);
    }

    System.out.println(DP[input.length - 1]);
  }
}
