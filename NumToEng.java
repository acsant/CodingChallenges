import java.util.*;
import java.io.*;

class NumToEng {
  static String[] ones = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
  };

  static String[] twos = {
    "", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
  };

  static String[] tens = {
    "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
  };

  static String[] powers = {
    "hundred", "thousand"
  };

  public static void main(String[] args) {
    String num = args[0];
    System.out.println(convert(num));
  }

  private static String convert( String num ) {
    int index = Integer.parseInt(num);
    if ( num.length() == 1 )
      return ones[index];

    if ( num.length() == 2 ) {
      if ( index % 10 == 0 ) {
        return tens[index/10];
      } else {
        if ( index < 20 )
          return twos[index%10];
        return convert(String.valueOf(index - index%10)) + " " + convert(String.valueOf(index%10));
      }
    } else {
      String res;
      if ( num.length() > 3 ) {
        int curr = index / 1000;
        res = convert(String.valueOf(curr)) + " " + powers[1];
        if ( index % 1000 != 0 )
          res += " " + convert(String.valueOf(index % 1000));
        return res;
      } else {
        int curr = index / 100;
        res = convert(String.valueOf(curr)) + " " + powers[0];
        if ( index % 100 != 0 )
          res += " " + convert(String.valueOf(index%100));
        return res;
      }
    }
  }
}
