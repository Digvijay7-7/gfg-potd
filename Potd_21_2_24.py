'''
Given a boolean expression s of length n with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer can be large, so return it with modulo 1003

Example 1:

Input: 
n = 7
s = T|T&F^T
Output: 
4
Explaination: 
The expression evaluates to true in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Example 2:

Input: 
n = 5
s = T^F|F
Output: 
2
Explaination: 
((T^F)|F) and (T^(F|F)) are the only ways.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes n and s as input parameters and returns number of possible ways modulo 1003.

Expected Time Complexity: O(n3)
Expected Auxiliary Space: O(n2)

Constraints:
1 ≤ n ≤ 200 
'''

#User function Template for python3

class Solution:
    def countWays(self, N, S):
        # code here
        dp=[[[0,0] for i in range(N)] for j in range(N)]
        for i in range(0,N,2):
            if S[i]=='T':
                dp[i][i][1]=1
            else:
                dp[i][i][0]=1
        for l in range(3,N+1,2):
            for i in range(0,N-l+1,2):
                j=i+l-1
                t=(l-1)//2
                for k in range(1,t+1):
                    k2=2*k
                    if (S[i+k2-1]=='&'):
                        dp[i][j][1]+=dp[i][i+k2-2][1]*dp[i+k2][j][1]
                        dp[i][j][0]+=dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][0]*dp[i+k2][j][1]+dp[i][i+k2-2][0]*dp[i+k2][j][0]
                    elif(S[i+k2-1]=='|'):
                        dp[i][j][0]+=dp[i][i+k2-2][0]*dp[i+k2][j][0]
                        dp[i][j][1]+=dp[i][i+k2-2][0]*dp[i+k2][j][1]+dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][1]*dp[i+k2][j][1]
                    else:
                        dp[i][j][0]+=dp[i][i+k2-2][0]*dp[i+k2][j][0]+dp[i][i+k2-2][1]*dp[i+k2][j][1]
                        dp[i][j][1]+=dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][0]*dp[i+k2][j][1]
        return dp[0][N-1][1]%1003


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends