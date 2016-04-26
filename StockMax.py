# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read in the number of test cases
T = int(raw_input());
for k in range(T):
    # Size of the current stock price array
    N = int(raw_input());
    # Read in the list of stock prices
    price = raw_input().split(" ");
    # Now we solve this problem using Dynamic Programming
    # Guess: Should I buy the share or sell it at any given day i?
    # Subproblems: There are O(n) sub-problems and each can be solved in O(1) time. So the overall time complexity is O(n)
    # Let DP(i) be the profit on day i, which is the profit accumulated from day i to day n. 
    # Throughout the trading process, j >= 0 where j is the number of shares owned 
    # This gives us a base case: DP(N) = 0 since profit made from day n to day n is 0
    DP = {};
    DP[N] = 0;
    # We only sell when the price is the highest to gain max profit so keep track of max price
    # Current differnce in buying and selling price is added to previously calculated profit to get current profit
    current_max_price = 0; # since all shares are between 0 and 100000
    for i in range(N-1, -1, -1):
        # From the above speculations, the recurrence is fairly clear: DP(i) = DP(i+1) + max{price[i, ..., n]} - price(i)
        current_max_price = max(current_max_price, int(price[i]));
        DP[i] = DP[i+1] + current_max_price - int(price[i]);
        
    # we now just trust this recurrence to give us a solution at DP(0)    
    print DP[0];