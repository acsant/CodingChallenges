import math;
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read in the number of test cases
T = int(raw_input());
# Go through all the test cases
for t in range(T):
    # Read in N
    N = int(raw_input());
    # The dimension of the wall is 4xN
    # Guess: How many configurations are there after placing the first brick?
    # Subproblems: Case 1 = If we place a 1x4 brick, then the rest of the wall is 3x(N-4). Case 2 = If we place a 4x1 brick, then
    # rest of the wall is 4x(N-1). There are O(N) subproblems each solved in constant time
    DP = {};
    # Base case: DP(0) = DP(1) = DP(2) = DP(3) = 1
    DP[0] = DP[1] = DP[2] = DP[3] = 1;
    # Let DP(i) be the number of configurations after placing the ith brick. Considering above cases, DP(i) = DP(i-1) + DP(i-4).
    for i in range(4,N+1):
        DP[i] = DP[i-1] + DP[i-4];
        
    # The total number of configurations is in DP(N)
    M = DP[N];
    
    # Now that we have the number of configurations, we find the prime numbers upto and including M
    array_num = [True for k in range(M+1)];
    
    sqrt_M = int(math.sqrt(M));
    i = 2;
    array_num[0] = False;
    array_num[1] = False;
    while i <= sqrt_M:
        if array_num[i]:
            # Go through all the composites of i and mark them as not-prime
            j = int(math.pow(i, 2));
            while j <= M:
                array_num[j] = False;
                j += i;
        i += 1;
    
    # Count the prime numbers
    count_primes = 0;
    for num in array_num:
        if num:
            count_primes += 1;
    
    # Return the number of prime numbers found
    print count_primes;
        
    