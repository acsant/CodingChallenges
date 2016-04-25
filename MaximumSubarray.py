# Enter your code here. Read input from STDIN. Print output to STDOUT
m = raw_input();
arrList = [];
for i in range(int(m)):
    n = raw_input();
    arrList.append(raw_input());
    
for arr in arrList:
    A = [int(s) for s in arr.split(' ')];
    # let DP(i) be the sum of subarray from A{i, ..., j} for some j >= i
    # let DPNON(i) be the non-contiguous sum of the subarray from A{0,...,i}
    # we need to guess whether to include the next index in the sum or not
    # of subproblems is O(n), each takes constant time to solve hence the algorithm completes in O(n)
    DP = {};
    DPNON = {};
    # base case -infinity
    DP[-1] = -pow(10,4);
    DPNON[-1] = -pow(10,4);
    # initialize the sums to the lowest
    contiguousSum = -pow(10,4);
    # Recurrence
    for i in range(len(A)):
	# from the above speculations, we come up with a recurrence for contiguous and non-contiguous subarray sums (max)
        DP[i] = max(DP[i-1] + A[i], A[i]);
	# slight modification for non-contiguous - we must also include the previous solution for DP(i-1)
        DPNON[i] = max(DPNON[i-1] + A[i], A[i], DPNON[i-1]);
        
    for k in range(len(A)):
        contiguousSum = max(DP[k], contiguousSum);
    print(str(contiguousSum) + " " + str(DPNON[len(A) - 1])) ;

