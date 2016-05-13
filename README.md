# Solutions to coding challenges

## Maximum Subarray problem
> Given an array A = {a1, a2, ..., an} of N elements, find the maximum possible sum of a :
* Contiguous Subarray
* Non-contiguous subarray

###### Sample Input
2

4

1 2 3 4

6

2 -1 2 3 4 -5
###### Sample Output
10 10

10 11

## Friend Circle
> Given a NxN matrix M, M[i][j] = Y iff person i and j are friends for all i,j. 
> Else M[i][j] = N. The friendships are transitive. In other words, if A is a friend of B and B is a friend of C, then A and C are also friends. The goal is to find the number of all the independent friend circles.

###### Sample Input
4

YYNN

YYYN

NYYN

NNNY
###### Sample Output
2

## Stock Maximize
> Given T test cases where each test cases consists of N stock prices for N days. The goal is to figure out the maximum possible profit that can be made from an optimal trading stratergy.

###### Sample Input
3

3

5 3 2

3

1 2 100

4

1 3 1 2
###### Sample Output
0

197

3

## Red John Is Back
> Red John is a murdered who likes to leave clues. There is a 4xN wall in the victim's house. There is also an infinite supply of bricks where each brick is either a 1x4 or a 4x1 in dimensions. To find the murderer, one must find the number of all possible configurations in which the wall can be covered by the available bricks. Let this number be M. Now we must find all the prime numbers upto and including M.

###### Sample Input
2  // Number of test cases

1  // First test case

7  // Second test case
###### Sample Output
0  

3

> There is only 1 configuration for the first test case. So 0 prime numbers. For the second test case, there are 5 configurations (M = 5). There are 3 prime numbers upto and including 5, which are 2, 3, and 5. Hence the output is 0 for first test case and 3 for the second test case.  

## The city with blinding lights
> Given a directed, weighted graph, consisting of N nodes and there are edges, of specified length between some of them in the graph. Given Q questions, inquiring the shortest distance between a queried pair of nodes in the graph. Answer all the queries as quickly as possible.

###### Sample Input
4 5 // Number of nodes and edges

1 2 5 // First two numbers are nodes and last int is weight of the edge between
the two nodes

1 4 24

2 4 6

3 4 4

3 2 7

3

1 2  // Shortest path from 1 to 2 is of length 5

3 1  // No paths from 3 to 1

1 4  // Shortest path from 1 to 4 is of length 11

###### Sample Output
5

-1

11
