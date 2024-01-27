'''
Given an array p[] of length n used to denote the dimensions of a series of matrices such that the dimension of i'th matrix is p[i] * p[i+1]. There are a total of n-1 matrices. Find the most efficient way to multiply these matrices together. 
As in MCM, you were returning the most effective count but this time return the string which is formed of A - Z (only Uppercase) denoting matrices & Brackets( "(" ")" ) denoting multiplication symbols. For example, if n =11, the matrixes can be denoted as A - K as n<=26 & brackets as multiplication symbols.

NOTE:
Each multiplication is denoted by putting open & closed brackets to the matrices multiplied & also Please note that the order of matrix multiplication matters, as matrix multiplication is non-commutative A*B != B*A
As there can be multiple possible answers, the console would print "True" for the correct string and "False" for the incorrect string. You need to only return a string that performs a minimum number of multiplications.

Example 1:
Input: 
n = 5
p[] = {40, 20, 30, 10, 30}
Output: 
True
Explaination: 
Let's divide this into matrix(only 4 are possible) 
[ [40, 20] -> A
, [20, 30] -> B
, [30, 10] ->C
, [10, 30] -> D ]
First we perform multiplication of B & C -> (BC)
then we multiply A to (BC) -> (A(BC))
then we multiply D to (A(BC)) -> ((A(BC))D)
so the solution returned the string ((A(BC))D), which performs minimum multiplications. The total number of multiplications are 20*30*10 + 40*20*10 + 40*10*30 = 26,000.

Example 2:
Input: 
n = 3
p = {3, 3, 3}
Output: 
True
Explaination: 
The solution returned the string (AB), which performs minimum multiplications. The total number of multiplications are (3*3*3) = 27.
Your Task:
You do not need to read input or print anything. Your task is to complete the function matrixChainOrder() which takes n and p[] as input parameters and returns the string of parenthesis for n-1 matrices. Use uppercase alphabets to denote each matrix.

Expected Time Complexity: O(n^3)
Expected Auxiliary Space: O(n^2)
'''
#User function Template for python3

class Solution:
    def matrixChainOrder(self, p, n):
        # Creating a table to store the results of subproblems
        dp = [[0] * n for _ in range(n)]

        # Initializing the table with 0 for single matrix products
        for i in range(1, n):
            dp[i][i] = 0

        # Loop to fill the dp table
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')  # Initializing with infinity

                for k in range(i, j):
                    # Updating the minimum cost
                    cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        # Constructing the matrix chain multiplication string
        matrix_string = self.constructMatrixString(1, n - 1, dp)

        return matrix_string

    def constructMatrixString(self, i, j, dp):
        if i == j:
            return chr(65 + i - 1)  # Convert index to uppercase letter

        min_cost_index = -1
        min_cost = float('inf')

        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
            if cost < min_cost:
                min_cost = cost
                min_cost_index = k

        left_matrix = self.constructMatrixString(i, min_cost_index, dp)
        right_matrix = self.constructMatrixString(min_cost_index + 1, j, dp)
        matrix_string = "(" + left_matrix + right_matrix + ")"

        return matrix_string


#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends