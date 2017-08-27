import java.util.*;

class MergeIntervals {

  private static class Interval {
    int start = 0;
    int end = 0;

    Interval( int _start, int _end ) {
      start = _start;
      end = _end;
    }
  }

  private static List<Interval> merge(Interval[] intervals) {
    List<Interval> merged = new ArrayList<>();
    // Sort by start time
    Arrays.sort(intervals, new Comparator<Interval>() {
      public int compare (Interval one, Interval other) {
        if ( one.start == other.start ) 
          return 0;
        else if ( one.start < other.start ) 
          return -1;
        else
          return 1;
      }
    });
  
    merged.add(intervals[0]);
    for ( int i = 1; i < intervals.length; i++ ) {
      Interval curr = intervals[i];
      Interval prev = merged.get(merged.size() - 1);

      if ( prev.end >= curr.start ) {
        merged.remove(prev);
        if ( curr.end > prev.end ) 
          prev.end = curr.end;
        merged.add(prev);
      } else {
        merged.add(curr);
      }
    }

    return merged;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // Number of intervals
    int N = sc.nextInt();
    Interval[] intervals = new Interval[N];


    for ( int i = 0; i < N; i++ ) {
      int start = sc.nextInt();
      int end  = sc.nextInt();
      Interval interval = new Interval(start, end);
      intervals[i] = interval;
    }

    List<Interval> merged = merge(intervals);
    System.out.println();
    System.out.print("Ouput: ");

    for ( int i = 0; i < merged.size(); i++ ) {
      Interval interval = merged.get(i);
      System.out.print("[" + interval.start + ", " + interval.end + "]");
      if ( i < merged.size() - 1) {
        System.out.print(", ");
      }
    }
    System.out.println();
  }
}
